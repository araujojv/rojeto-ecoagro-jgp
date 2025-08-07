import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

def limpar_valor(valor_str):
    """Remove R$, pontos e converte vírgula para ponto."""
    valor_str = re.sub(r'[R$\.\s\xa0]', '', valor_str)
    valor_str = valor_str.replace(',', '.')
    try:
        return float(valor_str)
    except ValueError:
        return None

def extrair_dados_pagina(soup):
    dados = []
    linhas = soup.select('table tbody tr')
    for linha in linhas:
        colunas = linha.find_all('td')
        if len(colunas) >= 6:
            ano = colunas[0].text.strip()
            empresa = colunas[1].text.strip()
            numero_emissao = colunas[2].text.strip()
            serie = colunas[3].text.strip()
            isins = colunas[4].text.strip().split()
            valor = limpar_valor(colunas[5].text.strip())

            # Junta os ISINs em uma única string separada por vírgula
            codigo_isin = ', '.join(isins)

            # Adiciona uma linha única por emissão
            dados.append([ano, empresa, numero_emissao, serie, codigo_isin, valor])
    return dados

def main():
    base_url = "https://ecoagro.agr.br/emissoes?page="
    todas_emissoes = []
    pagina = 1

    while True:
        url = f"{base_url}{pagina}"
        print(f"🔎 Coletando dados da página {pagina}...")
        resp = requests.get(url)

        if resp.status_code != 200:
            print(f"❌ Erro ao acessar a página {pagina}")
            break

        soup = BeautifulSoup(resp.content, 'html.parser')
        dados = extrair_dados_pagina(soup)

        if not dados:
            print("✅ Fim das páginas detectado.")
            break

        todas_emissoes.extend(dados)
        pagina += 1
        time.sleep(1)  # Respeitar o servidor

    # Ajuste dos nomes das colunas finais
    df = pd.DataFrame(todas_emissoes, columns=[
        "Ano", "Empresa (Operação)", "NumeroEmissao", "Serie", "Cod ISIN", "Valor"
    ])
    df.to_csv("emissoes.csv", index=False, encoding='utf-8-sig')
    print("📁 Arquivo 'emissoes.csv' salvo com sucesso!")

if __name__ == "__main__":
    main()
