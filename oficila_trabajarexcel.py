import pandas as pd

filepath_roto = r"c://desarrollo//recorrer-dataframe//excel-roto-oficial.xlsx"
filepath_completo = r"c://desarrollo//recorrer-dataframe//excel-completo-oficial.xlsx"

df_ai_roto = pd.read_excel(filepath_roto, sheet_name='Actividades individuales',  usecols = 'c:T',header = 3)
df_ae_roto = pd.read_excel(filepath_roto, sheet_name='Alta_Empresa',  usecols = 'B:L',header = 3)

df2_ai_completo = pd.read_excel(filepath_completo, sheet_name='Actividades individuales',  usecols = 'c:T',header = 3)
df2_ae_completo = pd.read_excel(filepath_completo, sheet_name='Alta_Empresa',  usecols = 'B:L',header = 3)

# df_ai_roto.to_excel('output.xlsx', index=False)



#for index1, row in df_ai_roto.iterrows():    
#     dni = df_ai_roto.iloc[[index1]]cls

#     # print(dni) 
#     # df_ = pd.DataFrame(index1, columns=['DNI empresa'])
#     #df_empresa_buscada = data_oap_tab_LISTA_ASESORE_GENERACION_DOCUME.loc[data_oap_tab_LISTA_ASESORE_GENERACION_DOCUME['documento_soclitiante'] == cif]      
#     #df_ = df_ai_roto.loc[df_ai_roto['DNI empresa'] == dni]      
#     # df_ai_roto.iloc('DNI Empresa')    
#     print( dni)
#     a = input("Pulse una tecla....")
# print(dni.index)

# === recorrer actividades individuales sin usuario

#for estadonif, dniempresa in zip(df_ai_roto['Nombre usuario'], df_ai_roto['DNI empresa']):
for estadonif, nifempresa in zip(df_ai_roto['Estado NIF'], df_ai_roto['NIF Empresa']):
    if estadonif == "no encontrado":    
        dniarestaurar = nifempresa
        df2_result = df2_ae_completo.loc[df2_ae_completo['NIF Empresa'] == dniarestaurar, ['Nombre o razón social']]
        print('usuario %s' % dniarestaurar) # elimnar CUANDNO OK
        print(" DF2 result  es la siguiente informacion " )  # elimnar CUANDNO OK
        print(df2_result)  # elimnar CUANDNO OK
        # setting value in dataframe with loc
        print ("resutlado a evaluar ")   # elimnar CUANDNO OK
        print (df2_result['Nombre o razón social'])  # elimnar CUANDNO OK
        # df_ai_roto.loc[df_ai_roto['DNI usuario'] == dniarestaurar, "Nombre usuario"] = df2_result['Nombre usuario']
        # localizamos el usuario a restaurar
        print(" imprimimos el resultado de la actualizacion corregida del DF")  # elimnar CUANDNO OK
        print(df_ai_roto)    # elimnar CUANDNO OK
        print ("original DF")  # elimnar CUANDNO OK
        







                                     



    



