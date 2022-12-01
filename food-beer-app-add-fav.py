import json
import boto3
import urllib3

def lambda_handler(event, context):
    beer_id = event['pathParameters']['id']
    url = f"https://api.punkapi.com/v2/beers/{beer_id}"

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    data = json.loads(r.data)
    
    beer_name = data[0]["name"]
    beer_tagline = data[0]["tagline"]
    beer_abv = str(data[0]["abv"]) + "%"
    
    client = boto3.client('dynamodb')
    response = client.put_item(
    Item={
        'id': {
            'N': event['pathParameters']['id'],
        },
        'beername' : {
            'S': beer_name
        },
        'beertagline' : {
            'S': beer_tagline
        },
        'beerabv' : {
            'S': beer_abv
        },
    },
    TableName='food-beer-api',
    )
    
    response_body = "<h3>The beer has been saved into your favorites!</h3> <a href='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m/Creamy%20lemon%20bar%20doused%20in%20powdered%20sugar'> Why not give this one a try?</a>"
    response_body = response_body + "<p></p><h1>  </h1><h2>  </h2><form id='homepage'action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m'><input type='submit' value='Go to Frontpage' /></form>"
    return {
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'headers': {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*'
        },
        'body': response_body,
        "isBase64Encoded": False
    }