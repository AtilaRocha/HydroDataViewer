from src.function import processar_estacoes, definir_datas, deletar_arquivos_gerados
import os

# Datas para processar
datas = definir_datas()

# Codigos das Estações
estacoes = ['946005', '23310000', '23466000', '23490000', '23790000', '33250000', '33260000', '33273000', '33281000', '33286000', '33290000', '33321000', '33380000', '33420000', '33480000', '33530000', '33550000', '33590000', '33630000', '33661000', '33680000', '33690100', '33730000', '33760000', '33770000', '34010000', '34020000', '34020980', '34040500', '34129980', '34130000', '34160900', '34170000', '34311000', '34820000']

# Iterar sobre as datas
for data in datas:
    processar_estacoes(data, estacoes)

# Perguntar ao usuário se deseja deletar os arquivos gerados
resposta = input("Deseja deletar os arquivos gerados? (S/N): ")
if resposta.upper() == 'S':
    deletar_arquivos_gerados()