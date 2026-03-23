import re

html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Insert "Write a Review" button if missing
if "Write a Review" not in content: # Check in body loosely (or generally across file)
    button_html = """    <div class="pbadges rv d1">
      <a href="https://www.zomato.com/mumbai/mix-culture-pizzeria-vile-parle-east" target="_blank" class="pbadge"><div class="pb-logo">🍅</div><div><span class="pb-name">Zomato</span><span class="pb-rating">4.4 ★</span></div></a>
      <a href="https://www.swiggy.com/restaurants/mix-culture-pizzeria-vile-parle-east-mumbai-1152906/dineout" target="_blank" class="pbadge"><div class="pb-logo">🛵</div><div><span class="pb-name">Swiggy Dineout</span><span class="pb-rating">4.6 ★ · 164 reviews</span></div></a>
      <a href="https://www.justdial.com/Mumbai/Mix-Culture-Pizzeria-Opposite-RBL-Bank-Vile-Parle-East/022PXX22-XX22-220128171945-Z5U4_BZDET" target="_blank" class="pbadge"><div class="pb-logo">📍</div><div><span class="pb-name">Justdial</span><span class="pb-rating">4.4 ★ · 370 ratings</span></div></a>
    </div>
    <div style="text-align:center;margin-top:40px;">
      <button onclick="showReviewPopup()" class="btnr" style="border:none;cursor:pointer;font-family:inherit;">✏️ Write a Review</button>
    </div>"""
    content = re.sub(r'    <div class="pbadges rv d1">[\s\S]*?</div>\s*</div>', button_html + "\n  </div>", content, count=1)


# 2. Add Photo Upload input to the Form
old_textarea = '<textarea id="revMessage" name="Message" placeholder="Your review..." required rows="4" style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;resize:none;"></textarea>'
new_photo_and_textarea = """      <label style="font-size:0.85rem;opacity:0.8;margin-bottom:-8px;">Upload a Photo (Optional):</label>
      <input type="file" id="revPhoto" name="Photo" accept="image/*" style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;">
      <textarea id="revMessage" name="Message" placeholder="Your review (Required)" required rows="4" style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;resize:none;"></textarea>"""

if "revPhoto" not in content:
    content = content.replace(old_textarea, new_photo_and_textarea)

# 3. Modify JS to use FormData instead of JSON
old_js = """  fetch("https://formsubmit.co/ajax/mixculturepizzeria@gmail.com", {
    method: "POST",
    headers: { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
    body: JSON.stringify({
        _subject: "New Website Review!",
        Name: name,
        Rating: rating + " Stars",
        Message: msg
    })
  })"""

new_js = """  const formData = new FormData();
  formData.append('_subject', 'New Customer Review!');
  formData.append('Name', name);
  formData.append('Rating', rating + ' Stars');
  formData.append('Message', msg);
  
  const photoInput = document.getElementById('revPhoto');
  if(photoInput.files.length > 0) {
      formData.append('Photo', photoInput.files[0]);
  }

  fetch("https://formsubmit.co/ajax/mixculturepizzeria@gmail.com", {
    method: "POST",
    headers: { 
        'Accept': 'application/json'
    },
    body: formData
  })"""

if "const formData = new FormData();" not in content:
    content = content.replace(old_js, new_js)

# Add enctype to form definition
content = content.replace('<form id="reviewForm" onsubmit="submitReview(event)" style="display:flex;flex-direction:column;gap:12px;">', '<form id="reviewForm" onsubmit="submitReview(event)" enctype="multipart/form-data" style="display:flex;flex-direction:column;gap:12px;">')


with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Review button fixed and FormSubmit FormData logic with photo upload added.")
