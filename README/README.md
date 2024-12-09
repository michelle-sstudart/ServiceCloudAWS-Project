# Projeto Service CLoud (AWS)

## Cenário de estudo para o projeto 

Cenário
A Ada Contabilidade enfrenta um desafio operacional diário: os contadores precisam enviar arquivos manualmente para armazenamento e, em seguida, registrar no banco de dados a quantidade de linhas contidas nesses arquivos. Esse processo manual é ineficiente e propenso a erros.

Crie uma solução que automatize a arquitetura em todo o seu fluxo, se baseando em práticas DevOps para simplificar o fluxo de trabalho e garantir a confiabilidade do processo.

 
## Descrição 

Este projeto visa automatizar o processamento de arquivos carregados em um bucket S3 da AWS, contando o número de linhas em cada arquivo e armazenando esses dados em uma tabela DynamoDB. O projeto integra diversos serviços AWS: incluindo S3, Lambda, SNS, SQS e DynamoDB.

## Componentes Implementados

1. **Amazon S3**
   - Bucket criado: `bucket-contador-1`
   - Funcionalidade: Armazenamento de arquivos `.txt`

2. **AWS Lambda**
   - Função criada: `MyLambdaFunction`
   - Funcionalidade: Processar arquivos do S3, mensagens do SNS e SQS, e inserir dados no DynamoDB

3. **Amazon SNS**
   - Tópico criado: `arn:aws:sns:us-east-1:********:MySNSTopic` #account id ocultada do readme
   - Funcionalidade: Notificar a função Lambda com mensagens

4. **Amazon SQS**
   - Fila criada: `https://sqs.us-east-1.amazonaws.com/****/fila-contador-1` # account id ocultada do readme
   - Funcionalidade: Fila para mensagens a serem processadas pela Lambda

5. **Amazon DynamoDB**
   - Tabela criada: `FileMetadata`
   - Funcionalidade: Armazenar metadados dos arquivos processados (nome do arquivo e número de linhas)

## Fluxo de Trabalho

1. **Upload de Arquivo para o S3**:
   - Um arquivo `.txt` é carregado no bucket S3.
   - O trigger do S3 aciona a função Lambda.

2. **Processamento pela Lambda**:
   - A Lambda lê o arquivo do S3.
   - Conta o número de linhas no arquivo.
   - Insere os metadados no DynamoDB.
   - Publica uma mensagem no SNS.
   - Envia uma mensagem para a fila SQS.

3. **Monitoramento e Logs**:
   - CloudWatch Logs configurado para monitorar a função Lambda.
   - Alarmes configurados para métricas críticas.
  

### Arquivo `requirements.txt`

```plaintext
boto3==1.28.2
```

### Como executar o projeto 

#### Fazer Upload de Arquivo para o S3

echo "Este é um arquivo de teste para acionar a função Lambda." > cloud-texte.txt

aws s3 cp cloud-texte.txt s3://bucket-contador-1/

#### Publicar Mensagem no SNS

aws sns publish --topic-arn arn:aws:sns:us-east-1:YOUR-ACCOUNT-ID:MySNSTopic --message "Teste de publicação no tópico SNS"

#### Enviar Mensagem para a Fila SQS

aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/YOUR-ACCOUNT-ID/fila-contador-1 --message-body "Teste de mensagem SQS"


### Requisitos de Instalação

 1 Instalações necessárias 

#### Atualizar repositórios
sudo apt update


#### Instalar Python e pip
sudo apt install python3 python3-pip python3-venv


#### Instalar AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install


#### Verificar instalações

python3 --version

pip3 --version

aws --version


#### Ative o ambiente no Linux

source venv/bin/activate



2 Configurar credenciais AWS:
aws configure
#### Inserir:
#### AWS Access Key ID
#### AWS Secret Access Key
#### Região padrão (ex: us-east-1)
#### Formato de saída (json)


3 Estrutura do Projeto:
#### Exemplo de diretorios

mkdir -p devops-file-processor/src

mkdir -p devops-file-processor/scripts

cd devops-file-processor


4 Criar ambiente virtual

python3 -m venv venv

source venv/bin/activate


5 Instalar bibliotecas

pip install boto3 psycopg2-binary


6 Desenvolvimento do Script 
-gerador de arquivo
-upload para S3
-processador Lambda com Boto3
-criação de recursos AWS com Boto3



### Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

Este `README.md` cobre os principais pontos do seu projeto, descreve o fluxo de trabalho, os componentes implementados, os pontos críticos, o monitoramento e como executar o projeto.



### Autores:
-[Michelle Sindeaux](https://github.com/michelle-sstudart)
