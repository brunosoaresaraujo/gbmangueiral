const fs = require('fs');

const htmlPath = '/Users/brunos.araujo/Documents/projetos-bsaux/gbmangueiral/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');

// Regex to match a time slot block
const timeSlotRegex = /<div class="time-slot">[\s\S]*?<div class="slot-header"><span class="slot-time">(.*?)<\/span><\/div>[\s\S]*?<div class="slot-class-box">\s*<span class="slot-class">(.*?)<\/span>\s*<\/div>[\s\S]*?<span class="slot-prof"><iconify-icon icon="lucide:user"><\/iconify-icon> (.*?)<\/span>[\s\S]*?<\/div>[\s\S]*?<iconify-icon icon=".*?" class="slot-bg-icon"><\/iconify-icon>\s*<\/div>/g;

html = html.replace(timeSlotRegex, (match, time, className, profName) => {
  return `<div class="time-slot">
            <div class="slot-top">
              <span class="slot-time">${time}</span>
              <div class="slot-divider"></div>
              <span class="slot-class">${className}</span>
            </div>
            <span class="slot-prof">${profName}</span>
          </div>`;
});

fs.writeFileSync(htmlPath, html);
console.log('Refactoring complete.');
