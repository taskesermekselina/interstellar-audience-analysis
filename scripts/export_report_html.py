import os
import re
import base64

def md_to_html(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Embed Images (Base64)
    def replace_image(match):
        alt = match.group(1)
        img_filename = match.group(2)
        # Assume images are in the same dir as the md file
        img_path = os.path.join(os.path.dirname(md_path), img_filename)
        
        if os.path.exists(img_path):
            with open(img_path, "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                ext = os.path.splitext(img_filename)[1][1:]
                return f'<img src="data:image/{ext};base64,{b64_string}" alt="{alt}" style="max-width:100%; border-radius: 8px; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">'
        else:
            return f'<div style="color:red">[Image not found: {img_filename}]</div>'

    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_image, content)

    # 2. Basic Markdown Conversion
    html_lines = []
    in_list = False
    in_table = False
    
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        
        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1 style="color:#2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px;">{line[2:]}</h1>')
            continue
        if line.startswith('## '):
            html_lines.append(f'<h2 style="color:#34495e; margin-top: 30px;">{line[3:]}</h2>')
            continue
        if line.startswith('### '):
            html_lines.append(f'<h3 style="color:#7f8c8d;">{line[4:]}</h3>')
            continue
            
        # Lists
        if line.startswith('* ') or line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            # Bold processing inside list items
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line[2:])
            html_lines.append(f'<li style="margin-bottom: 5px;">{item_text}</li>')
            continue
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False

        # Tables
        if line.startswith('|'):
            if not in_table:
                html_lines.append('<table style="border-collapse: collapse; width: 100%; margin: 20px 0; font-size: 14px;">')
                in_table = True
            
            row_html = '<tr>'
            cells = [c.strip() for c in line.split('|') if c]
            
            # Check if it's a separator line
            if '---' in line:
                continue

            for cell in cells:
                # Basic Bold check
                cell = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', cell)
                # Link check
                cell = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', cell)
                
                style = "border: 1px solid #ddd; padding: 12px; text-align: left;"
                if 'Video Başlığı' in line or 'Link' in line: # Header heuristic
                     style += " background-color: #f2f2f2; font-weight: bold;"
                
                row_html += f'<td style="{style}">{cell}</td>'
            
            row_html += '</tr>'
            html_lines.append(row_html)
            continue
        else:
            if in_table:
                html_lines.append('</table>')
                in_table = False

        # Paragraphs & Bold
        if line:
            # Separator
            if line == '---':
                html_lines.append('<hr style="margin: 30px 0; border: 0; border-top: 1px solid #eee;">')
                continue
                
            p_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            # Links
            p_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" style="color: #3498db; text-decoration: none;">\1</a>', p_text)
            
            html_lines.append(f'<p style="line-height: 1.6; color: #333;">{p_text}</p>')

    # Final HTML Wrapper
    final_html = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interstellar Akademik Rapor</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 900px; margin: 0 auto; padding: 40px; background-color: #f9f9f9; }}
            .container {{ background-color: white; padding: 50px; box-shadow: 0 0 20px rgba(0,0,0,0.05); border-radius: 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            {chr(10).join(html_lines)}
        </div>
    </body>
    </html>
    """

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"Exported to {html_path}")

md_source = r'c:\interstellar_audience_analysis\outputs\INTERSTELLAR_AKADEMIK_RAPOR.md'
html_dest = r'c:\interstellar_audience_analysis\outputs\INTERSTELLAR_AKADEMIK_RAPOR_FULL.html'

md_to_html(md_source, html_dest)
