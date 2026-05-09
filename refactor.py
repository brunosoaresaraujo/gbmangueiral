import re

html_path = '/Users/brunos.araujo/Documents/projetos-bsaux/gbmangueiral/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Regex to match a time slot block
time_slot_regex = re.compile(r'<div class="time-slot">\s*<div class="slot-header"><span class="slot-time">(.*?)</span></div>\s*<div class="slot-info">\s*<div class="slot-class-box">\s*<span class="slot-class">(.*?)</span>\s*</div>\s*<span class="slot-prof"><iconify-icon icon="lucide:user"></iconify-icon>\s*(.*?)</span>\s*</div>\s*<iconify-icon icon=".*?" class="slot-bg-icon"></iconify-icon>\s*</div>', re.DOTALL)

def replace_slot(match):
    time = match.group(1)
    className = match.group(2)
    profName = match.group(3)
    return f"""<div class="time-slot">
            <div class="slot-top">
              <span class="slot-time">{time}</span>
              <div class="slot-divider"></div>
              <span class="slot-class">{className}</span>
            </div>
            <span class="slot-prof">{profName}</span>
          </div>"""

html_replaced = time_slot_regex.sub(replace_slot, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_replaced)

print('Refactoring complete.')
