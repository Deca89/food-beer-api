import boto3
import json
import urllib3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    data = dynamodb.Table('food-beer-api')
    response = data.scan()

# Get the items from the response
    items = response['Items']

# Make a list of the IDs

    beer_favorites = ""
    for item in items:
        beer_favorites = beer_favorites + f"<p>{item['beername']} {item['beertagline']} {item['beerabv']}</p>"
        beer_favorites = beer_favorites + f"<form id='L{item['id']}' action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m/favourites/{item['id']}'>   <input type='submit' value='Go to beer' /></form>"
        beer_favorites = beer_favorites + f"<form id='D{item['id']}' action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m/delete/{item['id']}'>   <input type='submit' color='red' value='Delete beer' /></form>"
    
    response_body = beer_favorites  + "<p></p><h1>  </h1><h2>  </h2><form id='homepage'action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m'><input type='submit' value='Go to Frontpage' /></form>"
    return {
        "statusCode": 200,
        "body": response_body,
        "headers": {
            'Content-Type': 'text/html',
        }
    }   