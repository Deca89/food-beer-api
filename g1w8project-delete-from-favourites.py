import os
import boto3
import urllib3
import json





def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    
    response = client.delete_item(
    Key={
        'id': {
            'N': event['pathParameters']['id'],
        },
    },
    TableName='food-beer-api',
)

   
    beer_id = event['pathParameters']['id']
    url = f"https://api.punkapi.com/v2/beers/{beer_id}"

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    data = json.loads(r.data)
    
    beer_name = data[0]["name"]
    beer_tagline = data[0]["tagline"]
    beer_abv = str(data[0]["abv"]) + "%"
    beer_img = data[0]["image_url"]
    
    beer_item = f"You deleted '{beer_name}' from your favourites."
    
    
    response_body = f"<h1>{beer_item}</h1><img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIY3nL0z0e0XkxOAGoy3k97v_8hTa0DmO28w&usqp=CAU alt='So sad!' width='400' height='400'>"
    response_body = response_body + "<p></p><h1>  </h1><h2>  </h2><form id='homepage'action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m'><input type='submit' value='Go to Frontpage' /></form>"
    return {
    "statusCode": 200,
    "body": response_body,
    "headers": {
        'Content-Type': 'text/html',
    }
}