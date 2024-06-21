data "aws_ecr_repository" "dataops-demo-repo" {
  name = "dataops-demo"
}

resource "aws_lambda_function" "pipe_cadastro" {
    function_name = "pipe_cadastro"
    timeout       = 45 # seconds
    image_uri     = "${data.aws_ecr_repository.dataops-demo-repo.repository_url}:latest"
    package_type  = "Image"
    memory_size = 512
    role = "arn:aws:iam::505678360548:role/service-role/demo-role-rpe1uzfi"

}

resource "aws_cloudwatch_event_rule" "every_two_minutes" {
    name = "every_two_minutes"
    schedule_expression = "rate(2 minutes)"
}

resource "aws_cloudwatch_event_target" "pipe_cadastro_every_two_minutes" {
    rule = aws_cloudwatch_event_rule.every_two_minutes.name
    target_id = "pipe_cadastro"
    arn = aws_lambda_function.pipe_cadastro.arn
}


resource "aws_lambda_permission" "allow_cloudwatch_to_call_pipe_cadastro" {
    statement_id = "AllowExecutionFromCloudWatch"
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.pipe_cadastro.function_name
    principal = "events.amazonaws.com"
    source_arn = aws_cloudwatch_event_rule.every_two_minutes.arn
}