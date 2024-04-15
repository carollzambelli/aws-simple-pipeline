data "aws_ecr_repository" "de04-demo-repo" {
  name = "de04-demo"
}

resource "aws_lambda_function" "de04-demo-func" {
    function_name = "de04-demo-func"
    timeout       = 30 # seconds
    image_uri     = "${data.aws_ecr_repository.de04-demo-repo.repository_url}:latest"
    package_type  = "Image"
    memory_size = 512
    role = "arn:aws:iam::505678360548:role/service-role/demo-role-rpe1uzfi"

}