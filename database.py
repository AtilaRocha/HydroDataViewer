import os, sqlite3
from src.function import verificar_pasta

def criar_tabela_estacoes(conexao):
    cursor = conexao.cursor()

    # Criação da tabela Estacoes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Estacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CodEstacoes TEXT,
            DataHora TEXT,
            Vazao REAL,
            Nivel REAL,
            Chuva REAL
        )
    ''')

def criar_tabela_rde(conexao):
    cursor = conexao.cursor()

    # Criação da tabela RDE
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RDE (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CodE TEXT,
            DataHora TEXT,
            MxChuva REAL,
            MnChuva REAL,
            MxNivel REAL,
            MnNivel REAL,
            MxVazao REAL,
            MnVazao REAL,
            FOREIGN KEY (CodE, DataHora) REFERENCES Estacoes (CodE, DataHora)
        )
    ''')

def criar_conexao_banco_dados():
    # Obter o diretório atual do projeto
    diretorio_projeto = os.getcwd()

    # Criar o caminho completo para a pasta "DB"
    pathDB = os.path.join(diretorio_projeto, 'DB')

    # Verificar e criar a pasta "DB", se necessário
    verificar_pasta(pathDB)

    # Definir o caminho completo para o arquivo do banco de dados
    caminho_arquivo_banco_dados = os.path.join(pathDB, 'dadosBrutosANA.db')

    # Conectar ao banco de dados SQLite
    conexao = sqlite3.connect(caminho_arquivo_banco_dados)

    return conexao

# Criação do banco de dados e das tabelas
conexao = criar_conexao_banco_dados()

criar_tabela_estacoes(conexao)
criar_tabela_rde(conexao)

conexao.close()
