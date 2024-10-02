import requests
import time

def fetch_jokes(min_jokes=100):
    jokes = []
    url = 'https://v2.jokeapi.dev/joke/Any'
    jokes_to_fetch = min_jokes
    batch_size = 10
    
    while len(jokes) < min_jokes:
        try:
            params = {
                'amount': min(batch_size, jokes_to_fetch)
            }
            response = requests.get(url, params=params)
            rate_limit_remaining = int(response.headers.get('RateLimit-Remaining', 0))
            retry_after = int(response.headers.get('Retry-After', 0))

            if rate_limit_remaining == 0 and retry_after > 0:
                print(f"Rate limit exceeded. Waiting for {retry_after} seconds.")
                time.sleep(retry_after)
                continue
            data = response.json()
            jokes.extend(data['jokes'])

            jokes_to_fetch = min_jokes - len(jokes)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break
    return jokes
