
# Automated Static Website Hosting on Amazon S3

## 📌 Project Overview

This project demonstrates how to host a static website using **Amazon S3** and automate the website file upload process using **Python and boto3**.

The website files are uploaded to an Amazon S3 bucket, where Amazon S3 serves the static website content.

The project helps demonstrate practical knowledge of AWS S3, Python automation, boto3, IAM permissions, and static website hosting.

---

## 🎯 Objective

The main objectives of this project are:

- Host a static website using Amazon S3.
- Create and configure an S3 bucket.
- Upload website files to S3.
- Automate file uploads using Python and boto3.
- Configure static website hosting.
- Understand AWS IAM permissions.
- Verify the website through a browser.

---

## ☁️ AWS Services and Technologies Used

| Service / Technology | Purpose |
|---|---|
| Amazon S3 | Store and host website files |
| AWS IAM | Manage permissions |
| Python | Automation script |
| boto3 | Python SDK for AWS |
| HTML | Website structure |
| CSS | Website styling |

---

## 🏗️ Architecture

```text
                    USER
                      |
                      | HTTP Request
                      v
              +----------------+
              |   Amazon S3    |
              |                |
              | Static Website |
              |    Hosting     |
              +-------+--------+
                      |
                      v
               Website Files
               HTML / CSS / Images


        Python + boto3
               |
               | Upload Files
               v
        +----------------+
        |   Amazon S3    |
        |     Bucket     |
        +----------------+
