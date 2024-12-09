import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FileMetadata')
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    sqs = boto3.client('sqs')
    
    print("Evento recebido: ", event)
    
    for record in event['Records']:
        # Verifique se é um evento do S3
        if record.get('eventSource') == 'aws:s3':
            s3_bucket = record['s3']['bucket']['name']
            s3_key = record['s3']['object']['key']
        
        response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
        conteudo = response['Body'].read().decode('utf-8')
        num_linhas = conteudo.count('\n')

            # Inserir no DynamoDB
        table.put_item(
            Item={
                'FileName': s3_key,
                'LineCount': num_linhas
            }
        )
        print(f"Dados inseridos para o arquivo {s3_key}: {num_linhas} linhas.")

        message = f'File {s3_key} has {num_linhas} lines.' 
        sns.publish(TopicArn='arn:aws:sns:us-east-1:601931402457:topico-contador-1', Message=message) 
        sqs.send_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/601931402457/fila-contador-1', MessageBody=message)

    # Verifique se é um evento do SNS
    for record in event['Records']:
        if record.get('EventSource') == 'aws:sns': 
            sns_message = record['Sns']['Message'] 
            print("Mensagem do SNS: ", sns_message)