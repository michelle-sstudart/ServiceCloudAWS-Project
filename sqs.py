import boto3

def criar_fila_sqs(nome_fila):
    sqs = boto3.client('sqs')
    try:
        response = sqs.create_queue(QueueName=nome_fila)
        print(f"Fila SQS {nome_fila} criada com sucesso. URL: {response['QueueUrl']}")
        return response['QueueUrl']
    except Exception as e:
        print(f"Erro ao criar fila SQS: {str(e)}")
        return None
    
if __name__ == '__main__':
    nome_fila = "fila-contador-1"
    url = criar_fila_sqs(nome_fila)
    print(f"URL da fila SQS criada: {url}")
    