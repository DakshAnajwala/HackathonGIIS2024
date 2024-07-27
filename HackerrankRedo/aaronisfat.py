import plotly.graph_objects as go
import plotly.io as pio
from flask import Flask, render_template_string
import pandas as pd
import json
import requests
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl

app = Flask('_name_')

# Wolfram One session
session = WolframLanguageSession()

# Load world map data
world_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

# Load GeoJSON data for country boundaries
url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
response = requests.get(url)
countries_geojson = json.loads(response.text)


def create_map():
    # Create the choropleth map
    fig = go.Figure(go.Choroplethmapbox(
        geojson=countries_geojson,
        locations=world_data['CODE'],
        z=world_data['GDP (BILLIONS)'],
        colorscale='Viridis',
        marker_opacity=0.5,
        marker_line_width=0,
        colorbar_title='GDP Billions USD'
    ))

    # Update the layout
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=1,
        mapbox_center={"lat": 0, "lon": 0},
        title_text='World GDP (Click on a country for more info)',
        height=600,
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )

    # Add click event
    fig.update_traces(
        hoverinfo='text',
        hovertemplate='<b>%{location}</b><br>GDP: %{z} Billion USD<extra></extra>',
    )

    return fig


@app.route('/')
def index():
    fig = create_map()

    # Create a custom HTML template with the plot and a div for country info
    html_template = '''
    <html>
        <head>
            <title>Interactive World Map</title>
        </head>
        <body>
            <div id="map">{{ plot_div | safe }}</div>               
            <div id="country-info"></div>
            <script>
                var plot = document.getElementById('map').children[0];
                plot.on('plotly_click', function(data) {
                    var country = data.points[0].location;
                    fetch('/country/' + country)
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('country-info').innerHTML = 
                                '<h2>' + data.name + '</h2>' +
                                '<p>Population: ' + data.population + '</p>' +
                                '<p>Area: ' + data.area + ' sq km</p>' +
                                '<p>GDP: $' + data.gdp + ' billion</p>';
                        });
                });
            </script>
        </body>
    </html>
    '''

    # Convert the plot to HTML
    plot_div = pio.to_html(fig, full_html=False)

    return render_template_string(html_template, plot_div=plot_div)


@app.route('/country/<name>')
def get_country_data(name):
    # Fetch country data using Wolfram One
    try:
        data = session.evaluate(wl.CountryData(name, ["Name", "Population", "Area", "GDP"]))
        return {
            'name': str(data[0]),
            'population': str(data[1]),
            'area': str(data[2]),
            'gdp': str(data[3])
        }
    except Exception as e:
        return {'error': str(e)}, 400


if _name_ == '_main_':
    app.run(debug=True)