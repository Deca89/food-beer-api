import json

def lambda_handler(event, context):
    arvo = 'pizza'
    response_return = f"""
    <body> 
    <h1>Beer and food recommendations</h1>
    <h3>By Santeli, Nelli, Dennis</h3>
    <h3>Using https://api.punkapi.com/v2/beers/ for our api calls</h3>
    <p>Enter a dish into the text box below and you'll be given a suitable beer recommendation for it!</p>
    <form id='foodform' method='GET' action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m/searchresult/result'>
     <input type='text' id='wantedfood' name='food'/>
     <input type='submit'/>
    </form>
    <p></p>
    <a href='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m/favourites'> Check out your favourite beers!</a>
    <p>Subscribe to our weekly beer suggestion! Enter email below</p>
    <form id='emailform' method='GET' action='https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m/subscribe/email'>
     <input type='text' id='wantedemail' name='email'/>
     <input type='submit'/>
    </form>
    </body>
    """
    
    return {
        'statusCode': '200',
        'headers': {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*'
        },
        'body': response_return,
        "isBase64Encoded": False
    }
