import re

# Read generated HTMLs
with open("gen.py", "r", encoding="utf-8") as f:
    pass # we can just run the logic again to avoid reading from stdout

import os

directory = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\Mix Culture Food Photos"

pizzas = []
sides = []
pastas = []
desserts = []

for filename in os.listdir(directory):
    if not filename.endswith('.jpg'):
        continue
    
    path = f"Mix Culture Food Photos/{filename}"
    name = filename.replace('.jpg', '')
    
    lower_name = name.lower()
    
    if any(p in lower_name for p in ['pizza', 'margherita', 'funghi', 'tandoori paneer', 'the loaded legend']):
        pizzas.append({'name': name, 'path': path})
    elif any(p in lower_name for p in ['pasta', 'bechamel', 'marinara', 'parma rosa']):
        pastas.append({'name': name, 'path': path})
    elif any(d in lower_name for d in ['brownie', 'lava cake', 'mojito', 'mango', 'guava']):
        desserts.append({'name': name, 'path': path})
    else:
        sides.append({'name': name, 'path': path})

def gen_html(items):
    html = []
    for item in items:
        short_name = item['name']
        if "Pizza" in short_name or len(short_name) > 20:
             short_name = short_name.replace("Pizza", "").strip()
             if len(short_name) > 25:
                 short_name = short_name[:22] + "..."
        html.append(f'        <div class="mpc"><img src="{item["path"]}" alt="{item["name"]}" loading="lazy"><div class="mpco"><div class="mpco-n">{short_name}</div></div></div>')
    return "\n".join(html)

pizza_html = gen_html(pizzas)
side_html = gen_html(sides)
pasta_html = gen_html(pastas)
dessert_html = gen_html(desserts)

html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

def replace_section(content, section_marker, new_html):
    pattern = r'(<!-- ' + section_marker + r' -->\s*<div id=".*?" class=".*?">\s*<div class="mpgrid".*?>)(.*?)(      </div>)'
    return re.sub(pattern, lambda m: m.group(1) + '\n' + new_html + '\n' + m.group(3), content, flags=re.DOTALL)

content = replace_section(content, "PIZZAS", pizza_html)
content = replace_section(content, "SIDES", side_html)
content = replace_section(content, "PASTA", pasta_html)
content = replace_section(content, "DESSERTS", dessert_html)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML updated successfully.")
