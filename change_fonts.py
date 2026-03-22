import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace fonts in the link tag (using regex to be safe about exactly what is replaced)
# We find the <link href="https://fonts.googleapis.com/css2?...&display=swap"
text = re.sub(
    r'href="https://fonts.googleapis.com/css2\?[^"]+"',
    r'href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,600&family=Space+Mono:wght@400;700&display=swap"',
    text,
    count=1
)

# Replace the CSS values
text = text.replace("'Syne', sans-serif", "'Outfit', sans-serif")
text = text.replace("'Fraunces', serif", "'Playfair Display', serif")
text = text.replace("'DM Mono', monospace", "'Space Mono', monospace")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fonts fully updated to Outfit, Playfair Display, and Space Mono.")
