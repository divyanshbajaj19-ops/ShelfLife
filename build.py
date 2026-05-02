import os
import re
import shutil

base_dir = r"c:\Users\divya\OneDrive\Desktop\ShelfLife"
out_dir = os.path.join(base_dir, "ShelfLifeWebsite")

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

pages = {
    "home_shelf_life": "index.html",
    "about_us_shelf_life": "about.html",
    "contact_shelf_life": "contact.html",
    "dashboard_shelf_life": "dashboard.html",
    "features_shelf_life": "features.html",
    "pricing_shelf_life": "pricing.html",
}

for folder, out_file in pages.items():
    code_path = os.path.join(base_dir, folder, "code.html")
    if not os.path.exists(code_path):
        print(f"Skipping {folder}, code.html not found.")
        continue
    
    with open(code_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace nav links
    content = re.sub(r'href="[^"]*"([^>]*>Home</a>)', r'href="index.html"\1', content, flags=re.IGNORECASE)
    content = re.sub(r'href="[^"]*"([^>]*>Features</a>)', r'href="features.html"\1', content, flags=re.IGNORECASE)
    content = re.sub(r'href="[^"]*"([^>]*>Pricing</a>)', r'href="pricing.html"\1', content, flags=re.IGNORECASE)
    content = re.sub(r'href="[^"]*"([^>]*>About</a>)', r'href="about.html"\1', content, flags=re.IGNORECASE)
    content = re.sub(r'href="[^"]*"([^>]*>Contact</a>)', r'href="contact.html"\1', content, flags=re.IGNORECASE)

    # Link the brand logo text to home
    content = re.sub(r'(<div[^>]*>)\s*Shelf-Life\s*(</div>)', r'\1<a href="index.html" class="hover:opacity-80 transition-opacity">Shelf-Life</a>\2', content)

    # Buttons
    content = re.sub(r'(<button[^>]*>\s*Login\s*</button>)', r'<a href="dashboard.html">\1</a>', content, flags=re.IGNORECASE)
    content = re.sub(r'(<button[^>]*>\s*Sign Up\s*</button>)', r'<a href="dashboard.html">\1</a>', content, flags=re.IGNORECASE)

    # Footer links
    content = re.sub(r'href="[^"]*"([^>]*>About Us</a>)', r'href="about.html"\1', content, flags=re.IGNORECASE)

    out_path = os.path.join(out_dir, out_file)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Generated {out_file}")

print("Build complete.")
