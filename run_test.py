from concurrent.futures import ThreadPoolExecutor

import requests

URL = "http://localhost:8000/counters/increment_atomic/test/"


# Function to send a request
def send_request(url):
    """Send a request to the server."""
    response = requests.get(URL)
    print(response.json())


# Send 10 requests in parallel
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request, URL) for _ in range(10)]

print("All requests completed.")