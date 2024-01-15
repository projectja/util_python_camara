import pandas as pd

filepath = r"c://desarrollo//recorrer-dataframe//excel-roto.xlsx"

df = pd.read_excel(filepath, sheet_name='Actividades individuales_R',  usecols = 'A:f',header = 0)
df_original = pd.read_excel(filepath, sheet_name='Actividades individuales_R',  usecols = 'A:f',header = 0)
df2 = pd.read_excel(filepath, sheet_name='Actividades individuales',  usecols = 'A:f',header = 0)
df.to_excel('output.xlsx', index=False)



#for index1, row in df.iterrows():    
#     dni = df.iloc[[index1]]
#     # print(dni) 
#     # df_ = pd.DataFrame(index1, columns=['DNI empresa'])
#     #df_empresa_buscada = data_oap_tab_LISTA_ASESORE_GENERACION_DOCUME.loc[data_oap_tab_LISTA_ASESORE_GENERACION_DOCUME['documento_soclitiante'] == cif]      
#     #df_ = df.loc[df['DNI empresa'] == dni]      
#     # df.iloc('DNI Empresa')    
#     print( dni)
#     a = input("Pulse una tecla....")
# print(dni.index)

# === recorrer actividades individuales sin usuario

#for nombreusuario, dniempresa in zip(df['Nombre usuario'], df['DNI empresa']):
for nombreusuario, dniusuario in zip(df['Nombre usuario'], df['DNI usuario']):
    if nombreusuario == "no encontrado":    
        dniarestaurar = dniusuario
        df2_result = df2.loc[df2['DNI usuario'] == dniarestaurar, ['Nombre usuario']]
        print('usuario %s' % dniarestaurar) # elimnar CUANDNO OK
        print(" DF2 result  es la siguiente informacion " )  # elimnar CUANDNO OK
        print(df2_result)  # elimnar CUANDNO OK
        # setting value in dataframe with loc
        print ("resutlado a evaluar ")   # elimnar CUANDNO OK
        print (df2_result['Nombre usuario'])  # elimnar CUANDNO OK
        df.loc[df['DNI usuario'] == dniarestaurar, "Nombre usuario"] = df2_result['Nombre usuario']
        # localizamos el usuario a restaurar
        print(" imprimimos el resultado de la actualizacion corregida del DF")  # elimnar CUANDNO OK
        print(df)    # elimnar CUANDNO OK
        print ("original DF")  # elimnar CUANDNO OK
        print(df_original) # elimnar CUANDNO OK
for nombree







                                     



    


