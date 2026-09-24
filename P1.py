import pandas as pd

archivo = pd.read_excel('C:/Users/usuario/Documents/Python - Estadistica/encuesta_clean_202102.xlsx')

df = pd.DataFrame(archivo)


df = df[["salario_mensual_o_retiro_neto_en_tu_moneda_local","trabajo_de","anos_de_experiencia","la_recomendas_como_un_buen_lugar_para_trabajar",
    "estado","carrera"]]

df = df.rename(columns = {"salario_mensual_o_retiro_neto_en_tu_moneda_local": "salario mensual neto", "trabajo_de": "puesto",
                          "la_recomendas_como_un_buen_lugar_para_trabajar": "percepcion condiciones de trabajo","estado": "estado academico"})

salarios = df["salario mensual neto"]

media = salarios.mean()
print(media)
print(f"maximo: {salarios.max()}")
print(f"minimi: {salarios.min()}")