import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd



header = st.container()
with header:
    st.title('Rural Fire Services Location Report')

features = st.container()
with features:
    st.header('Fire location map')


    df=pd.read_csv('streamlit_data_set.csv')

    def popup_html(row,df):
        report_date=df['report_date'].iloc[row] 
        area=df['lga_name'].iloc[row]
        left_col_color = "#3e95b5"
        right_col_color = "#f2f9ff"
    
        html = """
    <!DOCTYPE html>
    <html>
    <center><h4 style="margin-bottom:5"; width="100px">{}</h4>""".format(area) + """</center>
    <center> <table style="height: 26px; width: 250px;">
    <tbody>
    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;padding: 10px">Report Date </span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";padding-left: 30px;">"""+report_date + """</td>
    </table></center>
    </html>
    """
        return html 

    data = pd.read_csv('lga_population/lga_population_h.csv')

    def display_map():
        bins = list(data["population"].quantile([0, 0.10, 0.3, 0.90, 1]))
        fire_location = df[["latitude", "longitude"]]
        map = folium.Map(location=[-28.0, 135.0],zoom_start=4, control_scale=True)
        for row in range(0,len(df)):
            html = popup_html(row,df)
            popup = folium.Popup(folium.Html(html, script=True), max_width=500)
            folium.Marker([df['latitude'].iloc[row],df['longitude'].iloc[row]],
                    popup=popup,icon=folium.Icon(color="orange",icon = "fire")).add_to(map)
            
        choropleth = folium.Choropleth(
        geo_data='lga_population_geometry/simplified_lga_polygons.geojson',
        name='choropleth',
        data=data,
        columns=['lga_code','population'], 
        key_on='feature.properties.lga_code',
        fill_color='PuBuGn',
        nan_fill_color="White", 
        fill_opacity=0.7,
        line_opacity=0.2,
        highlight=True,
        line_color='black',
        bins = bins)

        choropleth.geojson.add_to(map)

        choropleth.geojson.add_child(folium.features.GeoJsonTooltip(
                fields=['lga_name','population'],
                style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"))) 
        
        
        st.map=st_folium(map,width=700, height =450)

    display_map()
    
    #BAR GRAPH
    st.header('Number of fires by local government area')
    df_location_count = pd.DataFrame(df['lga_name'].value_counts())
    st.bar_chart(df_location_count)

    #DATA FRAME BY LGA
    st.header('View data by region')
    
    df_location = pd.DataFrame((df['lga_name']).sort_values())
    option = st.selectbox('Please select local govenment area ', df_location.drop_duplicates())

    #remove columns we don't want to show in dataframe
    sorted_dataset= pd.DataFrame(df[['lga_name','latitude','longitude','state','report_date']].sort_values('report_date'))
    a = len((sorted_dataset.loc[sorted_dataset['lga_name'] == option]))
    st.write(f'There are {a} recorded fires in', option)

    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

# Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.table(sorted_dataset.loc[sorted_dataset['lga_name'] == option])