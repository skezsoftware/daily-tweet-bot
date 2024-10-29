from scheduled_news_bot import post_article_tweet
from post_to_x import post_tweet_v2
from datetime import datetime

print(f"\n🧪 Testing bots at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

print("\n📰 Testing News Bot...")
post_article_tweet()

print("\n💡 Testing Tips Bot...")
post_tweet_v2()

print("\n✅ Test complete!") 