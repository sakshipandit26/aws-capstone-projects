
# Project 2 — AWS Resource Automation Using Python

## 📌 Project Overview

This project demonstrates how common AWS resource operations can be automated using **Python and the boto3 AWS SDK**.

A menu-driven Python application was developed to perform basic operations on **Amazon S3** and **Amazon EC2** resources.

The project demonstrates practical cloud automation without manually performing every operation through the AWS Management Console.

---

## 🎯 Objective

The main objectives of this project are:

- Automate AWS operations using Python.
- Learn how to use the boto3 AWS SDK.
- Perform Amazon S3 operations programmatically.
- Perform Amazon EC2 operations programmatically.
- Understand AWS IAM permissions.
- Practice cloud resource lifecycle management.
- Reduce manual AWS console operations.

---

## ☁️ AWS Services and Technologies Used

| Service / Technology | Purpose |
|---|---|
| Amazon EC2 | Manage compute instances |
| Amazon S3 | Manage storage buckets and objects |
| AWS IAM | Control AWS permissions |
| Python | Application development |
| boto3 | AWS SDK for Python |

---

# 🏗️ Architecture

```text
                    USER
                      |
                      v
             +-------------------+
             | Python CLI        |
             | Automation Tool   |
             +---------+---------+
                       |
              +--------+--------+
              |                 |
              v                 v
       +-------------+    +-------------+
       | Amazon S3   |    | Amazon EC2  |
       | Operations  |    | Operations  |
       +-------------+    +-------------+
              |                 |
              +--------+--------+
                       |
                       v
                  AWS IAM
                Permissions
