import tweepy
import schedule
import time
import random
import os

# Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Authenticate using API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# List of inspirational messages
messages = [
    "Use semantic HTML to make your site accessible & SEO-friendly! 📈"
    "Clean and organized HTML is the first step to great code! 🌟"
    "Always add alt text to images for accessibility! ♿️"
    "Place JavaScript at the end of your HTML to speed up load times! 🚀"
    "Use <section> for related content to boost clarity. 📋"
    "Avoid <br> for spacing; let CSS do the work! 🎨"
    "HTML5 input types like email and date make forms user-friendly! 📝"
    "Make forms accessible by using <label> tags with for attributes! ✅"
    "Use the <meta> viewport tag for a responsive website. 📲"
    "Comments keep your HTML organized and easy to read. 🗂️"
    "Flexbox makes responsive design a breeze! 💨"
    "Use CSS Grid for powerful, advanced layouts! 🕸️"
    "Responsive typography is best with em and rem units! ✨"
    "Mobile-first design? Start with min-width media queries! 📱"
    "CSS variables are your friend for easy theme updates. 🎨"
    "Use background-size: cover for beautiful responsive images. 🌅"
    "Transform and animate with CSS for smooth effects. 🎬"
    "Use !important sparingly; it can make debugging hard! 🔍"
    "Shorthand CSS properties keep your styles concise! ✍️"
    "Set a default font-family for a consistent look. 🖋️"
    "Declare variables with const or let to avoid bugs! 🐛"
    "Template literals simplify string interpolation: `Hello, ${name}!`. 💡"
    "Use async/await for cleaner asynchronous code! ⏳"
    "Array methods like .map() and .filter() make data handling easier! 📊"
    "Pure functions make debugging easier; avoid side effects! 🔍"
    "Destructuring is your friend for cleaner code. ✨"
    "Avoid var; let and const keep variables block-scoped! 🚫"
    "Handle errors gracefully with try/catch. 🛡️"
    "Write modular code: break logic into small functions. 🧩"
    "Comments are a gift to future you and your team! 🎁"
    "List comprehensions in Python = readable and efficient code! 🐍"
    "Virtual environments are essential for managing dependencies. 🌐"
    "Short, focused functions are easier to test and maintain. 📏"
    "Use f-strings for cleaner formatting: f'Hello, {name}'. 🧹"
    "Document functions with docstrings for clarity! 📚"
    "Avoid mutable default arguments to prevent bugs. 🛑"
    "Python’s enumerate() is great for list loops. 🔄"
    "File operations? Use with statements for safety! 🛠️"
    "Catch specific error types for better debugging. 🐞"
    "Use type() and isinstance() to check object types. 🔍"
    "Functional components and hooks = cleaner React code! 🔥"
    "One component, one job—keep them small and focused! 👌"
    "Use useEffect for side effects, and always clean up! 🧼"
    "State updates are asynchronous; keep that in mind! ⏱️"
    "Use Context to avoid prop drilling. 🎯"
    "Memoize heavy calculations with useMemo and useCallback. 🧠"
    "Controlled components for form inputs make life easier. 🎉"
    "React.Fragment keeps your DOM clean! 📜"
    "Use unique keys in .map() to maintain component identity. 🔑"
    "PropTypes or TypeScript can catch issues early. 🛡️"
    "Material-UI Grid gives you responsive layouts easily. 📐"
    "Customize themes with ThemeProvider for a consistent look! 🎨"
    "Make styling easier with makeStyles or styled. 🖌️"
    "Material-UI icons add great functionality and style! 🌟"
    "Use Material-UI’s typography system for consistent text. 🖋️"
    "Explore button variants (contained, outlined) for context. 🔘"
    "Spacing in Material-UI’s Grid keeps items tidy. 🧹"
    "Dialogs in Material-UI make great popups and modals. 📤"
    "Material-UI’s Box component adds layout flexibility. 📦"
    "Customize themes to reflect your brand’s personality! 🌈"
    "Bootstrap’s grid is great for responsive, mobile-first layouts! 📱"
    "Utility classes make Bootstrap styling super fast. 🚀"
    "Customize with SCSS variables to match your design. 🎨"
    "Responsive navbars are easy with Bootstrap’s navbar. 🍔"
    "Bootstrap btn classes provide consistent button styling. ✨"
    "Display classes (d-flex, d-block) adjust layouts easily. 🔄"
    "Bootstrap cards structure data beautifully! 🃏"
    "Font Awesome icons enhance Bootstrap designs. 👍"
    "Bootstrap’s carousel component brings dynamic content. 🎢"
    "Responsive layouts are easy with col classes! 📐"
    "Break down problems into smaller parts before coding. 🧩"
    "Plan logic with pseudocode before jumping in. ✍️"
    "Write code that’s readable—future you will thank you! 🙏"
    "Use Git to track changes and collaborate. 🌍"
    "Refactor often for clean, maintainable code. 🧼"
    "Follow the DRY principle—avoid repeating yourself! ♻️"
    "Comments are for the 'why,' not the 'what'. 🕵️"
    "Learn code editor shortcuts to speed up coding. ⚡️"
    "Test often; don't wait until the end! 🔍"
    "Study design patterns for code that scales well. 🏗️"
    "Limit DOM manipulation to keep things fast! ⚡️"
    "Lazy load images for a faster first paint. 🖼️"
    "Optimize images before adding them for faster load times. 🐎"
    "Use caching to speed up web apps. 💾"
    "Stay up-to-date on dependencies for security. 🔒"
    "Debounce and throttle events like scroll and resize. ⏳"
    "Choose libraries over frameworks when possible. 🎯"
    "Keep console.logs minimal in production! 🧹"
    "Optimize loops and avoid nested loops where possible. 🔄"
    "Asynchronous code keeps the main thread free. 🌐"
    "Use console.log() strategically to trace errors. 🕵️"
    "Read error messages carefully; they’re your guide. 🧭"
    "Browser dev tools are invaluable for debugging. 🛠️"
    "Breakpoints are cleaner than multiple logs. 🎯"
    "Typos are a common source of bugs—check them first! 🔤"
    "Wrap error-prone code in try/catch. 🛡️"
    "Test functions with different inputs to catch edge cases. ⚖️"
    "Step through code line-by-line for tricky bugs. 🐛"
    "Explaining code out loud can reveal hidden issues. 🎙️"
    "Always keep a backup of working code. 🛑"
]

