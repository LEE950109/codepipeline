import boto3
import json

def lambda_handler(event, context):
    # AWS CodePipeline 클라이언트 생성
    codepipeline = boto3.client('codepipeline')

    # CodePipeline 이벤트에서 Job ID 추출
    job_id = event['CodePipeline.job']['id']

    try:
        # Lambda 작업 로직
        result = {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }

        # 작업 성공 알림
        codepipeline.put_job_success_result(jobId=job_id)

        return result
    except Exception as e:
        # 작업 실패 알림
        codepipeline.put_job_failure_result(
            jobId=job_id,
            failureDetails={
                'type': 'JobFailed',
                'message': str(e)
            }
        )
        raise e
