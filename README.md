
# 🌱 Projeto Ecoagro CRA - JGP

Este projeto tem como objetivo realizar a coleta, análise e visualização de dados relacionados às emissões de CRA (Certificados de Recebíveis do Agronegócio) divulgadas pela Ecoagro. A proposta engloba:

- 🕸️ Scraping dos dados diretamente do site da Ecoagro
- 📊 Análise exploratória (EDA) em notebook Jupyter
- 🌐 Dashboard interativo com Streamlit

---

## 📁 Estrutura do Projeto

```
ecoagro-cra-projeto/
│
├── scraping/                 # Scripts e dados coletados
│   ├── scraper.py           # Script de scraping
│   └── emissoes.csv         # Dados coletados via scraping
│
├── analysis/
│   └── analysis.ipynb       # Análise exploratória em notebook
│
├── web/
│   └── app.py               # Interface em Streamlit
│
├── .env                     # Variáveis de ambiente (como caminho do CSV)
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo
```

---

## 🔽 1. Coleta dos Dados (Scraping)

Para coletar os dados diretamente da [Ecoagro](https://www.ecoagro.agr.br/), utilize o script `scraper.py`:

```bash
cd scraping
python scraper.py
```

> 💾 O arquivo `emissoes.csv` será gerado automaticamente na pasta `scraping/`.

---

## 📊 2. Análise Exploratória (Notebook)

O notebook `analysis.ipynb` contém as análises feitas com Pandas, Seaborn e Plotly.

Principais análises realizadas:
- Evolução das emissões de CRA por ano
- Empresas com maior volume de emissões
- Distribuição de valores por setor e tipo

Para abrir o notebook:

```bash
jupyter notebook analysis/analysis.ipynb
```

---

## 🌐 3. Dashboard com Streamlit

A aplicação interativa foi desenvolvida com **Streamlit** e está localizada em `web/app.py`.

### ▶️ Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Crie o arquivo `.env` na raiz do projeto:

```
DATA_PATH=./scraping/emissoes.csv
```

3. Rode o app:

```bash
cd web
streamlit run app.py
```

O dashboard será iniciado em `http://localhost:8501`.

---

## 📦 Requisitos

- Python 3.8+
- Pandas
- Plotly
- Streamlit
- Python-dotenv
- Jupyter Notebook (para as análises)

---


## 📫 Contato

Desenvolvido por **João Araújo**  
📧 joaoaraujo.vitor@hotmail.com  
telefone : 21966686775