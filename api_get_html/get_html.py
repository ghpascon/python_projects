import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import matplotlib.pyplot as plt

# URL da página
url = "https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/grafico/"

# Faz a requisição GET para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Obtém o HTML da página
    html_content = response.text
    
    # Parseia o HTML usando BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Encontra o script que contém os dados JSON
    script_tag = soup.find("script", text=lambda x: "highchartsData" in str(x))
    
    # Extrai os dados JSON da variável highchartsData
    json_data = json.loads(script_tag.text.split("highchartsData = ")[1].split(";")[0])
    
    # Converte os dados JSON em um DataFrame do pandas
    df = pd.DataFrame(json_data)
    
    # Converte a coluna de data para o tipo datetime
    df['data'] = pd.to_datetime(df['data'])
    
    # Plotar o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(df['data'], df['value'])
    plt.title('Gráfico do Índice Ibovespa')
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.show()
    
    print("Gráfico plotado com sucesso.")
else:
    print("Erro ao acessar a página:", response.status_code)
