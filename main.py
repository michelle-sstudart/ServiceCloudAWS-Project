import boto3

# Criar recursos AWS

# Inicializa o cliente S3
def create_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)

# Inicializa o cliente SNS
def create_sns_topic(topic_name):
    sns = boto3.client('sns')
    sns.create_topic(Name=topic_name)

# Inicializa o cliente SQS
def create_sqs_queue(queue_name):
    sqs = boto3.client('sqs')
    sqs.create_queue(QueueName=queue_name)
    
# Inicializa o cliente DynamoDB
def create_dynamodb_table(table_name):
    dynamodb = boto3.client('dynamodb')
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'FileName',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'FileName',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

# Criar recursos
create_s3_bucket('meu-bucket')
create_sns_topic('MySNSTopic')
create_sqs_queue('MyQueue')
create_dynamodb_table('FileMetadata')
