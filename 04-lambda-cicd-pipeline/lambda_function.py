def lambda_handler(event, context):
    print("===== CI/CD LAMBDA DEPLOYMENT SUCCESSFUL =====")

    return {
        "statusCode": 200,
        "body": "Lambda deployed successfully through CI/CD!"
    }
