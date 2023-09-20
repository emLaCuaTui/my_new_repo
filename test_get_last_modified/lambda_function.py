import json
import boto3
import datetime
import random
import hashlib
import io
#Viet ơi sep 21 1:38

def generate_prepared_statement_name(query_statement):
    #Test
    # Lấy timestamp hiện tại
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Tạo một số ngẫu nhiên (ví dụ: 20 bits)
    random_number = random.getrandbits(20)
    
    # Kết hợp timestamp và số ngẫu nhiên
    combined_data = f"{current_timestamp}-{random_number}"
    
    # Tạo giá trị băm (SHA-256) từ chuỗi kết hợp
    hashed_data = hashlib.sha256(combined_data.encode()).hexdigest()
    
    # Return the hashed string as the prepared statement name.
    return hashed_data
        
def lambda_handler(event, context):
    # ec2 = boto3.client('ec2')
    # regions = map(lambda x: x['RegionName'], ec2.describe_regions()['Regions'])
    # for region in regions:
    #     print(region)
    
    # print ("ztest here")
    # ec2 = boto3.client('ec2', region_name="ap-northeast-1")

    # client = boto3.client('stepfunctions', region_name="ap-northeast-1")
    # status_code = client.start_execution(
    #         stateMachineArn="arn:aws:states:ap-northeast-1:735206531520:stateMachine:mf_hm_triggerNewdemandLogicApp",
    #         name= str(datetime.datetime.now().timestamp()),
    #         input= json.dumps(event)
    #     ) 

    # print(status_code)
    
    
    test = {
  "query_statement": "SELECT * FROM my_table"
}
    
    # Get the query statement from the event.
    query_statement = test['query_statement']
    
    # Generate a prepared statement name for the query statement.
    prepared_statement_name = generate_prepared_statement_name(query_statement)
    
    # Return the prepared statement name.
    return {
      'prepared_statement_name': prepared_statement_name
    }