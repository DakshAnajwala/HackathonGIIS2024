import streamlit as st
import pandas as pd
import plotly.express as px

# Define your DataFrame
eli_dict = {
    "Afghanistan": 45,
    "Albania": 70,
    "Algeria": 65,
    "Australia": 80,
    "Brazil": 88,
    # Add other countries
    "Zimbabwe": 66
}
df = pd.DataFrame.from_dict(eli_dict, orient='index', columns=['ELI'])
df.reset_index(inplace=True)
df.rename(columns={'index': 'Country'}, inplace=True)

# Create a custom color scale from green to red
custom_color_scale = [
    [0, 'red'],
    [0.5, 'yellow'],
    [1, 'green']
]

# Streamlit app
st.title('Elemental Life Index Visualization')

# Dropdown menu to select a country
selected_country = st.selectbox('Select a country', df['Country'])

# Filter DataFrame based on selected country
selected_data = df[df['Country'] == selected_country]

# Display the selected country's ELI value
st.write(f"**Elemental Life Index for {selected_country}:** {selected_data['ELI'].values[0]}")

# Create a Plotly choropleth map
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="ELI",
    hover_name="Country",
    hover_data=["ELI"],
    color_continuous_scale=custom_color_scale
)

fig.update_layout(title_text='Elemental Life Index by Country')
st.plotly_chart(fig)