"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df=df.copy()                                       #Copiar el dataframe para no modificar el original

    df.dropna(inplace=True)                            #Eliminar líneas con datos faltantes
    
    df = df.apply(lambda x: x.str.lower().replace({'-': ' ', '_': ' '}, regex=True) if x.dtype == "object" else x)     #Convertir a minúsculas y reemplazar guiones y guiones bajos por espacios
    df = df.apply(lambda x: x.replace('[!\"#$%&\'()*+,:;<=>?¿@[\\]^`{|}~]', '', regex=True) if x.dtype == "object" else x)      #Remover caracteres especiales

    
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)         #Convertir a float
    df['estrato'] = df['estrato'].astype(int)                               #Convertir a int
    df['comuna_ciudadano'] = df['comuna_ciudadano'].replace(r'\.0$', '', regex=True).astype(int)    #Convertir a int
    df.fecha_de_beneficio=pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format='mixed')   #Convertir a datetime
    
    df.drop_duplicates(inplace=True)       #Eliminar líneas duplicadas después de la limpieza 

    
    return df

#print(clean_data())
#print(clean_data().sexo.value_counts().to_list())
#print(pregunta.clean_data().tipo_de_emprendimiento.value_counts().to_list())
#print(pregunta.clean_data().idea_negocio.value_counts().to_list())
#print(pregunta.clean_data().barrio.value_counts().to_list())
#print(pregunta.clean_data().estrato.value_counts().to_list())
#print(pregunta.clean_data().comuna_ciudadano.value_counts().to_list())
#print(pregunta.clean_data().fecha_de_beneficio.value_counts().to_list())
#print(pregunta.clean_data().monto_del_credito.value_counts().to_list())
#print(pregunta.clean_data().línea_credito.value_counts().to_list())





