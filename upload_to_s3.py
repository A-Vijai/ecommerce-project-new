import boto3

s3_client=boto3.client('s3')
bucket_name='ecommerce-project-new '


def upload_to_s3(filename,current_date):
    year=current_date.year
    month=current_date.month
    day=current_date.day

    file_path=f'transactions/year={year}/month={month}/day={day}/{filename}'
    s3_client.upload_file(f'/tmp/{filename}',bucket_name,file_path)
    print(f"File uploaded to S3 Bucket {bucket_name}/{file_path}")
    return
