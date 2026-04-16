import os
import glob

template_dir = r"c:\Users\aalla kavya\Downloads\hanolms\templates"

for filepath in glob.glob(os.path.join(template_dir, "*.html")):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        pass
    
    new_content = content.replace(r"url_for(\'static\', filename=\'images/logo.png\')", "url_for('static', filename='images/logo.png')")
    new_content = new_content.replace(r"url_for(\"static\", filename=\"images/logo.png\")", "url_for('static', filename='images/logo.png')")

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
