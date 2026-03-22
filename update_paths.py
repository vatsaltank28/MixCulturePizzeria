import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replacer(match):
    old_path = match.group(1)
    filename = old_path.split('/')[-1]
    
    name, _ = os.path.splitext(filename)
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name).strip('-')
    new_filename = f"{name}.webp"
    
    new_path = f"optimized-images/{new_filename}"
    return f'src="{new_path}"'

# 1. Update <img src="..."> 
new_html = re.sub(r'src="(Mix Culture Food Photos/[^"]+)"', replacer, html)

# 2. Update CSS background url(...)
def bg_replacer(match):
    old_path = match.group(1)
    filename = old_path.split('/')[-1]
    
    name, _ = os.path.splitext(filename)
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name).strip('-')
    new_filename = f"{name}.webp"
    
    new_path = f"optimized-images/{new_filename}"
    # Keep the same surrounding quotes type as the original, but single quotes are safer for url('')
    return f"url('{new_path}')"

new_html = re.sub(r"url\(['\"]?(Mix Culture Food Photos/[^'\")]+)['\"]?\)", bg_replacer, new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("All image paths updated to optimized-images/")
