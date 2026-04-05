import requests
import json

# Step 1: Fetch trending posts from Reddit
url = "https://www.reddit.com/r/popular.json"
headers = {"User-Agent": "TrendPulseBot/0.1"}
response = requests.get(url, headers=headers)

# Step 2: Convert response to JSON
data = response.json()

# Step 3: Save to file
with open("reddit_trending.json", "w") as f:
    json.dump(data, f, indent=4)

