import requests
from bs4 import BeautifulSoup
import os
from zipfile import ZipFile
from io import BytesIO

os.makedirs('pdfs', exist_ok=True)
zip_path = os.path.join('pdfs', 'anexos.zip')

link = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
inicio_url = "https://www.gov.br/ans/pt-br/"

# Acessar site com Headers (Para requisição)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

# Requisição para receber HTML da página
try:
    requisicao = requests.get(link, headers=headers)
except requests.exceptions.RequestException: 
    print("Não foi possível acessar o site.")

# Instanciar o BeautifulSoup          # leitor html
site = BeautifulSoup(requisicao.text, "html.parser")

# Encontrar os links dos anexos
links = site.find_all("a", class_="internal-link")

# List Comprehension para filtrar os anexos corretos (com base no texto do HTML)
filter_pdfs = [a for a in links if "Anexo I." in a.text or "Anexo II." in a.text]


# Iterar sobre os pdfs e salvá-los no zip
with ZipFile(zip_path, 'w') as zipf:  
    for anexo in filter_pdfs:
        href = anexo.get("href")
        
        # Verificar se o link é um PDF válido
        if href and href.startswith(inicio_url) and href.endswith('.pdf'):
            print(f"Baixando: {href}")
            
            response = requests.get(href)

            if response.status_code == 200:
                file_name = href.split('/')[-1]  # Nome do arquivo PDF
                
                # Criar um buffer em memória e salvar o conteúdo (evita uso do disco desnecessariamente)
                pdf_bytes = BytesIO(response.content)
                
                # Adicionar ao ZIP sem precisar salvar os pdfs no disco
                zipf.writestr(file_name, pdf_bytes.getvalue())
                
                print(f'Arquivo adicionado ao ZIP: {file_name}')
            else:
                print(f'Erro ao baixar arquivo: {href}')
                break
        else:
            print('Arquivo inválido.')