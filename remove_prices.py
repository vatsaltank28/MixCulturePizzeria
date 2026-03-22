import re

html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove all '.mrp', '.dc-price', and '.mpco-p'
content = re.sub(r'<div class="mrp">.*?</div>', '', content)
content = re.sub(r'<div class="dc-price">.*?</div>', '', content)
content = re.sub(r'<div class="mpco-p">.*?</div>', '', content)

# 2. Insert 10% discount notice after <div class="obadge">...</div>
discount_html = """
        <div style="background:rgba(212,168,50,0.15);border:1px solid var(--gold);color:var(--gold);padding:10px 16px;font-size:0.85rem;font-weight:bold;margin-bottom:20px;border-radius:4px;text-align:center;">
          🎉 10% Discount for all customers who reserve a table from the website!
        </div>"""

content = content.replace(
    '<div class="obadge">● Open Now · Daily 11 AM – 11 PM</div>',
    '<div class="obadge">● Open Now · Daily 11 AM – 11 PM</div>\n' + discount_html
)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML prices removed and discount added successfully.")
