# Utilidad para reparar el excel registro actividades
# Al separar por años en red.es el registro de actividades
# Algunos registros de ALTA DE USUARIO y ACTIVIDADES (PESTAÑAS) quedan "no encontrado"
# Esto ocurre porque se ha borrado las empresas anteriores al año activo que funcionaban como claves
# en las siguientes pestañas
# Lo que hace la utilidad es a partir del CIF recuperar las empresas (Denominación y demás datos)
# 12-01-2024

import pandas as pd
#cambio

filepath_roto = r"c://desarrollo//recorrer-dataframe//excel-roto-oficial.xlsx"
filepath_completo = r"c://desarrollo//recorrer-dataframe//excel-completo-oficial.xlsx"


df_ai_roto = pd.read_excel(filepath_roto, sheet_name='Actividades individuales',  usecols = 'c:T',header = 3)
df_ae_roto = pd.read_excel(filepath_roto, sheet_name='Alta_Empresa',  usecols = 'B:L',header = 3)
df_au_roto = pd.read_excel(filepath_roto, sheet_name='Alta_Usuario',  usecols = 'E:N',header = 3)


df2_ai_completo = pd.read_excel(filepath_completo, sheet_name='Actividades individuales',  usecols = 'c:T',header = 3)
df2_ae_completo = pd.read_excel(filepath_completo, sheet_name='Alta_Empresa',  usecols = 'B:L',header = 3)
df2_au_completo = pd.read_excel(filepath_roto, sheet_name='Alta_Usuario',  usecols = 'E:N',header = 3)

df_ai_roto['NIF Empresa'].str.upper()
df_au_roto['NIF Empresa'].str.upper()
df2_ae_completo['NIF Empresa'].str.upper()



# salida = df_ai_roto.copy()
# with pd.ExcelWriter('excel_roto_fuente.xlsx') as writer:    
#         df_ai_roto(writer, sheet_name='Actividades individuales')
#         df_ae_roto(writer, sheet_name='Alta_empresa')

# salida.to_excel('excel_roto_fuente.xlsx',df_ae_roto, sheet_name='Alta_Empresa',index=True,header=True )


for estadonif, nifempresa in zip(df_ai_roto['Estado NIF'], df_ai_roto['NIF Empresa']):
    if estadonif == "No encontrado":   
        # nif problematico sobre el que hay que corregir el esado no encontrado 
        dniarestaurar = nifempresa
        # Convierte a mayusculas todos los cif
        dniarestaurar =  dniarestaurar.upper()
        # recuperamos la fila de la HOja de registro completa -la que no está manipulada por red.es- original con todos los registros
        df2_result = df2_ae_completo.loc[df2_ae_completo['NIF Empresa'] == dniarestaurar, ['Nombre o razón social', 'Empleados empresa', 'Incio de la actividad','Sector','NIF Empresa','Fecha (DD/MM/AA)','CCAA','Provincia','Localidad','CP','Tipo DOC' ]] 
        # convertimos a mayuscular esa fila recuperada para evitar en el cruce de dni , que las letras sean diferentes  
        df2_result['NIF Empresa'] = df2_result['NIF Empresa'].str.upper()
        untecla = input ( " .. CONVERTIDO .Pusle una tecla...")
        
        #borrar print('usuario %s' % dniarestaurar) # elimnar CUANDNO OK
        #borrar print(" DF2 result  es la siguiente informacion " )  # elimnar CUANDNO OK
        
        #borrar print(df2_result['NIF Empresa'])   # elimnar CUANDNO OK
        # setting value in dataframe with loc
        # print ("resutlado a evaluar ")   # elimnar CUANDNO OK
        # print (df2_result['Nombre o razón social'])  # elimnar CUANDNO OK
        # df_ai_roto.loc[df_ai_roto['DNI usuario'] == dniarestaurar, "Nombre usuario"] = df2_result['Nombre usuario']
        # localizamos el usuario a restaurar
        # print(" imprimimos el resultado de la actualizacion corregida del DF")  # elimnar CUANDNO OK
        #print(df_ai_roto)    # elimnar CUANDNO OK
        
        # print( df_ae_roto.loc[len(df_ae_roto.index - 1)])
        # df_ae_roto = pd.concat([df_ae_roto, pd.DataFrame([df2_result])], ignore_index=False);
        print ( "nif de empresa ")
        print (  dniarestaurar)
        B = input ( " Pulse una tecla " )
        # Aqui debemoss comprobar que el registro en estado no encontrado que corresponde con un cif no se haya tratado antes,
        # esto seria porque el usuario haya venido dos veces, en dicho caso, ya habriamos recuperado y reparado anteriormente
        # - si ya existe en el dataframe - 
        df2_exist = df_ae_roto.loc[df_ae_roto['NIF Empresa'] == dniarestaurar, ['Nombre o razón social', 'Empleados empresa', 'Incio de la actividad','Sector','NIF Empresa','Fecha (DD/MM/AA)','CCAA','Provincia','Localidad','CP','Tipo DOC' ]] 
        # si no está vacio es que existe no hacemos nada, o sea, ya habriamos tratado esta empresa huerfana
        if not df2_exist.empty:
            print("El CIF a restaurar EXISTE  - DNI %s " % dniarestaurar)
            a = input ( " El valor existe pulse una tecla para continuar")
        # si no existia, lo incorporamos a la lista de registros tratamos y esa empresa la mantenemos con fecha 01/01/2023
        else:
            print("El CIF a restaurar NO EXISTE  - DNI %s " % dniarestaurar)
            df_ae_roto = df_ae_roto._append(df2_result, ignore_index=True)
            df_ae_roto['Fecha (DD/MM/AA)'] = '01/01/2023'
            df_ae_roto['NIF Empresa'].str.upper()
        
        # print( df_ae_roto)
        # df_ae_roto = df_ae_roto.append(df2_result, ignore_index=True)
        print(df_ae_roto)

# aqui lo que hacemos primero escribir el dataframe de actividades individuales
# al momento de realizar esto no vemos necesario grabarlo, ya que solo corriengo las empresas 
# e incorporarlo al registro oficial, se corregirían las empresas en todas las pestañas.
# vemos tambien que es posible que se hayan eliminado altas de usuarios que vienieran
# por primera vez en 2022 pero realmente vemos que no tiene impacto en la de actividades individuales
# porque en esa pestaña el campo cable está siendo el nif de empresa.
                       
df_ai_roto.to_excel('excel_roto_fuente.xlsx', sheet_name='Actividades individuales',index=True,header=True)
with pd.ExcelWriter('excel_roto_fuente.xlsx',mode='a') as writer:
     df_ae_roto.to_excel(writer, sheet_name="Alta_empresa")

