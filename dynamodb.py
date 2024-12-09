import boto3

def criar_tabela_dynamodb():
    dynamodb = boto3.client('dynamodb')
    try:
        dynamodb.create_table(
            TableName='FileMetadata',
            KeySchema=[
                {'AttributeName': 'FileName', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'FileName', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print("Tabela DynamoDB criada.")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

criar_tabela_dynamodb()
