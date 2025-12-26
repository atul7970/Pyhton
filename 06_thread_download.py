import threading
import time
import requests

def download_file(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Finished download from {url} with status code {response.status_code} size {len(response.content)} bytes")


url = [
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/svg",
    "https://httpbin.org/image/webp"
]

start = time.time()

threads = []
for link in url:
    thread = threading.Thread(target=download_file, args=(link,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() 

end = time.time()
print(f"Total download time: {end - start:.2f} seconds")