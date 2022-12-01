# food-beer-api

This app suggests a beer to go with the food of your selection.
https://api.punkapi.com/v2/beers/ is used for our api calls.

Additional functionality includes saving the recomendation to favourites, which
stores the recommended beer to a DynamoDB table.
You can check out the favourites and also delete beers from the favourites table.
Lastly there is an option to subscribe to our SNS topic to get weekly beer recomendation.

Main page: https://8j55p9z8kf.execute-api.ap-southeast-2.amazonaws.com/dev/m? 