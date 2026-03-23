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
    
    # Categorization logic
    lower_name = name.lower()
    
    if any(p in lower_name for p in ['pizza', 'margherita', 'funghi', 'tandoori paneer', 'the loaded legend']):
        pizzas.append({'name': name, 'path': path})
    elif any(p in lower_name for p in ['pasta', 'bechamel', 'marinara', 'parma rosa']):
        pastas.append({'name': name, 'path': path})
    elif any(d in lower_name for d in ['brownie', 'lava cake', 'mojito', 'mango', 'guava']):
        desserts.append({'name': name, 'path': path})
    else:
        # Sides
        sides.append({'name': name, 'path': path})

def gen_html(items, category_id):
    html: list = []
    for item in items:
        # We will use the photo name as the display name, and some generic text for price/badges if needed.
        # But for large lists, just name and simple price.
        short_name = item['name']
        if "Pizza" in short_name or len(short_name) > 20:
             short_name = short_name.replace("Pizza", "").strip()
             if len(short_name) > 25:
                 short_name = short_name[:22] + "..."
        html.append(f'<div class="mpc"><img src="{item["path"]}" alt="{item["name"]}" loading="lazy"><div class="mpco"><div class="mpco-n">{short_name}</div></div></div>')
    return "\n        ".join(html)

print("<!-- PIZZAS GENERATED -->")
print(gen_html(pizzas, "mp"))
print("<!-- SIDES GENERATED -->")
print(gen_html(sides, "ms"))
print("<!-- PASTAS GENERATED -->")
print(gen_html(pastas, "mpa"))
print("<!-- DESSERTS GENERATED -->")
print(gen_html(desserts, "md"))

print(f"Total: {len(pizzas)} pizzas, {len(sides)} sides, {len(pastas)} pastas, {len(desserts)} desserts.")
