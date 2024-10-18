import boto3

def list_ec2_instances(access_key, secret_key):
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    ec2 = session.resource('ec2')
    
    instances = ec2.instances.all()

    print("Listing EC2 Instances:")
    for instance in instances:
        print(f'Instance ID: {instance.id}, State: {instance.state["Name"]}, Type: {instance.instance_type}')

if __name__ == "__main__":
  
    ACCESS_KEY = 'AKIA5GSFKBPCIG3P6ZIE'
    SECRET_KEY = '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'
    
    list_ec2_instances(ACCESS_KEY, SECRET_KEY)
