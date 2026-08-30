# Project 5 — Automated AWS Cost Optimizer

## 📌 Project Overview

This project demonstrates how AWS Lambda can be used to automate Amazon EC2 resource management and help reduce unnecessary cloud costs.

The Lambda function checks the current state of EC2 instances and identifies whether there are running instances that may need to be stopped.

The project demonstrates serverless automation, IAM permissions and CloudWatch monitoring.

---

## 🎯 Objective

The main objectives of this project are:

- Automate EC2 resource management.
- Identify running EC2 instances.
- Stop unnecessary instances when required.
- Use AWS Lambda for serverless automation.
- Monitor Lambda execution using CloudWatch.
- Apply IAM security principles.
- Demonstrate a practical AWS cost-optimization solution.

---

## ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon EC2 | Compute resources being monitored |
| AWS Lambda | Cost optimization automation |
| AWS IAM | Permissions and access control |
| Amazon CloudWatch | Logs and monitoring |
| Amazon EventBridge | Optional scheduled Lambda execution |

---

# 🏗️ Architecture

```text
                 EventBridge
                     |
                     | Scheduled Trigger
                     v
             +---------------+
             | AWS Lambda    |
             | Cost Optimizer|
             +-------+-------+
                     |
                     | Check EC2
                     v
             +---------------+
             | Amazon EC2    |
             | Instances     |
             +-------+-------+
                     |
                     | Stop when required
                     v
             EC2 Resources
                     
                     |
                     v
             +---------------+
             | CloudWatch    |
             | Logs          |
             +---------------+
