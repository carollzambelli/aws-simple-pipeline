from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.operators.aws_lambda import AwsLambdaInvokeFunctionOperator



with DAG(
    "de04-dataops",
    start_date=datetime(2023, 10, 10), 
    schedule_interval=timedelta(minutes=2),
    catchup=False) as dag:

    invoke_lambda_function = AwsLambdaInvokeFunctionOperator(
    task_id='setup__invoke_lambda_function',
    function_name="de04-demo-func",
    payload={"step":"ingestion"},
)


invoke_lambda_function