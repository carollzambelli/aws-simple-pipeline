FROM public.ecr.aws/lambda/python:3.9

COPY ./src/. ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

CMD [ "app.handler" ]