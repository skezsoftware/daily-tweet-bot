import tweepy
import random
import os
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

# Your existing messages list
messages = [
    "Use semantic HTML tags like <header>, <footer>, and <article> to improve your site’s accessibility and SEO. It tells both browsers and screen readers what each section of your content is for 🌐",
    "Don't forget the alt attribute for images! It’s essential for accessibility and helps with SEO when images don’t load properly 📸",
    "Organize your HTML with clear, nested structures. Good indentation and layout make debugging and updates a breeze 📂",
    "Keep your HTML lean by minimizing inline styles and scripts. This improves page load times and keeps your code cleaner 🚀",
    "Use <section> and <div> wisely; they serve different purposes. Sections group related content, while divs are more generic 🗂️",
    "Avoid relying on <br> tags to control layout. Use CSS for spacing and line breaks instead for a more maintainable structure 🎨",
    "Explore HTML5 input types, like email, date, and number to enhance form usability. These inputs make it easier for users to enter correct data ✍️",
    "Place JavaScript files at the end of the body section. This way, HTML loads first, boosting page performance ⚡️",
    "Include the <meta name='viewport' content='width=device-width, initial-scale=1.0'> tag for responsive designs. It helps your website look great on mobile 📱",
    "Label your forms properly using the <label for='id'> tag with matching IDs. It improves form accessibility and user experience ✅",
    "Use Flexbox (display: flex) to create responsive layouts that adapt to any screen size. It simplifies alignment and spacing of items 💪",
    "Try CSS Grid for complex layouts. It’s powerful for building responsive designs with ease, giving you control over rows and columns 🌐",
    "Use em and rem for font sizes to make your typography responsive. These units scale better across different devices 📏",
    "Design mobile-first by starting with min-width media queries. This approach makes sure your site works well on smaller screens first 📲",
    "CSS variables (--main-color: #333) make it easy to update colors and styles across your entire site. A single change can update multiple elements 🎨",
    "Background images should use background-size: cover for a responsive fit. This helps images look good without stretching or cropping unnecessarily 🖼️",
    "Use transform and transition for smooth CSS animations. Simple effects like scale or rotate can make your design feel dynamic 🎥",
    "Avoid using !important too often. It can make your CSS harder to manage and override 🛑",
    "Set a default font family in your CSS to keep your website looking consistent. Choose a fallback font stack in case your primary font doesn't load 🖋️",
    "Combine shorthand CSS properties for simplicity, like margin: 10px 20px. This reduces the amount of code and improves readability ✍️",
    "Use const and let in JavaScript instead of var to avoid accidental global variables. These keywords help keep your code secure and manageable 🔐",
    "Template literals (`Hello, ${name}!`) make string concatenation easier. They’re great for creating dynamic strings quickly ✨",
    "Write async code with async/await for cleaner handling of promises. It keeps your code looking synchronous, making it easier to read ⏳",
    "Use array methods like .map(), .filter(), and .reduce() for data manipulation. They’re powerful tools that improve code readability 🧩",
    "Keep your JavaScript functions pure and avoid modifying data outside of them. Pure functions help make your code more predictable and testable 🧼",
    "Use destructuring to unpack values from objects and arrays. It can make your code cleaner and more concise 🧹",
    "JavaScript’s index is best avoided as a key in lists. Use unique IDs instead to ensure list items stay stable 🔑",
    "Add try/catch blocks to handle errors gracefully. It can prevent your app from breaking unexpectedly 🛠️",
    "Break down complex tasks into small functions. This modular approach makes code more maintainable and reusable 🧩",
    "Use comments to explain why, not what. Clear code is better than heavily commented code 🚀",
    "Use list comprehensions in Python to build lists in one line. They’re concise and more readable than traditional loops 🐍",
    "Create virtual environments for each project in Python. It keeps your dependencies separate and avoids version conflicts 🌍",
    "Keep functions short and focused on one task. This makes your code easier to test and debug 🔍",
    "Use f-strings for efficient and readable string formatting, like f'Hello, {name}'. It’s Pythonic and avoids unnecessary concatenation 🧹",
    "Document functions with docstrings (''' Function description '''). It helps others understand your code’s purpose 📚",
    "Avoid mutable default arguments in functions, like []. They can lead to unexpected behavior and bugs 🛑",
    "Python’s enumerate() is handy for loops when you need index and value. It makes your code cleaner and avoids manual indexing 🔄",
    "Use with statements for file operations to ensure files close properly. This helps prevent memory leaks and errors 💾",
    "Handle specific exceptions with try/except. It provides clearer error messages and makes debugging easier 🐞",
    "Use type() and isinstance() to check object types. It ensures you’re working with the correct data types 🔍",
    "Use functional components and hooks in React for simpler, cleaner code. They’re modern, lightweight, and reduce boilerplate 🔄",
    "Keep each React component focused on one task. Small, focused components are easier to maintain and test 🛠️",
    "Manage side effects with useEffect and clean up after them when necessary. It helps prevent memory leaks in your app 💡",
    "Remember that state updates in React are asynchronous. Plan your code accordingly to avoid unexpected behavior ⏳",
    "React Context is a great way to avoid prop drilling in deeply nested components. It provides a simple, centralized state management 🎯",
    "Use useMemo and useCallback to optimize performance with heavy calculations. Memoization reduces unnecessary re-renders ⚙️",
    "Prefer controlled components for form handling. They offer better control and make it easy to track changes in state 📝",
    "Wrap multiple elements in <React.Fragment> or <> to avoid extra HTML tags. It keeps your DOM clean 📜",
    "Give unique keys to elements in lists to prevent unexpected re-renders. React relies on keys for identifying elements 🔑",
    "Validate props in React with PropTypes or TypeScript to catch bugs early. It’s a great way to add type-checking without extra code 🛡️",
    "Material-UI’s Grid component makes responsive layouts a breeze. It’s flexible and perfect for building adaptive layouts 📐",
    "Customize themes with ThemeProvider for consistent branding in Material-UI. Themes make global styles easy to manage 🌈",
    "Use makeStyles or styled to style Material-UI components. It keeps styling organized and component-specific 🖌️",
    "Material-UI icons are lightweight and customizable. Adding icons is an easy way to enhance user experience 🎨",
    "Material-UI’s Typography component offers great text styling options. It ensures consistent fonts across your app 🖋️",
    "Experiment with button variants like contained, outlined, and text for different actions. Each variant has its own visual style 🔘",
    "Spacing in Material-UI’s Grid component is easy with the spacing property. It helps maintain consistent gaps between items 🧹",
    "Material-UI’s Dialog component is perfect for pop-ups and modals. It provides easy-to-use, customizable dialogs 📤",
    "Use Material-UI’s Box component for quick layout adjustments. It’s highly versatile for spacing, colors, and more 📦",
    "Material-UI themes let you define your brand colors and font sizes. Update themes centrally to create a unified look 🎨",
    "Bootstrap’s grid system is great for responsive, mobile-first layouts. It lets you divide your layout into 12 columns easily 📱",
    "Use Bootstrap utility classes to quickly apply styles. They save you time by avoiding custom CSS 🚀",
    "Customize Bootstrap with SCSS variables to match your design. It’s a quick way to make Bootstrap fit your brand 🌐",
    "Bootstrap’s navbar component is perfect for fully responsive navigation bars. No need to code it from scratch 🖱️",
    "Use btn classes in Bootstrap for consistent button styling. It provides default styles that work out of the box ✨",
    "Display classes like d-flex and d-block make adjusting layouts easier. Bootstrap’s utilities save time on layout work 🔄",
    "Bootstrap cards are great for displaying structured data. They’re versatile and visually appealing 🃏",
    "Add Font Awesome icons to Bootstrap for more expressive designs. Icons can improve user experience and clarity 👍",
    "Bootstrap’s carousel component is perfect for image or content sliders. It’s great for rotating through content seamlessly 🎢",
    "Use responsive column classes (col-lg-4, col-sm-6) for flexible layouts. They adjust automatically to different screen sizes 📐",
    "Break down complex problems into smaller, manageable tasks before coding. It makes big challenges feel easier to tackle 🧩",
    "Write pseudocode to plan your logic before diving in. Pseudocode helps visualize your approach and saves time 📝",
    "Write code that’s clear and readable, even to others. Your future self will thank you for it 🙏",
    "Use version control like Git to keep track of changes. It’s essential for collaboration and maintaining project history 🌍",
    "Refactor code regularly to keep it clean and efficient. Good code is never written in one shot 🧼",
    "Stick to the DRY principle—Don’t Repeat Yourself. Reusable code is easier to maintain and debug ♻️",
    "Comment on why certain decisions were made, not what each line does. Make your intentions clear 🕵️",
    "Learn keyboard shortcuts in your editor to speed up workflow. Small shortcuts add up to big time savings ⏱️",
    "Test your code often, especially after changes. Early testing catches bugs before they become big issues 🔍",
    "Study design patterns for tried-and-true solutions. They make your code organized and scalable 🏗️",
    "Limit DOM manipulation to improve performance. It reduces reflow and repaints, keeping your app fast ⚡️",
    "Lazy load images for better initial load times. Users will see content faster, even on slower connections 🖼️",
    "Optimize images before adding them to your website. It reduces file size and speeds up load times 📸",
    "Cache data to improve performance and reduce server requests. Cached content loads faster for users 💾",
    "Keep dependencies up-to-date for security and performance improvements. Regular updates prevent vulnerabilities 🔒",
    "Debounce or throttle functions triggered by events like scroll and resize. It keeps your app responsive 🕹️",
    "Choose a small library instead of a full framework when appropriate. Sometimes, less is more 🎯",
    "Remove console logs from production code. It keeps your codebase clean and professional 🧹",
    "Optimize loops and avoid nested loops whenever possible. This improves efficiency and keeps performance high 🔄",
    "Use asynchronous code to avoid blocking the main thread. Async functions improve user experience 🌐",
    "Use console.log() effectively to trace errors and understand your code’s flow. Don’t be afraid to experiment with it 🕵️",
    "Read error messages carefully—they’re often more helpful than they seem. Error messages can lead you to the fix 🧭",
    "Developer tools are invaluable for inspecting and debugging. Don’t skip them; they’re your best friend 🛠️",
    "Set breakpoints instead of overusing console.log(). It makes debugging more organized and efficient 🎯",
    "Watch out for typos; they’re one of the most common bugs. Always double-check your spelling 🔤",
    "Wrap error-prone code in try/catch blocks. It helps you handle issues gracefully 🛡️",
    "Test functions with various inputs to catch edge cases. Comprehensive testing prevents unexpected behavior ⚖️",
    "If you’re stuck, step through the code line-by-line. Sometimes the answer is hiding in the details 🐛",
    "Explaining code out loud, even to yourself, can reveal insights. Sometimes, clarity comes from verbalizing ideas 🎙️",
    "Always keep a backup of working code before major changes. It’s a lifesaver when things go wrong 🛑"
    ]

