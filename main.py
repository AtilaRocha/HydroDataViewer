from src.function import saveXML, convertXMLtoCSV, convertXMLtoXLSX, verificar_pasta, criar_arquivo_RDE
import os

# Pedindo cod da estação e datas inicio/fim
# dataInicio = str(input("Digite a data inicial (ex.: 06/06/2023): "))
# dataFim = str(input("Digite a data final (ex.: 06/06/2023): "))
# codigoEstacao = str(input("Digite o código da Estação (ex.: 33281000): "))
dataInicio = '14/07/2023'
dataFim = '14/07/2023'

# Obter o diretório atual do projeto
diretorio_projeto = os.getcwd()

# Criar o caminho completo para as pastas
pathdata = f"{dataInicio.replace('/', '_')}_a_{dataFim.replace('/', '_')}"
pathCSV = os.path.join(diretorio_projeto, 'DB', pathdata, 'csv')
pathXLSX = os.path.join(diretorio_projeto, 'DB', pathdata, 'xlsx')
pathXML = os.path.join(diretorio_projeto, 'DB', pathdata, 'xml')

# Verificar e criar as pastas, se necessário
verificar_pasta(pathCSV)
verificar_pasta(pathXLSX)
verificar_pasta(pathXML)

# Dados das estações
estacoes = ['946005', '23310000', '23466000', '23490000', '23790000', '33250000', '33260000', '33273000', '33281000', '33286000', '33290000', '33321000', '33380000', '33420000', '33480000', '33530000', '33550000', '33590000', '33630000', '33661000', '33680000', '33690100', '33730000', '33760000', '33770000', '34010000', '34020000', '34020980', '34040500', '34129980', '34130000', '34160900', '34170000', '34311000', '34820000']


convert = input(f"Os arquivos XML de {dataInicio} até {dataFim} de todas as estações foram baixados com sucesso!\nSe deseja converter TODOS os arquivos para XSLS/CSV digite [1]\nSe deseja converter uma estação especifica digite [2]\nSe não deseja fazer nenhuma conversão digite [3]\nResposta:")
# convert = input(f"Deseja converter o XML para CSV/XLSX? Digite 'todos' para converter todos ou 'y' para converter individualmente: ")
if convert == '1':
    for codigoEstacao in estacoes:
        # Salva o arquivo XML e obtém o conteúdo XML como uma string
        xml_file = saveXML(codigoEstacao, dataInicio, dataFim, pathXML)
        try:
            convertXMLtoCSV(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathCSV)
            convertXMLtoXLSX(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathXLSX)
        except Exception as e:
            print(f"Ocorreu um erro durante a conversão da estação {codigoEstacao}:", str(e))
    criar_arquivo_RDE(pathCSV, pathXLSX, pathdata)

elif convert == '2':
    codigoEstacao = input("Digite o código da Estação (ex.: 33281000): ")
    # Salva o arquivo XML e obtém o conteúdo XML como uma string
    xml_file = saveXML(codigoEstacao, dataInicio, dataFim, pathXML)
    try:
        convertXMLtoCSV(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathCSV)
        convertXMLtoXLSX(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathXLSX)
    except Exception as e:
        print("Ocorreu um erro durante a conversão:", str(e))
elif convert == '3':
    for codigoEstacao in estacoes:
        # Salva o arquivo XML e obtém o conteúdo XML como uma string
        xml_file = saveXML(codigoEstacao, dataInicio, dataFim, pathXML)
else:
    print("Opção inválida. Por favor, digite novamente.")