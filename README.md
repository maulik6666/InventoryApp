# Inventory App - COMP-3020 Final Project

A **cloud-based inventory management system** built with AWS Lambda, DynamoDB, API Gateway, S3, and GitHub Actions CI/CD.

## Technologies Used
- **AWS Services**:
  - Lambda (Python)
  - DynamoDB (NoSQL Database)
  - API Gateway (REST API)
  - S3 (Static Website Hosting)
  - CloudFront (HTTPS)
- **CI/CD**:
  - GitHub Actions (Automated Deployment)
  - Super Linter (Code Validation)

## Features
- **CRUD Operations**:
  - Add, view, update, and delete inventory items.
  - Filter items by location.
- **Automated Deployment**:
  - Lambda functions deploy on merge to `main`.
  - Website updates deploy to S3 automatically.
- **RESTful API**:
  - Tested with Postman/Restfox.