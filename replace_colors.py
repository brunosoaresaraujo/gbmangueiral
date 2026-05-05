import re

with open('styleguide.html', 'r') as f:
    content = f.read()

# Replace hardcoded RGBA values
content = content.replace('249,115,22', '200,16,46')
content = content.replace('253,186,116', '232,26,59') # lighter red
content = content.replace('59,130,246', '200,16,46') # blue to red for glitch

# Replace variable names
content = content.replace('--orange-light', '--primary-light')
content = content.replace('--orange-deep', '--primary-dark')
content = content.replace('--orange', '--primary')
content = content.replace('--peach', '--primary-light')
content = content.replace('--border-o', '--border-p')

# Update :root
root_old = """    :root {
      /* Core Backgrounds */
      --bg-0: #08080A;
      --bg-1: #0C0C10;
      --bg-2: #111118;
      
      /* Primary Brand (Orange/Peach) */
      --primary: #F97316;
      --primary-light: #FB923C;
      --primary-light: #FDBA74;
      --primary-dark: #EA580C;
      
      /* Accents */
      --blue: #3B82F6;
      --emerald: #10b981;
      --red: #ef4444;
      
      /* Typography */
      --text: #f0f0f2;
      --muted: #8a8a96;
      
      /* UI Elements */
      --glass: rgba(255,255,255,0.03);
      --border-p: rgba(200,16,46,0.15);
      --border-s: rgba(255,255,255,0.06);
    }"""

root_new = """    :root {
      /* Core Backgrounds */
      --bg-0: #0F0F0F;
      --bg-1: #2B2B2B;
      --bg-2: #1A1A1A;
      
      /* Primary Brand (Gracie Barra Red) */
      --primary: #C8102E;
      --primary-light: #E81A3B;
      --primary-dark: #A00B23;
      
      /* Accents */
      --blue: #3B82F6;
      --emerald: #10b981;
      --red: #C8102E;
      
      /* Typography */
      --text: #FFFFFF;
      --muted: #6B6B6B;
      
      /* UI Elements */
      --glass: rgba(255,255,255,0.03);
      --border-p: rgba(200,16,46,0.25);
      --border-s: rgba(229, 229, 229, 0.15);
      --grey-light: #E5E5E5;
    }"""

content = content.replace(root_old, root_new)

# Update HTML Color Section
html_colors_old = """    <div class="color-grid stagger-up reveal">
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-bg0"></div>
        <div class="color-info">
          <div class="color-name">Background 0</div>
          <div class="color-hex">#08080A</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-bg1"></div>
        <div class="color-info">
          <div class="color-name">Background 1</div>
          <div class="color-hex">#0C0C10</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-muted"></div>
        <div class="color-info">
          <div class="color-name">Text Muted</div>
          <div class="color-hex">#8A8A96</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-primary"></div>
        <div class="color-info">
          <div class="color-name">Brand Primary</div>
          <div class="color-hex">#F97316</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-primary-light"></div>
        <div class="color-info">
          <div class="color-name">Brand Light</div>
          <div class="color-hex">#FB923C</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-primary-light"></div>
        <div class="color-info">
          <div class="color-name">Brand Peach (Gradients)</div>
          <div class="color-hex">#FDBA74</div>
        </div>
      </div>
    </div>"""

html_colors_new = """    <div class="color-grid stagger-up reveal">
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-bg0"></div>
        <div class="color-info">
          <div class="color-name">Background 0 (Preto)</div>
          <div class="color-hex">#0F0F0F</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-bg1"></div>
        <div class="color-info">
          <div class="color-name">Background 1 (Cinza Escuro)</div>
          <div class="color-hex">#2B2B2B</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-muted"></div>
        <div class="color-info">
          <div class="color-name">Muted (Cinza Médio)</div>
          <div class="color-hex">#6B6B6B</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch" style="background: var(--grey-light);"></div>
        <div class="color-info">
          <div class="color-name">Borders (Cinza Claro)</div>
          <div class="color-hex">#E5E5E5</div>
        </div>
      </div>
      <div class="color-card reveal-child">
        <div class="color-swatch swatch-primary"></div>
        <div class="color-info">
          <div class="color-name">GB Red (Primária)</div>
          <div class="color-hex">#C8102E</div>
        </div>
      </div>
    </div>"""

# Ensure the colors section gets properly updated by finding a smaller chunk if needed
content = re.sub(r'<div class="color-grid stagger-up reveal">.*?</div>\s*</section>', html_colors_new + '\n  </section>', content, flags=re.DOTALL)


# Also need to fix CSS classes that were hardcoded
content = content.replace('.swatch-orange', '.swatch-primary')
content = content.replace('.swatch-orange-light', '.swatch-primary-light')
content = content.replace('.swatch-peach', '.swatch-primary-light')

with open('styleguide.html', 'w') as f:
    f.write(content)

print("Done replacing.")
