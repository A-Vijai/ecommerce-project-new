from datetime import date, timedelta
import json
from mock_data import generate_data
from upload_to_s3 import upload_to_s3


start_date=date(2024,5,22)
end_date=date.today()


def lambda_handler(event,context):

    for current_date in range((end_date- start_date).days+1):
        current_date=start_date+timedelta(days=current_date)
        print(current_date)
        date_str=str(current_date)
        generate_data(current_date,date_str)
        upload_to_s3(f'transactions_{date_str}.csv',current_date)


    
    return{
        'statusCode': 200,
        'body': json.dumps(f'Ecommerce data generated successfully')
    }
        

    


