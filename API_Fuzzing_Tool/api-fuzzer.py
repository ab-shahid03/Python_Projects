import requests
import sys

# Loop through each word from stdin
for word in sys.stdin:
    word = word.strip()  # remove newline characters

    # Try using the word as part of an endpoint to test fuzzing
    url = f"https://jsonplaceholder.typicode.com/{word}"
    
    try:
        response = requests.get(url)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")

        # Try to parse JSON if possible
        try:
            print("Response:", response.json())
        except ValueError:
            print("Response not in JSON format.")
        
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed with error: {e}")
