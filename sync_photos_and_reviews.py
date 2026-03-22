import re

html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace Images in #dishes and #gallery
replacements = {
    # Dishes Images (w1000-rw, w800-rw)
    "https://lh3.googleusercontent.com/3p51G4r0J4NxFoW6Pd50cqoNyietV1LZyY5TzT3kDTwhNVxJ09FYMW4Th6rErBohLrbFRhbzR0jOzzUHOcmoVXWfONGGfAa5w1D_22sy=w1000-rw": "Mix Culture Food Photos/Ultimate Sicilian Pizza.jpg",
    "https://lh3.googleusercontent.com/yeqcabLpUMn_3JRvOfzFJtI_vfN0cJuiHJKeygTBtcL7-LkaUYomYqSzMmwHtSU_BJtAxVSJZyl3J9evFFDAQfq_IKUvJRBo09HJzzHRsw=w800-rw": "Mix Culture Food Photos/Tandoori Paneer.jpg",
    "https://lh3.googleusercontent.com/2BdCFFAnIxt03OGXuSbF5BeupTv7r4UNfk2Ryj0Eb6Uu143Gl182a7FjZzrXNiNb-mNVUY42yI9WqQFyRERHgDFzaZk23Uc31I9mGMWq=w800-rw": "Mix Culture Food Photos/Queen Margherita New York Pizza.jpg",
    "https://lh3.googleusercontent.com/oFZXMTXhB402vhWCojopbZcKG0c6QWwvNCmeT2amMZzBmmroroDIHd-wRJ711RFMV-e2hMicjFvuYxX6WCoXF-PHv3-1Lzk0PSIxQMqI1w=w800-rw": "Mix Culture Food Photos/Pesto Truffle Temptation Greek Pizza [10 Inches].jpg",
    "https://lh3.googleusercontent.com/ZC_kXfU4TiVhCBuRe2gne3WaZ28JXpQTaR3nggk8uHbOyWE2hKok4Bn2cwmhwYIfWso08Sxr1Km12Xg3kPUaUVU9wQhmGfAb2YVaxMpIPA=w800-rw": "Mix Culture Food Photos/Spicy Mushroom Neapolitan Pizza.jpg",

    # Gallery Images (w1200-rw, w600-rw)
    "https://lh3.googleusercontent.com/EWHitCxFHQ3-TkB8WAOPOzfdOTz7T67CUgjy28T2l77Iq_-3Ie8VIvwrPHT1fax_Q-wq-LGhhL4PFZm6RwtQTIKMfzY7603tJDar_-Y=w1200-rw": "Mix Culture Food Photos/Fresh Mozzarella Neapolitan Pizza.jpg",
    "https://lh3.googleusercontent.com/3p51G4r0J4NxFoW6Pd50cqoNyietV1LZyY5TzT3kDTwhNVxJ09FYMW4Th6rErBohLrbFRhbzR0jOzzUHOcmoVXWfONGGfAa5w1D_22sy=w600-rw": "Mix Culture Food Photos/The Loaded Legend.jpg",
    "https://lh3.googleusercontent.com/DmhMQnbhrV-sxr47r8vhF4CkVTZvJ0uxkVG4ELIqRirpKOgadTG8jB8r9B_isL0nwfTgYLRvmf4BCoKDwpCeDiSiUvYGLpQYcC-dcWdp9g=w600-rw": "Mix Culture Food Photos/Double Chocolate Lava Cake.jpg",
    "https://lh3.googleusercontent.com/yeqcabLpUMn_3JRvOfzFJtI_vfN0cJuiHJKeygTBtcL7-LkaUYomYqSzMmwHtSU_BJtAxVSJZyl3J9evFFDAQfq_IKUvJRBo09HJzzHRsw=w600-rw": "Mix Culture Food Photos/Fully Loaded Garlic Bread (Bun).jpg",
    "https://lh3.googleusercontent.com/2BdCFFAnIxt03OGXuSbF5BeupTv7r4UNfk2Ryj0Eb6Uu143Gl182a7FjZzrXNiNb-mNVUY42yI9WqQFyRERHgDFzaZk23Uc31I9mGMWq=w600-rw": "Mix Culture Food Photos/Spicy Barbeque St Louis Pizza.jpg",
    "https://lh3.googleusercontent.com/oFZXMTXhB402vhWCojopbZcKG0c6QWwvNCmeT2amMZzBmmroroDIHd-wRJ711RFMV-e2hMicjFvuYxX6WCoXF-PHv3-1Lzk0PSIxQMqI1w=w600-rw": "Mix Culture Food Photos/Al Pesto Pasta [Basil Sauce].jpg",
    "https://lh3.googleusercontent.com/ZC_kXfU4TiVhCBuRe2gne3WaZ28JXpQTaR3nggk8uHbOyWE2hKok4Bn2cwmhwYIfWso08Sxr1Km12Xg3kPUaUVU9wQhmGfAb2YVaxMpIPA=w600-rw": "Mix Culture Food Photos/Tandoori Paneer Kulhad Small.jpg",
}

