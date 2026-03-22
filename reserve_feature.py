import re

html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Top Banner right after <body>
top_banner = """
<!-- TOP BANNER -->
<div style="background:var(--gold);color:var(--char);text-align:center;padding:12px 24px;font-weight:700;font-size:0.95rem;position:relative;z-index:1000;">
  🎉 Book your table online and get 10% OFF your bill! <a href="#" onclick="showResPopup();return false" style="color:var(--char);text-decoration:underline;margin-left:8px;">Reserve Now →</a>
  <span style="font-size:0.75rem;display:block;opacity:0.85;margin-top:4px;font-weight:600;">* T&C: Discount is valid ONLY upon showing the official reservation email to the staff at the restaurant.</span>
</div>
"""
content = content.replace("<body>", "<body>\n" + top_banner)

# 2. Add Reserve button to Navigation (Main Nav + Sticky)
nav_btn = '<a href="#" class="ncta" onclick="showPopup();return false">Order Now 🍕</a>'
nav_reserve_btn = '<a href="#" class="ncta" style="background:#f5edd8;color:#1a1814;margin-right:10px;" onclick="showResPopup();return false">Reserve Table 🛎️</a>\n  '
content = content.replace(nav_btn, nav_reserve_btn + nav_btn)

sticky_btn = '<a href="#" class="ofab" onclick="showPopup();return false">Order Now 🍕</a>'
sticky_reserve_btn = '<a href="#" class="ofab" style="background:#f5edd8;color:#1a1814;margin-bottom:8px;" onclick="showResPopup();return false">Reserve Table 🛎️</a>\n  '
content = content.replace(sticky_btn, sticky_reserve_btn + sticky_btn)

# 3. Add #res-popup CSS
css_popup = "#popup.show .pbox{transform:none}"
css_res_popup = """#popup.show .pbox{transform:none}
#res-popup{position:fixed;inset:0;z-index:999;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.82);backdrop-filter:blur(14px);opacity:0;pointer-events:none;transition:opacity .4s}
#res-popup.show{opacity:1;pointer-events:all}
#res-popup.show .pbox{transform:none}
"""
content = content.replace(css_popup, css_res_popup)

# 4. Add #res-popup HTML at the end before <script>
res_modal = """
<!-- RESERVE POPUP -->
<div id="res-popup" onclick="if(event.target===this)hideResPopup()">
  <div class="pbox">
    <button class="px" onclick="hideResPopup()">×</button>
    <div class="pico">🛎️</div>
    <h3 class="ptitle">Reserve a Table</h3>
    <p class="psub">Book your table online and enjoy 10% OFF your bill.</p>
    <p style="font-size:0.75rem; color:var(--gold); margin-bottom:15px; font-weight:bold;">*T&C: You must show this reservation confirmation email to the staff to avail the discount.</p>
    
    <form action="https://formsubmit.co/mixculturepizzeria@gmail.com" method="POST" style="display:flex;flex-direction:column;gap:12px;">
      <!-- Hidden Config Fields -->
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_subject" value="New Table Reservation from Website!">
      <input type="hidden" name="_template" value="table">
      
      <input type="text" name="Name" placeholder="Your Name" required style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;">
      <input type="tel" name="Phone" placeholder="Phone Number" required style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;">
      <input type="number" name="Guests" placeholder="Number of Guests" required min="1" max="20" style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;">
      <div style="display:flex;gap:12px;">
        <input type="date" name="Date" required style="flex:1;padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;">
        <input type="time" name="Time" required style="flex:1;padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;">
      </div>
      
      <button type="submit" style="background:var(--gold);color:var(--char);font-weight:bold;padding:14px;border:none;cursor:pointer;margin-top:10px;font-family:inherit;">Confirm Reservation</button>
    </form>
  </div>
</div>
"""
content = content.replace("<script>", res_modal + "\n<script>")

# 5. Add JS functions for res-popup
js_popup = "function hidePopup(){document.getElementById('popup').classList.remove('show')}"
js_res_popup = js_popup + """
function showResPopup(){document.getElementById('res-popup').classList.add('show')}
function hideResPopup(){document.getElementById('res-popup').classList.remove('show')}
"""
content = content.replace(js_popup, js_res_popup)


with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Reservation feature and top banner added successfully.")
