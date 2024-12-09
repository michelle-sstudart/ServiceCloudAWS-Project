import boto3

import boto3

def associar_sns_sqs(topic_arn, queue_arn):
    sns = boto3.client('sns')
    try:
        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='sqs',
            Endpoint=queue_arn
        )
        print(f"Associação entre SNS {topic_arn} e SQS {queue_arn} criada com sucesso.")
    except Exception as e:
        print(f"Erro ao associar SNS com SQS: {str(e)}")

if __name__ == "__main__":
    topic_arn = "arn:aws:sns:us-east-1:601931402457:topico-contador-1"  
    queue_arn = "arn:aws:sqs:us-east-1:601931402457:fila-contador-1"  
    associar_sns_sqs(topic_arn, queue_arn)
