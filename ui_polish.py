import re

html_file = r"c:\Users\algo 11\OneDrive\Desktop\Vatsal\Mix Culture\Mix Culture1\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Modify #about
old_about = "#about{padding:130px 0;background:var(--char2);position:relative;overflow:hidden}"
new_about = "#about{padding:130px 0;background:radial-gradient(circle at right top,rgba(0,138,63,.09) 0%,var(--char2) 65%);position:relative;overflow:hidden}"
content = content.replace(old_about, new_about)

# 2. Modify #reviews
old_reviews = "#reviews{padding:130px 0;background:var(--char3);overflow:hidden}"
new_reviews = "#reviews{padding:130px 0;background:radial-gradient(circle at left center,rgba(0,138,63,.09) 0%,var(--char3) 55%);overflow:hidden;position:relative}"
content = content.replace(old_reviews, new_reviews)

# 3. Modify Gallery Masonry
old_ggrid = """.ggrid{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3, 220px);gap:4px}
.gitem{position:relative;overflow:hidden;cursor:pointer}
.gitem:nth-child(1){grid-column:span 2;grid-row:span 2}
.gitem:nth-child(5){grid-column:span 2}"""

new_ggrid = """.ggrid{column-count:3;column-gap:16px;padding-bottom:10px}
.gitem{position:relative;overflow:hidden;cursor:pointer;margin-bottom:16px;break-inside:avoid;border-radius:10px;transform:translateZ(0);background:var(--char)}
/* Enforce auto height */
.gitem img{border-radius:10px;width:100%;height:auto;object-fit:cover;display:block}"""

content = content.replace(old_ggrid, new_ggrid)


with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("UI enhancements complete.")
