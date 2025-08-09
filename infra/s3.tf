resource "aws_s3_bucket" "example_s3" {
  bucket = var.bucket_name
  
  tags = {
    Name        = "Test S3 bucket"
    Environment = "dev"
    Project = "project12"
    Service = "example"
    purpose = "test"
    backup = "monthly"
  }
}

# i added tags in order to make this code longer , 
# since the SonarQube checks the code longer 
# than 20 lines

resource "aws_s3_bucket_public_access_block" "example-public-access-block" {
  bucket = aws_s3_bucket.example_s3.id

  block_public_acls       = false                 # should be true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "example" {     # Sensitive
  bucket = aws_s3_bucket.example_s3.id
  versioning_configuration {
    status = "Enabled"
  }
}
