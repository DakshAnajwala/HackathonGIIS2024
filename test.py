import streamlit as st
import plotly.express as px
import pandas as pd

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

# Convert the dictionary to a DataFrame, whilst creating a dataframe
df = pd.DataFrame.from_dict(eli_dict, orient='index', columns=['ELI'])

# Reset index to make 'Country' a column rather than an index
df.reset_index(inplace=True)
df.rename(columns={'index': 'Country'}, inplace=True)
print(df.head())

# Define a custom color scale from green to red
custom_color_scale = [
    [0, 'red'],  # Low values in red
    [0.5, 'yellow'],  # Intermediate values in yellow
    [1, 'green']  # High values in green
]

# Create a Plotly choropleth map
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="ELI",
    hover_name="Country",
    hover_data=["ELI"],
    color_continuous_scale=custom_color_scale  # Reverse the RdYlGn scale for green to red
    # color_continuous_scale=px.colors.sequential.Plasma
)

# Set the title of the map
fig.update_layout(
    title_text="World Map with Hover Data",
    geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular")
)

# Display the map in Streamlit
st.title("Interactive World Map")
st.plotly_chart(fig)
