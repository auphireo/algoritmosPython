import pandas as pd
import folium
import webbrowser
colegios_db = pd.read_excel('../add/colegios-medellin.xlsx')

df_colegiosMedellin = pd.DataFrame()
df_colegiosMedellin['Nombre_sede'] = colegios_db['NOMBRE SEDE']
df_colegiosMedellin['Direccion_sede]'] = colegios_db['DIRECCION SEDE']
df_colegiosMedellin['Lat'] = colegios_db['LATITUD']
df_colegiosMedellin['Log'] = colegios_db['LONGITUD']

print('x -'*30)
print(df_colegiosMedellin.info())
print(df_colegiosMedellin.head())

#subset_of_df = df_colegiosMedellin.sample(n=100)

some_map = folium.Map(location=(df_colegiosMedellin['Lat'].mean(),df_colegiosMedellin['Log'].mean()),zoom_start=10)

for row in df_colegiosMedellin.itertuples():
    some_map.add_child(folium.Marker(location=[row.Lat,row.Log],popup=row.Nombre_sede))

# # Descomentar las siguientes lineas para guardar y ver el mapa en el navegador
# some_map.save("add/map.html")
# webbrowser.open("map.html")