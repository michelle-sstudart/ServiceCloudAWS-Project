import boto3
import random
import os

def gerar_arquivo(nome_arquivo):
    num_linhas = random.randint(1, 100)  # Número aleatório de linhas
    with open(nome_arquivo, 'w') as f:
        for i in range(num_linhas):
            f.write(f"Linha {i+1}\n")
    print(f"Arquivo contadores {nome_arquivo} gerado com {num_linhas} linhas.")
    return num_linhas

def enviar_para_s3(nome_arquivo, bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(nome_arquivo, bucket_name, nome_arquivo)
        print(f"Arquivo contador {nome_arquivo} enviado para o bucket {bucket_name}.")
    except Exception as e:
        print(f"Erro ao enviar arquivo: {e}")

# Gerar e enviar o arquivo
nome_arquivo = "texto_contador_linha.txt"
bucket_name = "bucket-contador-1"
num_linhas = gerar_arquivo(nome_arquivo)
enviar_para_s3(nome_arquivo, bucket_name)
os.remove(nome_arquivo)

