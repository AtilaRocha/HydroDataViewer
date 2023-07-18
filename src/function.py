import requests, xml.etree.ElementTree as ET, os, json, xmltodict, openpyxl, pandas as pd, sqlite3, csv, datetime

def verificar_pasta(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)
def criar_arquivo_RDE(pathCSV, pathXLSX, pathdata):
    # Dicionário para armazenar os maiores e menores valores por estação
    RDE = {}
    # Percorrer todos os arquivos na pasta de dados
    for arquivo in os.listdir(pathCSV):
        if arquivo.endswith(".csv") or arquivo.endswith(".xlsx"):
            caminho_arquivo = os.path.join(pathCSV, arquivo)
            # Verificar se o arquivo é CSV ou XLSX e ler os dados
            if arquivo.endswith(".csv"):
                dados = pd.read_csv(caminho_arquivo)
            elif arquivo.endswith(".xlsx"):
                dados = pd.read_excel(caminho_arquivo)
            # Obter o código da estação a partir do nome do arquivo
            codigoEstacao = arquivo.split("_")[1]
            # Verificar se a estação já está presente no dicionário
            if codigoEstacao not in RDE:
                RDE[codigoEstacao] = {}
            # Atualizar os maiores e menores valores para cada coluna
            if "Nivel" in dados.columns:
                maior_valor_nivel = dados["Nivel"].max()
                menor_valor_nivel = dados["Nivel"].min()
                RDE[codigoEstacao]["Maior Valor Nivel"] = maior_valor_nivel
                RDE[codigoEstacao]["Menor Valor Nivel"] = menor_valor_nivel
            if "Chuva" in dados.columns:
                maior_valor_chuva = dados["Chuva"].max()
                menor_valor_chuva = dados["Chuva"].min()
                RDE[codigoEstacao]["Maior Valor Chuva"] = maior_valor_chuva
                RDE[codigoEstacao]["Menor Valor Chuva"] = menor_valor_chuva
            if "Vazao" in dados.columns:
                maior_valor_vazao = dados["Vazao"].max()
                menor_valor_vazao = dados["Vazao"].min()
                RDE[codigoEstacao]["Maior Valor Vazao"] = maior_valor_vazao
                RDE[codigoEstacao]["Menor Valor Vazao"] = menor_valor_vazao
    # Converter o dicionário para DataFrame
    df_RDE = pd.DataFrame.from_dict(RDE, orient="index")
    # Criar o caminho completo para o arquivo de saída em CSV
    nome_arquivo_saida_csv = os.path.join(pathCSV, f"RDE_{os.path.basename(pathdata)}.csv")
    # Salvar o DataFrame como arquivo CSV
    df_RDE.to_csv(nome_arquivo_saida_csv)
    # Criar o caminho completo para o arquivo de saída em XLSX
    nome_arquivo_saida_xlsx = os.path.join(pathXLSX, f"RDE_{os.path.basename(pathdata)}.xlsx")
    # Salvar o DataFrame como arquivo XLSX
    df_RDE.to_excel(nome_arquivo_saida_xlsx, sheet_name="RDE", index_label="Estacao")
    # Abrir o arquivo XLSX e ajustar a largura das colunas
    workbook = openpyxl.load_workbook(nome_arquivo_saida_xlsx)
    worksheet = workbook["RDE"]
    for column in worksheet.columns:
        max_length = 0
        column = column[0].column_letter  # Obter a letra da coluna
        for cell in worksheet[column]:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        worksheet.column_dimensions[column].width = adjusted_width

    # Salvar as alterações no arquivo XLSX
    workbook.save(nome_arquivo_saida_xlsx)
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
        return filename  # Retorna o nome do arquivo CSV gerado
    except Exception as e:
        print("Ocorreu um erro durante a conversão para CSV:", str(e))
        return None  # Retorna None em caso de erro
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
def importar_dados_csv_para_sqlite(csvFile, pathDB):
    # Combinar o caminho completo do banco de dados SQLite
    caminho_arquivo_banco_dados = os.path.join(pathDB, 'dadosBrutosANA.db')
    # Conexão com o banco de dados SQLite
    conexao = sqlite3.connect(caminho_arquivo_banco_dados)
    # Criação do cursor
    cursor = conexao.cursor()
    # Leitura e inserção dos dados do arquivo CSV
    with open(csvFile, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=',')
        next(leitor_csv)  # Pula o cabeçalho do arquivo CSV
        for linha in leitor_csv:
            cod_estacao = linha[2]
            data_hora = linha[3]
            vazao = float(linha[4]) if linha[4] != '' else None
            nivel = float(linha[5]) if linha[5] != '' else None
            chuva = float(linha[6]) if linha[6] != '' else None
            cursor.execute('''INSERT INTO Estacoes (CodEstacao, DataHora, Vazao, Nivel, Chuva)
                              VALUES (?, ?, ?, ?, ?)''',
                           (cod_estacao, data_hora, vazao, nivel, chuva))
    # Commit das alterações e fechamento da conexão
    conexao.commit()
    conexao.close()
