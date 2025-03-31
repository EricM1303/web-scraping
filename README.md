# ⛏️ Web Scraping e Utilização da lib Pandas
O desafio 1 apresentado foi iniciar uma "mineração de dados" no site : https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-dasociedade/atualizacao-do-rol-de-procedimentos, para acessar os PDF's I e II e fazer o download deles na máquina local e logo em seguida converter para Zip.

O desafio 2 foi transformar os dados do anexo I (que era um PDF com uma tabela). Esses dados precisavam ser salvos em formato csv e também alterar uma duas informações específicas de todas as colunas e transformar em outro nome (conforme legenda do documento).
***
## 🤖 Instalação

1. Clone o repositório do github na sua máquina local
 ~~~~git
    git clone https://github.com/EricM1303/web-scraping.git
~~~~

2. Instale as depêndencias

~~~~python
    pip install -r requirements.txt
~~~~

3. Execute o comando e abra no seu navegador na porta **localhost:3000**

~~~~python
    python <nome do arquivo python>
~~~~
## ⚙️Funcionalidades
* Minerar dados no site escolhido;
* Automatizar tarefa de download de arquivos e conversão para ZIP;
* Extrair dados de tabelas em pdf, alterar valores e transformar em .CSV;
* Utilização da biblioteca BeautifulSoap para facilitar o web scraping.

## 📂 Estrutura de Pastas

* **📦 web-scraping**
    * **extracao_pandas_csv.py**
    * **web_scraping.py**
  * **📜 README** **---> Você está aqui😉**


## 🟡 Dificuldades apresentadas
* **Conversão de dados CSV para MySQL ou PostgreSQL (ambos foram tentados)**
* **Utilização do Vue.JS com Python para Backend (oportunidade de aprendizado)**
***
#### ✒️ Autor
* **Eric Matheus N Campelo**

***