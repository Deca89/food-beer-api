import json
import urllib3
from random import randint





def lambda_handler(event, context):
    
    food_choice = event['pathParameters']['food']
    url = f"https://api.punkapi.com/v2/beers?food={food_choice}"

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    data = json.loads(r.data)

    beer_list = []

    for beer in data:
        beer_id = beer['id']
        name = beer['name']
        tagline = beer['tagline']
        abv = beer['abv']
        image_url = beer['image_url']

        beer_item = {
            'beer_id': beer_id,
            'name': name,
            'tagline': tagline,
            'abv': abv,
            'image_url': image_url
        }
        beer_list.append(beer_item)

    value = randint(0, len(beer_list)-1)

    try_this = beer_list[value]
    
    try_id = try_this['beer_id']
    try_name = try_this['name']
    try_tagline = try_this['tagline']
    try_abv = try_this['abv']
    try_image = try_this['image_url']

    suggestion = f'The beer that goes well with {food_choice} is \"{try_name}, {try_tagline}\". Alcohol content is {try_abv}%'
    
    try: response_body = f"<h1>{suggestion}</h1><a href='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/library/{try_id}'> Save to favourites!</a> <img src={try_image} alt='Beer pic!' width='190' height='400'>"
    finally:
        return {
    "statusCode": 200,
    "body": response_body,
    "headers": {
        'Content-Type': 'text/html',
    }
}