def processar_estacoes(data, estacoes):
    # Obter o diretório atual do projeto
    diretorio_projeto = os.getcwd()

    # Criar o caminho completo para as pastas
    pathdata = f"{data.replace('/', '_')}_a_{data.replace('/', '_')}"
    pathCSV = os.path.join(diretorio_projeto, 'DB', pathdata, 'csv')
    pathXLSX = os.path.join(diretorio_projeto, 'DB', pathdata, 'xlsx')
    pathXML = os.path.join(diretorio_projeto, 'DB', pathdata, 'xml')
    pathDB = os.path.join(diretorio_projeto, 'DB')

    # Verificar e criar as pastas, se necessário
    verificar_pasta(pathCSV)
    verificar_pasta(pathXLSX)
    verificar_pasta(pathXML)
    verificar_pasta(pathDB)

    # Iterar sobre as estações
    for codigoEstacao in estacoes:
        # Salvar o arquivo XML e obter o conteúdo XML como uma string
        xml_file = saveXML(codigoEstacao, data, data, pathXML)

        try:
            csvFile = convertXMLtoCSV(pathXML, xml_file, codigoEstacao, data, data, pathCSV)
            convertXMLtoXLSX(pathXML, xml_file, codigoEstacao, data, data, pathXLSX)

            if csvFile is not None:
                # Criar o caminho completo para o arquivo CSV
                csvFilePath = os.path.join(pathCSV, csvFile)
                # Importar os dados do arquivo CSV para o banco de dados SQLite
                importar_dados_csv_para_sqlite(csvFilePath, pathDB)
                print(f"Dados importados com sucesso para o banco de dados: {csvFilePath}")
            else:
                print(f"Não foi possível gerar o arquivo CSV para a estação {codigoEstacao}")

        except Exception as e:
            print(f"Ocorreu um erro durante a conversão da estação {codigoEstacao}:", str(e))
    criar_arquivo_RDE(pathCSV, pathXLSX, pathdata)

def definir_datas():
    # Pedir a data inicial ao usuário
    data_inicial_str = input("Digite a data inicial (no formato DD/MM/AAAA): ")
    data_inicial = datetime.datetime.strptime(data_inicial_str, "%d/%m/%Y")

    # Pedir a data final ao usuário
    data_final_str = input("Digite a data final (no formato DD/MM/AAAA): ")
    data_final = datetime.datetime.strptime(data_final_str, "%d/%m/%Y")

    # Lista para armazenar as datas
    datas = []

    # Iterar sobre as datas e adicionar à lista
    data_atual = data_inicial
    while data_atual <= data_final:
        datas.append(data_atual.strftime('%d/%m/%Y'))
        data_atual += datetime.timedelta(days=1)

    return datas    
    
