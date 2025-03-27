from zipfile import ZipFile
import pdfplumber
import pandas as pd
import os

try:
    os.makedirs("pdfs_extraidos", exist_ok=True) # Criar pasta
    dir_name = "pdfs_extraidos"
    zip_path = os.path.join("pdfs", "anexos.zip") # Pasta e arquivo dentro da pasta que preciso

    # Extrair arquivos!
    with ZipFile(zip_path, "r") as f:
        f.extractall(dir_name) # Extrair tudo
except Exception as e:
    print("Ocorreu um erro ao extrair pdfs na pasta.")

anexo = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_path = os.path.join(dir_name, "tabela_procedimentos.csv")
pdf_path = os.path.join(dir_name, anexo)

# Lista que conterá o dataframe concatenado
all_tables = []

# Leitura do PDF
print('Criando dataframe...')
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()  
        for table in tables:
            df = pd.DataFrame(table)  # Criar DataFrame com a tabela extraída
            all_tables.append(df) # Adiciona a lista


# Concatenar todas as tabelas em um único DataFrame
print("Cocatenando dataframe ao csv")
if all_tables: # Se houver dados na tabela (TRUE)
    final_df = pd.concat(all_tables, ignore_index=True) # Cocatenar todas as tabelas
    
    # Substituir as abreviações OD e AMB na tabela
    final_df = final_df.replace({"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}) # dict é mais eficaz
    
    # Salvar como CSV, retirar índices e cabeçalhos do dataframe
    final_df.to_csv(csv_path, index=False, header=False)
    print(f"Tabela salva em {csv_path}")
else:
    print("Nenhuma tabela encontrada no PDF.")
               

            

