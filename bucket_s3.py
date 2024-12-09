import boto3

def criar_bucket_s3(bucket_name, region='us-east-1'):
    s3 = boto3.client('s3', region_name=region)
    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
            Bucket=bucket_name,          
        
            CreateBucketConfiguration={'LocationConstraint': region}
        )
        print(f"Bucket {bucket_name} criado com sucesso.")
    
    except Exception as e:
         #Imprime detalhes completos do erro
        print(f"Erro ao criar bucket: {str(e)}")

# Nome do bucket S3
bucket_name = "bucket-contador-1"
criar_bucket_s3(bucket_name)



