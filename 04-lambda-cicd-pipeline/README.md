# Project 4 — CI/CD Pipeline for AWS Lambda

## 📌 Project Overview

This project demonstrates a CI/CD pipeline for automatically deploying AWS Lambda code from a GitHub repository.

The pipeline connects GitHub with AWS CodePipeline and deploys the application source code to an AWS Lambda function.

The final working architecture is:

```text
GitHub
   ↓
AWS CodePipeline
   ↓
AWS Lambda
   ↓
Amazon CloudWatch
