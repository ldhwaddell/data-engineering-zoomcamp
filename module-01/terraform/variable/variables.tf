variable "credentials" {
  description = "Credentials"
  default     = "/Users/lucaswaddell/git/data-engineering-zoomcamp/module-01/terraform/keys/de-course-terraform-011a9ded04ec.json"
}


variable "project" {
  description = "Project name"
  default     = "de-course-terraform"
}

variable "region" {
  description = "Project Region"
  default     = "us-east1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "BigQuery Dataset Name"
  default     = "de_course_dataset"
}

variable "gcs_bucket_name" {
  description = "Storage Bucket Name"
  default     = "de-course-terraform-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