for old_url, new_url in replacements.items():
    content = content.replace(old_url, new_url)

# 2. Add Review Button
review_btn_html = """
    </div>
    <div style="text-align:center;margin-top:40px;">
      <button onclick="showReviewPopup()" class="btnr" style="border:none;cursor:pointer;font-family:inherit;">✏️ Write a Review</button>
    </div>
  </div>
</section>
"""
content = content.replace('    </div>\n  </div>\n</section>', review_btn_html, 1)

# 3. Add #rev-popup CSS
css_res_popup = "#res-popup.show .pbox{transform:none}"
css_rev_popup = css_res_popup + """
#rev-popup{position:fixed;inset:0;z-index:999;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.82);backdrop-filter:blur(14px);opacity:0;pointer-events:none;transition:opacity .4s}
#rev-popup.show{opacity:1;pointer-events:all}
#rev-popup.show .pbox{transform:none}
"""
content = content.replace(css_res_popup, css_rev_popup)

# 4. Add #rev-popup HTML before <script>
rev_modal = """
<!-- REVIEW POPUP -->
<div id="rev-popup" onclick="if(event.target===this)hideReviewPopup()">
  <div class="pbox">
    <button class="px" onclick="hideReviewPopup()">×</button>
    <div class="pico">⭐</div>
    <h3 class="ptitle">Write a Review</h3>
    <p class="psub">Tell us about your experience. Great reviews might be featured on our site!</p>
    
    <form id="reviewForm" onsubmit="submitReview(event)" style="display:flex;flex-direction:column;gap:12px;">
      <input type="text" id="revName" name="Name" placeholder="Your Name" required style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;">
      
      <select id="revRating" name="Rating" required style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;appearance:none;">
        <option value="" disabled selected>Select Rating (1-5 Stars)</option>
        <option value="5">5 ★★★★★ - Excellent!</option>
        <option value="4">4 ★★★★☆ - Very Good</option>
        <option value="3">3 ★★★☆☆ - Average</option>
        <option value="2">2 ★★☆☆☆ - Poor</option>
        <option value="1">1 ★☆☆☆☆ - Terrible</option>
      </select>
      
      <textarea id="revMessage" name="Message" placeholder="Your review..." required rows="4" style="padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-family:inherit;resize:none;"></textarea>
      
      <button type="submit" id="revSubmitBtn" style="background:var(--gold);color:var(--char);font-weight:bold;padding:14px;border:none;cursor:pointer;margin-top:10px;font-family:inherit;">Submit Review</button>
    </form>
  </div>
</div>
"""
content = content.replace("<script>", rev_modal + "\n<script>")

# 5. Add JS functions for rev-popup
js_res_popup = "function hideResPopup(){document.getElementById('res-popup').classList.remove('show')}"
js_rev_popup = js_res_popup + """
function showReviewPopup(){document.getElementById('rev-popup').classList.add('show')}
function hideReviewPopup(){document.getElementById('rev-popup').classList.remove('show')}

function submitReview(e) {
  e.preventDefault();
  const btn = document.getElementById('revSubmitBtn');
  btn.innerText = 'Submitting...';
  
  const name = document.getElementById('revName').value;
  const rating = parseInt(document.getElementById('revRating').value);
  const msg = document.getElementById('revMessage').value;
  
  fetch("https://formsubmit.co/ajax/mixculturepizzeria@gmail.com", {
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
  })
  .then(response => response.json())
  .then(data => {
    if(rating >= 4.0) {
      let starsHtml = '★'.repeat(rating) + '☆'.repeat(5-rating);
      let newCard = `<div class="rcard"><div class="rstars">${starsHtml}</div><p class="rtext">${msg}</p><div class="rauthor">${name} · Verified Review</div></div>`;
      document.querySelector('.rtrack').insertAdjacentHTML('afterbegin', newCard);
    }
    
    btn.innerText = 'Thanks for your Review!';
    setTimeout(() => {
      hideReviewPopup();
      document.getElementById('reviewForm').reset();
      btn.innerText = 'Submit Review';
    }, 2000);
  })
  .catch(error => {
    btn.innerText = 'Sorry, try again.';
    setTimeout(() => { btn.innerText = 'Submit Review'; }, 2000);
  });
}
"""
content = content.replace(js_res_popup, js_rev_popup)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Images replaced and Review System added successfully.")
