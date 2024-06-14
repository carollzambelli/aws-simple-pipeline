data "aws_ecr_repository" "dataops-demo-repo" {
  name = "dataops-demo"
}

resource "aws_lambda_function" "ingestion_cadastro" {
    function_name = "ingestion_cadastro"
    timeout       = 30 # seconds
    image_uri     = "${data.aws_ecr_repository.dataops-demo-repo.repository_url}:latest"
    package_type  = "Image"
    memory_size = 512
    role = "arn:aws:iam::505678360548:role/service-role/demo-role-rpe1uzfi"

}

resource "aws_lambda_function" "prep_cadastro" {
    function_name = "prep_cadastro"
    timeout       = 30 # seconds
    image_uri     = "${data.aws_ecr_repository.dataops-demo-repo.repository_url}:latest"
    package_type  = "Image"
    memory_size = 512
    role = "arn:aws:iam::505678360548:role/service-role/demo-role-rpe1uzfi"

}