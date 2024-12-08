
import boto3

def upload_to_s3(file_path, bucket_name, object_name=None, aws_access_key=None, aws_secret_key=None):
    """
    Upload a file to an S3 bucket.
    Args:
        file_path (str): Path to the file to upload.
        bucket_name (str): Name of the S3 bucket.
        object_name (str, optional): S3 object name. Defaults to file_path name.
        aws_access_key (str): AWS access key ID.
        aws_secret_access_key (str): AWS secret access key.
    Returns:
        str: URL of the uploaded file.
    """
    if object_name is None:
        object_name = file_path.split("/")[-1]

    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    s3_client.upload_file(file_path, bucket_name, object_name)
    file_url = f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
    return file_url
