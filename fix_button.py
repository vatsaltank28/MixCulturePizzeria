import re

html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

old_badges = """    <div class="pbadges rv d1">
      <a href="https://www.zomato.com/mumbai/mix-culture-pizzeria-vile-parle-east" target="_blank" class="pbadge"><div class="pb-logo">🍅</div><div><span class="pb-name">Zomato</span><span class="pb-rating">4.4 ★</span></div></a>
      <a href="https://www.swiggy.com/restaurants/mix-culture-pizzeria-vile-parle-east-mumbai-1152906/dineout" target="_blank" class="pbadge"><div class="pb-logo">🛵</div><div><span class="pb-name">Swiggy Dineout</span><span class="pb-rating">4.6 ★ · 164 reviews</span></div></a>
      <a href="https://www.justdial.com/Mumbai/Mix-Culture-Pizzeria-Opposite-RBL-Bank-Vile-Parle-East/022PXX22-XX22-220128171945-Z5U4_BZDET" target="_blank" class="pbadge"><div class="pb-logo">📍</div><div><span class="pb-name">Justdial</span><span class="pb-rating">4.4 ★ · 370 ratings</span></div></a>
    </div>"""

new_badges = """    <div class="pbadges rv d1">
      <a href="https://www.zomato.com/mumbai/mix-culture-pizzeria-vile-parle-east" target="_blank" class="pbadge"><div class="pb-logo">🍅</div><div><span class="pb-name">Zomato</span><span class="pb-rating">4.4 ★</span></div></a>
      <a href="https://www.swiggy.com/restaurants/mix-culture-pizzeria-vile-parle-east-mumbai-1152906/dineout" target="_blank" class="pbadge"><div class="pb-logo">🛵</div><div><span class="pb-name">Swiggy Dineout</span><span class="pb-rating">4.6 ★ · 164 reviews</span></div></a>
      <a href="https://www.justdial.com/Mumbai/Mix-Culture-Pizzeria-Opposite-RBL-Bank-Vile-Parle-East/022PXX22-XX22-220128171945-Z5U4_BZDET" target="_blank" class="pbadge"><div class="pb-logo">📍</div><div><span class="pb-name">Justdial</span><span class="pb-rating">4.4 ★ · 370 ratings</span></div></a>
    </div>
    <div style="text-align:center;margin-top:40px;margin-bottom:20px;">
      <button onclick="showReviewPopup()" class="btnr" style="border:none;cursor:pointer;font-family:inherit;">✏️ Write a Review</button>
    </div>"""

if "showReviewPopup()" not in content.split('id="reviews"')[1]:
    content = content.replace(old_badges, new_badges)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Button successfully re-added to html")
