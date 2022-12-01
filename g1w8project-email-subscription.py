import boto3



def lambda_handler(event, context):
    client = boto3.client('sns')

    response = client.subscribe(
    TopicArn="arn:aws:sns:ap-southeast-2:341014156608:beer-topic",
    Protocol="email",
    Endpoint= event['queryStringParameters']['email']
    )
    
    response_body = "<p>Check your email</p>"
    response_body = response_body + "<p></p><h1>  </h1><h2>  </h2><form id='homepage'action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m'><input type='submit' value='Go to Frontpage' /></form>"
    
    return {
    "statusCode": 200,
    "body": response_body,
    "headers": {
        'Content-Type': 'text/html',
    }
}

