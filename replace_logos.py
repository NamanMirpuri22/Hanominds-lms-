import os
import glob
import re

template_dir = r"c:\Users\aalla kavya\Downloads\hanolms\templates"

for filepath in glob.glob(os.path.join(template_dir, "*.html")):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read {filepath}: {e}")
        continue
    
    new_content = content
    
    # 1. Update .sb-logo blocks
    pattern_sb = r'(<div class="sb-logo">\s*)<div class="sb-logo-icon">.*?</div>\s*<div class="sb-logo-text">.*?</div>'
    replacement_sb = r'\1<img src="{{ url_for(\'static\', filename=\'images/logo.png\') }}" alt="Hanominds Logo" style="max-width: 90%; height: auto; max-height: 60px; display: block; margin: 0 auto;">'
    new_content = re.sub(pattern_sb, replacement_sb, new_content, flags=re.DOTALL)
    
    # 2. Update .logo-section (in login.html)
    pattern_login = r'(<div class="logo-section">\s*)<div class="logo-icon">.*?</div>\s*<div class="logo-text">.*?</div>'
    replacement_login = r'\1<img src="{{ url_for(\'static\', filename=\'images/logo.png\') }}" alt="Hanominds Logo" style="max-width: 300px; height: auto; margin-bottom: 15px;">\n                <br>'
    new_content = re.sub(pattern_login, replacement_login, new_content, flags=re.DOTALL)
    
    # 3. Update footer logo (in footer.html)
    pattern_footer = r'(<div class="footer-logo">\s*)<span class="logo-icon">.*?</span>\s*<h3>.*?</h3>'
    replacement_footer = r'\1<img src="{{ url_for(\'static\', filename=\'images/logo.png\') }}" alt="Hanominds Logo" style="max-width: 250px; height: auto; margin-bottom: 5px;">'
    new_content = re.sub(pattern_footer, replacement_footer, new_content, flags=re.DOTALL)
    
    if new_content != content:
        print(f"Updated {os.path.basename(filepath)}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