# Track posted messages
posted_tracker = [False] * len(messages)  # False means not posted, True means posted
post_count = 0  # Count of total messages posted

# Function to post a tweet using API v2
def post_tweet_v2():
    global post_count
    # Get indexes of messages that haven't been posted yet
    unposted_indexes = [i for i, posted in enumerate(posted_tracker) if not posted]

    # Check if all messages have been posted
    if not unposted_indexes:
        print("All messages have been posted once. Resetting tracker.")
        # Reset tracker and count
        for i in range(len(posted_tracker)):
            posted_tracker[i] = False
        unposted_indexes = list(range(len(messages)))
        post_count = 0

    # Select a random unposted message
    selected_index = random.choice(unposted_indexes)
    message = messages[selected_index]

    print("Attempting to post a tweet...")
    print(f"Selected message: {message}")
    print(f"API Key: {API_KEY}")
    print(f"Access Token: {ACCESS_TOKEN}")

    try:
        # Post the tweet
        client.create_tweet(text=message)
        print(f"Tweet posted successfully ({post_count + 1}/{len(messages)}): {message}")
        
        # Mark the message as posted and increment count
        posted_tracker[selected_index] = True
        post_count += 1

    except Exception as e:
        print("An error occurred while posting the tweet:", e)

# Schedule the tweet to post every day at 9:00 AM
schedule.every().day.at("11:00").do(post_tweet_v2)

# Run once for testing instead of an infinite loop
post_tweet_v2()  # Call the function once for testing
# Use schedule.run_pending() only if you want to test scheduling

