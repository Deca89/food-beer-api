import json
import urllib3
from random import randint





def lambda_handler(event, context):
    
    beer_id = event['pathParameters']['id']
    url = f"https://api.punkapi.com/v2/beers/{beer_id}"

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    data = json.loads(r.data)
    
    beer_name = data[0]["name"]
    beer_tagline = data[0]["tagline"]
    beer_abv = str(data[0]["abv"]) + "%"
    beer_img = data[0]["image_url"]
    
    beer_item = f"The beer you are looking for is called '{beer_name}, {beer_tagline}' Alcohol content is {beer_abv}."
    
    
    response_body = f"<h1>{beer_item}</h1><img src={beer_img} alt='Beer pic!' width='190' height='400'>"
    response_body = response_body + "<p></p><h1>  </h1><h2>  </h2><form id='homepage' action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m'><input type='submit' value='Go to Frontpage' /></form>"
    
    return {
    "statusCode": 200,
    "body": response_body,
    "headers": {
        'Content-Type': 'text/html',
    }
}
