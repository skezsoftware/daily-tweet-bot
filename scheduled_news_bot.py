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

# NewsAPI credentials (replace 'your_news_api_key' with your NewsAPI key)
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = 'https://newsapi.org/v2/everything'

# Function to fetch a coding-related article
def fetch_article():
    params = {
        'q': 'coding OR programming OR software development OR programming languages',  # Keywords for tech-related articles
        'language': 'en',
        'sortBy': 'publishedAt',
        'apiKey': NEWS_API_KEY
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        if response.status_code == 200:
            articles = response.json().get('articles')
            if articles:
                # Get the latest article
                article = articles[0]
                title = article['title']
                url = article['url']
                return f"{title} - Read more: {url}"
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
while True:
    schedule.run_pending()
    time.sleep(60)  
# post_article_tweet()
