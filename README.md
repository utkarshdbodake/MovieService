# MovieService
IMDB like movie service.

Run below code in ipython to get results.


```
import  requests, json
headers = {'content-type':'application/json'}
url = 'https://arcane-escarpment-9354.herokuapp.com/movies/search/'
data = {"movie_name": "Oz", "director": "Victor", "genre": "Fantasy", "imdb_score": 8.3, "popularity": 83}
params = {'content': json.dumps(data)}
response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
	print response.json()['size']
	print json.dumps(response.json(), indent=4, sort_keys=True)
else:
	print response
```
