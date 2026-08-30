# Project 3 — Serverless Image Resizer

## 📌 Project Overview

This project demonstrates a serverless image-processing workflow using Amazon S3, AWS Lambda, and Amazon CloudWatch.

When an image is uploaded to the S3 bucket, an S3 event triggers the Lambda function automatically. The Lambda function processes the uploaded image and generates the required output.

This project demonstrates event-driven serverless architecture without using traditional servers.

---

## 🎯 Objective

The main objectives of this project are:

- Create a serverless image-processing application.
- Store images using Amazon S3.
- Automatically trigger AWS Lambda when an image is uploaded.
- Process images using Lambda.
- Monitor Lambda execution using CloudWatch.
- Understand event-driven AWS architecture.
- Configure IAM permissions securely.

---

## ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Store input and output images |
| AWS Lambda | Process uploaded images |
| Amazon CloudWatch | Monitor Lambda execution and logs |
| AWS IAM | Manage permissions |

---

## 🏗️ Architecture

```text
                    USER
                      |
                      | Upload Image
                      v
              +----------------+
              |   Amazon S3    |
              |  Input Bucket  |
              +-------+--------+
                      |
                      | ObjectCreated Event
                      v
              +----------------+
              |   AWS Lambda   |
              | Image Processor|
              +-------+--------+
                      |
                      | Process Image
                      v
              +----------------+
              |   Amazon S3    |
              | Output Image   |
              +----------------+
                      |
                      v
              +----------------+
              |  CloudWatch    |
              |     Logs       |
              +----------------+
