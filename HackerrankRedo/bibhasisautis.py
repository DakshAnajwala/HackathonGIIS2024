import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from flask import Flask, render_template_string
import json
import requests

# Sample data
eli_dict = {
    "Afghanistan": 45,
    "Albania": 70,
    "Algeria": 65,
    "Andorra": 80,
    "Angola": 60,
    "Antigua and Barbuda": 75,
    "Argentina": 78,
    "Armenia": 68,
    "Australia": 80,
    "Austria": 82,
    "Azerbaijan": 64,
    "Bahamas": 77,
    "Bahrain": 66,
    "Bangladesh": 60,
    "Barbados": 73,
    "Belarus": 69,
    "Belgium": 76,
    "Belize": 71,
    "Benin": 62,
    "Bhutan": 67,
    "Bolivia": 72,
    "Bosnia and Herzegovina": 65,
    "Botswana": 70,
    "Brazil": 88,
    "Brunei": 74,
    "Bulgaria": 67,
    "Burkina Faso": 58,
    "Burundi": 61,
    "Cabo Verde": 69,
    "Cambodia": 66,
    "Cameroon": 63,
    "Canada": 82,
    "Central African Republic": 55,
    "Chad": 53,
    "Chile": 77,
    "China": 73,
    "Colombia": 76,
    "Comoros": 60,
    "Congo, Republic of the": 64,
    "Congo, Democratic Republic of the": 65,
    "Costa Rica": 72,
    "Croatia": 70,
    "Cuba": 71,
    "Cyprus": 74,
    "Czech Republic": 78,
    "Denmark": 83,
    "Djibouti": 62,
    "Dominica": 72,
    "Dominican Republic": 68,
    "East Timor": 67,
    "Ecuador": 71,
    "Egypt": 67,
    "El Salvador": 69,
    "Equatorial Guinea": 59,
    "Eritrea": 56,
    "Estonia": 74,
    "Eswatini": 65,
    "Ethiopia": 58,
    "Fiji": 73,
    "Finland": 85,
    "France": 77,
    "Gabon": 62,
    "Gambia": 60,
    "Georgia": 68,
    "Germany": 76,
    "Ghana": 70,
    "Greece": 75,
    "Grenada": 74,
    "Guatemala": 68,
    "Guinea": 60,
    "Guinea-Bissau": 57,
    "Guyana": 66,
    "Haiti": 54,
    "Honduras": 65,
    "Hungary": 73,
    "Iceland": 82,
    "India": 75,
    "Indonesia": 85,
    "Iran": 66,
    "Iraq": 50,
    "Ireland": 79,
    "Israel": 72,
    "Italy": 79,
    "Jamaica": 68,
    "Japan": 80,
    "Jordan": 67,
    "Kazakhstan": 70,
    "Kenya": 73,
    "Kiribati": 65,
    "Korea, North": 52,
    "Korea, South": 74,
    "Kuwait": 63,
    "Kyrgyzstan": 66,
    "Laos": 62,
    "Latvia": 73,
    "Lebanon": 69,
    "Lesotho": 64,
    "Liberia": 58,
    "Libya": 61,
    "Liechtenstein": 80,
    "Lithuania": 74,
    "Luxembourg": 78,
    "Madagascar": 60,
    "Malawi": 63,
    "Malaysia": 78,
    "Maldives": 67,
    "Mali": 55,
    "Malta": 76,
    "Marshall Islands": 68,
    "Mauritania": 62,
    "Mauritius": 74,
    "Mexico": 74,
    "Micronesia": 66,
    "Moldova": 67,
    "Monaco": 82,
    "Mongolia": 69,
    "Montenegro": 72,
    "Morocco": 68,
    "Mozambique": 61,
    "Myanmar": 59,
    "Namibia": 72,
    "Nauru": 64,
    "Nepal": 63,
    "Netherlands": 77,
    "New Zealand": 81,
    "Nicaragua": 68,
    "Niger": 56,
    "Nigeria": 69,
    "North Macedonia": 66,
    "Norway": 84,
    "Oman": 67,
    "Pakistan": 65,
    "Palau": 71,
    "Panama": 73,
    "Papua New Guinea": 62,
    "Paraguay": 70,
    "Peru": 72,
    "Philippines": 70,
    "Poland": 71,
    "Portugal": 74,
    "Qatar": 68,
    "Romania": 73,
    "Russia": 78,
    "Rwanda": 61,
    "Saint Kitts and Nevis": 76,
    "Saint Lucia": 73,
    "Saint Vincent and the Grenadines": 71,
    "Samoa": 68,
    "San Marino": 78,
    "Sao Tome and Principe": 60,
    "Saudi Arabia": 67,
    "Senegal": 63,
    "Serbia": 68,
    "Seychelles": 75,
    "Sierra Leone": 58,
    "Singapore": 80,
    "Slovakia": 72,
    "Slovenia": 76,
    "Solomon Islands": 65,
    "Somalia": 57,
    "South Africa": 81,
    "South Sudan": 55,
    "Spain": 76,
    "Sri Lanka": 68,
    "Sudan": 56,
    "Suriname": 66,
    "Sweden": 82,
    "Switzerland": 79,
    "Syria": 60,
    "Taiwan": 74,
    "Tajikistan": 63,
    "Tanzania": 62,
    "Thailand": 75,
    "Togo": 59,
    "Tonga": 67,
    "Trinidad and Tobago": 74,
    "Tunisia": 68,
    "Turkey": 73,
    "Turkmenistan": 62,
    "Tuvalu": 65,
    "Uganda": 60,
    "Ukraine": 67,
    "United Arab Emirates": 69,
    "United Kingdom": 80,
    "United States": 79,
    "Uruguay": 77,
    "Uzbekistan": 64,
    "Vanuatu": 68,
    "Vatican City": 80,
    "Venezuela": 69,
    "Vietnam": 72,
    "Yemen": 55,
    "Zambia": 62,
    "Zimbabwe": 66
}

