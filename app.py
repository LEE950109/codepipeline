import json
def lambda_handler(event, context):
    """
    HTTP 요청을 처리하는 AWS lambda 함수
    """
    # print("Event: ", event)
    #
    # response = {
    #     "statusCode": 200,
    #     "headers":{
    #         "Content-Type": "application/json"
    #     },
    #     "body": json.dumps({
    #         "message": "Hello from AWS lambda!",
    #         "input": event
    #     })
    # }
    return{
        "statusCode": 200,
        "body": "Hello, AWS Lambda!"
    }