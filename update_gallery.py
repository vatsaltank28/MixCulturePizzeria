import os
import shutil

source_dir = r"C:\Users\algo 11\.gemini\antigravity\brain\2450f5f4-9d3a-46ca-92d3-3f8b48b0bca4"
dest_dir = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\Mix Culture Food Photos"

media_files = [
    "media__1774176321640.png",
    "media__1774176326998.png",
    "media__1774176342063.png",
    "media__1774176346252.png",
    "media__1774176533302.jpg"
]

new_names = [
    "Ambience_1.png",
    "Ambience_2.png",
    "Ambience_3.png",
    "Ambience_4.png",
    "Ambience_5.jpg"
]

# Copy files
for old, new in zip(media_files, new_names):
    shutil.copy2(os.path.join(source_dir, old), os.path.join(dest_dir, new))

# Update index.html
html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace gallery grid
old_ggrid = content.split('<div class="ggrid" style="max-width:1400px;margin:0 auto">')[1].split('</section>')[0]

new_ggrid = """
    <div class="gitem"><img src="Mix Culture Food Photos/Ambience_1.png" alt="Ambience 1" loading="lazy"><div class="gov"><span class="gcap">Cozy Seating</span></div></div>
    <div class="gitem"><img src="Mix Culture Food Photos/Ambience_2.png" alt="Ambience 2" loading="lazy"><div class="gov"><span class="gcap">Green Wall</span></div></div>
    <div class="gitem"><img src="Mix Culture Food Photos/Ambience_3.png" alt="Ambience 3" loading="lazy"><div class="gov"><span class="gcap">Modern Vibes</span></div></div>
    <div class="gitem"><img src="Mix Culture Food Photos/Ambience_4.png" alt="Ambience 4" loading="lazy"><div class="gov"><span class="gcap">Warm Lighting</span></div></div>
    <div class="gitem"><img src="Mix Culture Food Photos/Ambience_5.jpg" alt="Ambience 5" loading="lazy"><div class="gov"><span class="gcap">Wall Art</span></div></div>
  </div>
"""

full_old_section = '<div class="ggrid" style="max-width:1400px;margin:0 auto">' + old_ggrid

content = content.replace(full_old_section, '<div class="ggrid" style="max-width:1400px;margin:0 auto">\n' + new_ggrid)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Gallery updated successfully")
