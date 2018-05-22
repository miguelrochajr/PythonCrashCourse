import pandas as pd
import numpy as np

veltron = pd.read_excel('Dados_Velotron1.xlsx')

km = 0  # km a ser analisado
index = 0  # index do valor

for value in veltron['miles']:
    if value*1.61 < 2*(km+1):
        veltron.set_value(index, 'miles', km)
    else:
        km = km + 2
        veltron.set_value(index, 'miles', km)
    index = index + 1


group_v = veltron.groupby('miles')
tabela_final = group_v.mean()
tabela_aux = tabela_final.reset_index()

index = 0
for valor in tabela_aux['speed']:
    tabela_aux.set_value(index, 'speed', valor*1.61)
#     tabela_aux.set_value(index, 'speed', valor)
#     print(valor*1.61)
    index = index + 1

actual_mileage = 0
index = 0
for value in veltron['miles']:
    if value != actual_mileage:
        actual_mileage = value
        index_final_table = int(value/2)
        value_min = (veltron['ms '][index])/60000
        tabela_aux.set_value(index_final_table, 'ms ', value_min)
    index = index + 1

writer = pd.ExcelWriter('final.xlsx')
tabela_aux.to_excel(writer, 'Result')
writer.save()
