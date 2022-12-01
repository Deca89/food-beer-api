import urllib3
import boto3
import json

def lambda_handler(event, context):
    
    url = f"https://api.punkapi.com/v2/beers/random"

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    beer = json.loads(r.data)
    
    
    beer_id = beer[0]['id']
    name = beer[0]['name']
    tagline = beer[0]['tagline']
    abv = beer[0]['abv']
    image_url = beer[0]['image_url']
    
    message_to_send = f"This weeks recomendation is {name} {tagline} Check it out https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m/favourites/{beer_id}"
    
    
    
    
    client = boto3.client('sns')
    response = client.publish(TopicArn = 'arn:aws:sns:ap-southeast-2:341014156608:beer-topic', Message = message_to_send, Subject = 'Your beer recomendation of the week!')