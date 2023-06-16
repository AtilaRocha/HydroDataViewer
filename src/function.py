import requests
import xml.etree.ElementTree as ET
import os
import pandas as pd
import xml.etree.ElementTree as ET
import json
import xmltodict


def convertXMLtoCSV(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathCSV):
    try:
        # Construindo o nome do arquivo de saída
        filename = f"Estacao_{codigoEstacao}_de_{dataInicio.replace('/', '_')}_a_{dataFim.replace('/', '_')}.csv"
        output_path = os.path.join(pathCSV, filename)

        # Lendo o arquivo XML e convertendo para JSON
        with open(os.path.join(pathXML, xml_file), 'r') as xml:
            data_dict = xmltodict.parse(xml.read())
        
        # Convertendo para formato tabular com pd.json_normalize
        data = pd.json_normalize(data_dict['DataTable']['diffgr:diffgram']['DocumentElement']['DadosHidrometereologicos'])

        # Salvando como CSV
        data.to_csv(output_path, index=False)
        print(f"Arquivo CSV salvo em: {output_path}")
    except Exception as e:
        print("Ocorreu um erro durante a conversão para CSV:", str(e))


def convertXMLtoXLSX(pathXML, xml_file, codigoEstacao, dataInicio, dataFim, pathXLSX):
    try:
        # Construindo o nome do arquivo de saída
        filename = f"Estacao_{codigoEstacao}_de_{dataInicio.replace('/', '_')}_a_{dataFim.replace('/', '_')}.xlsx"
        output_path = os.path.join(pathXLSX, filename)

        # Lendo o arquivo XML e convertendo para JSON
        with open(os.path.join(pathXML, xml_file), 'r') as xml:
            data_dict = xmltodict.parse(xml.read())
        
        # Convertendo para formato tabular com pd.json_normalize
        data = pd.json_normalize(data_dict['DataTable']['diffgr:diffgram']['DocumentElement']['DadosHidrometereologicos'])

        # Salvando como XLSX
        data.to_excel(output_path, index=False)
        print(f"Arquivo XLSX salvo em: {output_path}")
    except Exception as e:
        print("Ocorreu um erro durante a conversão para XLSX:", str(e))

def saveXML(codigoEstacao, dataInicio, dataFim, pathXML):
    try:
        # Faz a requisição HTTP
        
        filename = f"Estacao_{codigoEstacao}_de_{dataInicio.replace('/', '_')}_a_{dataFim.replace('/', '_')}.xml"
        url = f"https://telemetriaws1.ana.gov.br/ServiceANA.asmx/DadosHidrometeorologicos?codEstacao={codigoEstacao}&dataInicio={dataInicio}&dataFim={dataFim}"
        response = requests.get(url)
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Obtém o conteúdo da resposta em formato XML
            xml_content = response.content

            # Define o caminho completo do arquivo
            file_path = os.path.join(pathXML, filename)

            # Salva o conteúdo em um arquivo XML
            with open(file_path, "wb") as file:
                file.write(xml_content)

            # Carrega o conteúdo do arquivo XML em um objeto ElementTree
            xml_tree = ET.fromstring(xml_content)

            # Retorna o nome do arquivo XML salvo
            return filename

        else:
            print("A requisição falhou com o status:", response.status_code)
    except Exception as e:
        print("Ocorreu um erro durante a requisição:", str(e))

