import boto3
import os
from PIL import Image

s3 = boto3.client("s3")

OUTPUT_BUCKET = "image-resizer-output-2026-8274"

MAX_SIZE = (300, 300)


def lambda_handler(event, context):

    print("===== IMAGE RESIZER STARTED =====")

    for record in event["Records"]:

        source_bucket = record["s3"]["bucket"]["name"]
        object_key = record["s3"]["object"]["key"]

        print(f"Source bucket: {source_bucket}")
        print(f"Image: {object_key}")

        filename = os.path.basename(object_key)

        input_path = f"/tmp/{filename}"
        output_path = f"/tmp/resized-{filename}"

        # Download original image
        s3.download_file(
            source_bucket,
            object_key,
            input_path
        )

        # Open image
        image = Image.open(input_path)

        print(f"Original size: {image.size}")

        # Resize
        image.thumbnail(MAX_SIZE)

        print(f"New size: {image.size}")

        # Save resized image
        image.save(
            output_path,
            format=image.format
        )

        # Output filename
        output_key = f"resized-{filename}"

        # Upload resized image
        s3.upload_file(
            output_path,
            OUTPUT_BUCKET,
            output_key
        )

        print(
            f"SUCCESS: {output_key} uploaded to {OUTPUT_BUCKET}"
        )

    return {
        "statusCode": 200,
        "body": "Image resized successfully"
    }