# Track posted messages
posted_tracker = [False] * len(messages)
post_count = 0

# Add hashtag categories
hashtag_categories = {
    'html': '#WebDev #HTML #FrontEnd #CodingTips',
    'css': '#CSS #WebDesign #FrontEnd #UIDesign',
    'javascript': '#JavaScript #WebDev #Programming #CodeTips',
    'python': '#Python #Programming #CodingTips #PythonProgramming',
    'react': '#ReactJS #JavaScript #WebDev #FrontEnd',
    'material-ui': '#MaterialUI #ReactJS #UIDesign #FrontEnd',
    'bootstrap': '#Bootstrap #WebDesign #FrontEnd #CSS',
    'general': '#Programming #CodingTips #DevLife #CodeNewbie',
    'accessibility': '#a11y #WebAccessibility #Inclusion',
    'performance': '#WebPerformance #Optimization #DevTips'
}

def get_relevant_hashtags(message):
    """Determine relevant hashtags based on message content."""
    hashtags = []
    
    # Check message content for keywords and add relevant hashtags
    message_lower = message.lower()
    if any(term in message_lower for term in ['html', '<header>', '<footer>', '<article>', '<div>', '<section>']):
        hashtags.append(hashtag_categories['html'])
    if any(term in message_lower for term in ['css', 'style', 'flexbox', 'grid']):
        hashtags.append(hashtag_categories['css'])
    if any(term in message_lower for term in ['javascript', 'async', 'const', 'let']):
        hashtags.append(hashtag_categories['javascript'])
    if any(term in message_lower for term in ['python', 'f-string', 'enumerate']):
        hashtags.append(hashtag_categories['python'])
    if any(term in message_lower for term in ['react', 'component', 'useeffect']):
        hashtags.append(hashtag_categories['react'])
    if 'material-ui' in message_lower:
        hashtags.append(hashtag_categories['material-ui'])
    if 'bootstrap' in message_lower:
        hashtags.append(hashtag_categories['bootstrap'])
    if 'accessibility' in message_lower or 'alt attribute' in message_lower:
        hashtags.append(hashtag_categories['accessibility'])
    if any(term in message_lower for term in ['performance', 'speed', 'optimize']):
        hashtags.append(hashtag_categories['performance'])
    
    # If no specific category was matched, use general programming hashtags
    if not hashtags:
        hashtags.append(hashtag_categories['general'])
    
    return ' '.join(hashtags)

def post_tweet_v2():
    print(f"\n🤖 Tips Bot starting at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    global post_count
    
    unposted_indexes = [i for i, posted in enumerate(posted_tracker) if not posted]
    
    if not unposted_indexes:
        print("📝 All messages have been posted once. Resetting tracker.")
        for i in range(len(posted_tracker)):
            posted_tracker[i] = False
        unposted_indexes = list(range(len(messages)))
        post_count = 0
    
    selected_index = random.choice(unposted_indexes)
    message = messages[selected_index]
    
    # Add relevant hashtags to the message
    hashtags = get_relevant_hashtags(message)
    final_message = f"{message}\n\n{hashtags}"
    
    try:
        client.create_tweet(text=final_message)
        print(f"✅ Tweet posted successfully ({post_count + 1}/{len(messages)})")
        print(f"📊 Message index: {selected_index}")
        print(f"🏷️ Added hashtags: {hashtags}")
        posted_tracker[selected_index] = True
        post_count += 1
    except Exception as e:
        print(f"❌ Error posting tweet: {e}")

if __name__ == "__main__":
    post_tweet_v2()

