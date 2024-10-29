import tweepy
import requests
import os
import random
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Initialize Twitter client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

DEV_TO_API_URL = 'https://dev.to/api/articles'

def fetch_article():
    print(f"\n🔍 Fetching article at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Multiple tags to search for
    tags = [
        'programming',
        'webdev',
        'javascript',
        'python',
        'coding',
        'tutorial',
        'beginners',
        'react',
        'productivity',
        'devops'
    ]
    
    # Randomly select a tag
    selected_tag = random.choice(tags)
    print(f"🏷️ Selected tag: {selected_tag}")
    
    params = {
        'tag': selected_tag,
        'per_page': 10,
        'state': 'rising'
    }
    
    try:
        response = requests.get(DEV_TO_API_URL, params=params)
        if response.status_code == 200:
            articles = response.json()
            if articles:
                for article in articles:
                    title = article['title']
                    url = article['url']
                    try:
                        url_check = requests.get(url, timeout=5)
                        if url_check.status_code == 200:
                            return f"{title} - Read more: {url} #{selected_tag} #coding #programming"
                    except requests.RequestException:
                        print(f"⚠️ Skipping article with broken link: {url}")
                        continue
        print("❌ No suitable articles found")
        return None
    except Exception as e:
        print(f"❌ Error fetching article: {e}")
        return None

def post_article_tweet():
    print(f"\n🤖 News Bot starting at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    message = fetch_article()
    if message:
        try:
            client.create_tweet(text=message)
            print(f"✅ Tweet posted successfully: {message}")
        except Exception as e:
            print(f"❌ Error posting tweet: {e}")
    else:
        print("❌ No message to post")

if __name__ == "__main__":
    post_article_tweet()
