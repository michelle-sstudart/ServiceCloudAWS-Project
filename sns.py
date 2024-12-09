import boto3

def criar_topico_sns(nome_topico):
    sns = boto3.client('sns')
    try:
        response = sns.create_topic(Name=nome_topico)
        print(f"Topico SNS {nome_topico} criado com sucesso.ARN: {'TopicArn'}")
        return response['TopicArn']
    except Exception as e:
        print(f"Erro ao criar topico SNS: {str(e)}")
        return None
    
if __name__ == '__main__':
    nome_topico = "topico-contador-1"
    arn = criar_topico_sns(nome_topico)
    print(f"ARN do topico criado: {arn}")