terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.12.0"
    }
  }
}

provider "google" {
  project = "de-course-terraform"
  region  = "useast-1"
  # Configuration options
}


resource "google_storage_bucket" "auto-expire" {
  name     = "de-course-terraform-bucket"
  location = "US"

  # Optional, but recommended settings:
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 3 // days
    }
  }

  force_destroy = true
}
