variable "token" {}

terraform {
  required_providers {
    sonarcloud = {
      source  = "rewe-digital/sonarcloud"
      version = "0.2.1"
    }
  }
}

provider "sonarcloud" {
  organization = "petereon"
  token        = var.token
}

resource "sonarcloud_project" "petereon_battleship" {
  key        = "petereon_battleship"
  name       = "Battleship"
  visibility = "public"
}
