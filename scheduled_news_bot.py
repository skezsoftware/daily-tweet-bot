import tweepy
import schedule
import time
import requests
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials (replace with your keys and tokens)
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Tweepy client for posting tweets
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Dev.to API credentials (replace 'your_dev_to_api_key' with your Dev.to API key)
DEV_TO_API_URL = 'https://dev.to/api/articles'

# Function to fetch a coding-related article
def fetch_article():
    params = {
        'tag': 'programming',  # You can use tags like: javascript, python, webdev, etc.
        'per_page': 10,  # Number of articles to fetch
        'state': 'rising'  # Can be fresh, rising, or all
    }
    try:
        response = requests.get(DEV_TO_API_URL, params=params)
        if response.status_code == 200:
            articles = response.json()
            if articles:
                for article in articles:
                    title = article['title']
                    url = article['url']
                    
                    # Verify the article URL is accessible
                    try:
                        url_check = requests.get(url, timeout=5)
                        if url_check.status_code == 200:
                            return f"{title} - Read more: {url}"
                    except requests.RequestException:
                        print(f"Skipping article with broken link: {url}")
                        continue
                
                print("No articles with working links found.")
                return None
            else:
                print("No articles found.")
                return None
        else:
            print("Error fetching article:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred while fetching the article:", e)
        return None

# Function to post the article as a tweet
def post_article_tweet():
    message = fetch_article()
    if message:
        try:
            client.create_tweet(text=message)
            print("Tweet posted successfully:", message)
        except Exception as e:
            print("An error occurred while posting the tweet:", e)

# Schedule the article tweet at 9:00 AM PST
schedule.every().day.at("09:00").do(post_article_tweet)

# Keep the script running to check the schedule
# while True:
#     schedule.run_pending()
#     time.sleep(60)  
post_article_tweet()
