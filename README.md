# HydroDataViewer

O HydroDataViewer é um aplicativo baseado em Django que consome a API da Agência Nacional de Águas (ANA) para exibir informações hidrometeorológicas de uma determinada estação. Com esta ferramenta, os usuários podem visualizar de forma fácil e intuitiva dados como níveis de água, precipitação, temperatura e outros parâmetros relevantes.

## Recursos

- **Salvar arquivos em XML, CSV e XLSX:** 

- **Integração da API da ANA:** O HydroDataViewer utiliza a biblioteca Requests do Python para realizar solicitações HTTP à API da ANA, buscando os dados hidrometeorológicos atualizados da estação escolhida.
- **Modelos do Django:** O projeto possui modelos Django que representam as informações da estação, incluindo código, nome e localização. Além disso, os dados hidrometeorológicos detalhados, como datas, níveis de água, precipitação, entre outros, são armazenados no banco de dados.
- **Visualização de dados:** O HydroDataViewer apresenta os dados hidrometeorológicos de forma clara e intuitiva por meio de gráficos, tabelas e outros elementos visuais, permitindo aos usuários compreender as informações de maneira fácil e rápida.
- **Pesquisa e filtro:** O aplicativo oferece recursos de pesquisa e filtro, permitindo aos usuários encontrar e visualizar dados específicos, como intervalos de datas ou parâmetros específicos de interesse.
- **Atualizações automáticas:** O HydroDataViewer possui um mecanismo de atualização periódica dos dados, permitindo que as informações da estação sejam atualizadas automaticamente em intervalos regulares, garantindo dados sempre atualizados para os usuários.
- **Interface amigável:** O aplicativo oferece uma interface de usuário moderna e responsiva, com uma experiência intuitiva de navegação e interação, garantindo uma ótima usabilidade em diferentes dispositivos.

## Como usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/hydrodataviewer.git

2. Instale as dependências do projeto:

   cd hydrodataviewer
   pip install -r requirements.txt