# Define a custom color scale from green to red
custom_color_scale = [
    [0, 'red'],  # Low values in red
    [0.5, 'yellow'],  # Intermediate values in yellow
    [1, 'green']  # High values in green
]

# Load GeoJSON data for country boundaries
url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
response = requests.get(url)
countries_geojson = json.loads(response.text)


def create_map(df):
    # Create the choropleth map
    fig = go.Figure(go.Choroplethmapbox(
        geojson=countries_geojson,
        locations=df['Country'],
        z=df['ELI'],
        colorscale=custom_color_scale,
        marker_opacity=0.5,
        marker_line_width=0,
        colorbar_title='ELI Score'
    ))

    # Update the layout
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=1,
        mapbox_center={"lat": 0, "lon": 0},
        title_text='Elemental Life Index (ELI) World Map',
        height=600,
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )

    # Add hover effects
    fig.update_traces(
        hoverinfo='text',
        hovertemplate='<b>%{location}</b><br>ELI: %{z}<extra></extra>',
        marker=dict(line=dict(width=0.5, color='black'))  # Outline color
    )

    return fig


if _name_ == '_main_':
    st.set_page_config(page_title="ELI - Elemental Life Index", layout="wide")

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(eli_dict, orient='index', columns=['ELI'])
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Country'}, inplace=True)

    st.title("ELI - Elemental Life Index")
    st.text("What is ELI? Read further to find out more about our brand new index!")

    # Create and display the interactive map
    fig = create_map(df)
    st.plotly_chart(fig, use_container_width=True)

    eli_description = """
    *The "Elemental Life Index" (ELI)* is a composite metric representing the status of a country's relationship with essential life elements. It reflects how well a country supports life through the availability and management of these elements. Here's a breakdown of what ELI could include:

    1. *Biodiversity*: Measures the variety and variability of life within the country, including the number of species and ecosystems.
    2. *Soil Fertility*: Assesses the richness of soil in essential nutrients required for plant growth and agricultural productivity.
    3. *Air Quality*: Evaluates the cleanliness of the air and the presence of pollutants that can affect human health and ecosystems.
    4. *Water Quality*: Examines the availability and cleanliness of water resources, including rivers, lakes, and groundwater.
    5. *Elemental Abundance*: Looks at the presence and accessibility of critical elements like carbon, nitrogen, oxygen, phosphorus, and trace elements necessary for biological processes.
    6. *Environmental Health*: Considers overall environmental conditions, including the impact of human activities on ecosystems and natural resources.
    7. *Human Health*: Includes metrics related to nutrition, access to clean water, and air, reflecting how elemental availability impacts public health.
    """

    st.markdown(eli_description)

# Flask app section
app = Flask(_name_)

# Load world map data
world_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')


def create_gdp_map():
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
        title_text='World GDP (Hover over a country to enlarge)',
        height=600,
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )

    # Add hover effects
    fig.update_traces(
        hoverinfo='text',
        hovertemplate='<b>%{location}</b><br>GDP: %{z} Billion USD<extra></extra>',
        marker=dict(line=dict(width=0.5, color='black'))  # Outline color
    )

    return fig


@app.route('/')
def index():
    fig = create_gdp_map()

    # Create a custom HTML template with the plot and a div for country info
    html_template = '''
    <html>
        <head>
            <title>Interactive World Map</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f0f0;
                }
                #map {
                    width: 80%;
                    height: 80%;
                }
                .hover:hover {
                    transform: scale(1.05);
                    transition: transform 0.3s;
                }
            </style>
        </head>
        <body>
            <div id="map"></div>
            <script>
                var plotDiv = document.getElementById('map');
                var plotData = {{ plot_div | safe }};
                Plotly.newPlot(plotDiv, plotData.data, plotData.layout);

                // Add hover effect
                plotDiv.on('plotly_hover', function(data) {
                    var country = data.points[0].location;
                    var countryPath = document.querySelectorAll('path[title="' + country + '"]');
                    countryPath.forEach(function(path) {
                        path.classList.add('hover');
                    });
                });

                plotDiv.on('plotly_unhover', function(data) {
                    var country = data.points[0].location;
                    var countryPath = document.querySelectorAll('path[title="' + country + '"]');
                    countryPath.forEach(function(path) {
                        path.classList.remove('hover');
                    });
                });
            </script>
        </body>
    </html>
    '''

    # Convert the plot to HTML
    plot_div = pio.to_html(fig, full_html=False)

    return render_template_string(html_template, plot_div=plot_div)


if __name__ == '_main_':
    app.run(debug=True)