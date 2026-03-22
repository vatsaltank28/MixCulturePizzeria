import os
import shutil
import re

html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# -----------------------------------------------------
# 1. ADD GREEN ACCENT
# -----------------------------------------------------
# Add variable
if "--green" not in content:
    content = content.replace("--red:#c0291c;", "--red:#c0291c;--green:#008a3f;")

# Navbar Logo Green Focus
content = content.replace('<div class="nword">Mix Culture<br><small>Pizzeria</small></div>', '<div class="nword">Mix <span style="color:var(--green)">Culture</span><br><small>Pizzeria</small></div>')

# Gradient rules
content = content.replace("background:var(--red);margin:18px 0", "background:linear-gradient(90deg, var(--red), var(--green));margin:18px 0")

# Reserve Table sticky button green
content = content.replace('style="background:#f5edd8;color:#1a1814;margin-bottom:8px;"', 'style="background:var(--green);color:#fff;margin-bottom:8px;"')


# -----------------------------------------------------
# 2. UPDATE PHONE NUMBER
# -----------------------------------------------------
# For visual text
content = content.replace('+91 88507 17019', '+91 88507 17019 / 976910078')


# -----------------------------------------------------
# 3. ADD 6TH GALLERY PHOTO
# -----------------------------------------------------
# File paths
source_dir = r"C:\Users\algo 11\.gemini\antigravity\brain\2450f5f4-9d3a-46ca-92d3-3f8b48b0bca4"
dest_dir = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\Mix Culture Food Photos"

# We know media__1774176843126.jpg is the pizza solves everything
photo = "media__1774176843126.jpg"
target = "Ambience_6.jpg"

try:
    shutil.copy2(os.path.join(source_dir, photo), os.path.join(dest_dir, target))
except Exception as e:
    pass # Ignored if it doesn't exist just in case script re-runs

# Update CSS for gallery 3x3 layout
old_ggrid_css = ".ggrid{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:280px 200px;gap:4px}"
new_ggrid_css = ".ggrid{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3, 220px);gap:4px}"
if old_ggrid_css in content:
    content = content.replace(old_ggrid_css, new_ggrid_css)

# Update HTML to add 6th item
old_gitems = """    <div class="gitem"><img src="Mix Culture Food Photos/Ambience_5.jpg" alt="Ambience 5" loading="lazy"><div class="gov"><span class="gcap">Wall Art</span></div></div>
  </div>"""

new_gitems = """    <div class="gitem"><img src="Mix Culture Food Photos/Ambience_5.jpg" alt="Ambience 5" loading="lazy"><div class="gov"><span class="gcap">Wall Art</span></div></div>
    <div class="gitem"><img src="Mix Culture Food Photos/Ambience_6.jpg" alt="Ambience 6" loading="lazy"><div class="gov"><span class="gcap">Pizza Solves Everything</span></div></div>
  </div>"""

if "Ambience_6.jpg" not in content:
    content = content.replace(old_gitems, new_gitems)


with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Contact info augmented, gallery updated, and green branding injected.")
