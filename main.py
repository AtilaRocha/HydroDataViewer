
from src.function import saveXML
from src.function import convertXMLtoCSV
from src.function import convertXMLtoXLSX
import os

# Define o caminho onde o arquivo será salvo
pathXML = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/xml'
pathCSV = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/csv'
pathXLSX = 'G:/Atila_Rocha/Programacao/HydroDataViewer/db/xlsx'

# Pedindo cod da estação e datas inicio/fim

# dataInicio = str(input("Digite a data inicial (ex.: 06/06/2023): "))
# dataFim = str(input("Digite a data final (ex.: 06/06/2023): "))
# codigoEstacao = str(input("Digite o código da Estação (ex.: 33281000): "))
dataInicio = '15/06/2023'
dataFim = '15/06/2023'
codigoEstacao = '33281000'


# Salva o arquivo XML e obtém o conteúdo XML como uma string
xml_file = saveXML(codigoEstacao, dataInicio, dataFim, pathXML)

convert = input("Deseja converter o XML para CSV/XLSX? (y/n): ")

if convert.lower() == 'y':
    try:
        convertXMLtoCSV(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathCSV)
        convertXMLtoXLSX(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathXLSX)
    except Exception as e:
        print("Ocorreu um erro durante a conversão:", str(e))