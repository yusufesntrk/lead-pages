const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const directoryPath = '/Users/yusufesentuerk/lead-pages/docs/grosse-waechter-watter';

// Define all valid pages
const validPages = [
  'index.html',
  'kontakt.html',
  'team.html',
  'leistungen.html',
  'frankreich.html',
  'referenzen.html',
  'impressum.html',
  'datenschutz.html'
];

const issues = [];
const fixes = [];

// Check all HTML files
const files = fs.readdirSync(directoryPath).filter(f => f.endsWith('.html'));

files.forEach(file => {
  const filePath = path.join(directoryPath, file);
  const content = fs.readFileSync(filePath, 'utf8');
  
  try {
    const dom = new JSDOM(content);
    const doc = dom.window.document;
    
    // Test 1: Check all links
    const links = doc.querySelectorAll('a[href]');
    links.forEach(link => {
      const href = link.getAttribute('href');
      
      if (!href) return;
      
      // Skip external links and special protocols
      if (href.startsWith('http') || href.startsWith('mailto:') || href.startsWith('tel:') || href === '#') {
        return;
      }
      
      // Get anchor part
      const [pagePart, anchorPart] = href.split('#');
      const targetPage = pagePart || file;
      
      // Check if target page exists
      if (pagePart && !validPages.includes(targetPage)) {
        issues.push({
          type: 'Missing Page',
          page: file,
          href: href,
          status: 'ERROR'
        });
      }
      
      // Check anchor links
      if (anchorPart && pagePart) {
        const targetContent = fs.readFileSync(path.join(directoryPath, targetPage), 'utf8');
        const targetDom = new JSDOM(targetContent);
        const targetDoc = targetDom.window.document;
        const anchor = targetDoc.getElementById(anchorPart);
        
        if (!anchor) {
          issues.push({
            type: 'Missing Anchor',
            page: file,
            href: href,
            anchor: anchorPart,
            status: 'WARNING'
          });
        } else {
          console.log(`✅ Anchor link OK: ${file} -> ${href}`);
        }
      }
    });
    
    // Test 2: Check external links have target="_blank"
    const externalLinks = doc.querySelectorAll('a[href^="http"]');
    externalLinks.forEach(link => {
      const target = link.getAttribute('target');
      if (target !== '_blank') {
        issues.push({
          type: 'Missing target="_blank"',
          page: file,
          href: link.getAttribute('href'),
          status: 'WARNING'
        });
      }
    });
    
  } catch (e) {
    console.error(`Error parsing ${file}:`, e.message);
  }
});

console.log('\n=== LINK QA REPORT ===\n');
console.log(`Total files checked: ${files.length}`);
console.log(`Total issues found: ${issues.length}\n`);

if (issues.length === 0) {
  console.log('✅ All links are OK!');
} else {
  console.log('Issues found:\n');
  issues.forEach((issue, i) => {
    console.log(`${i+1}. [${issue.status}] ${issue.type}`);
    console.log(`   Page: ${issue.page}`);
    console.log(`   Link: ${issue.href}`);
    if (issue.anchor) console.log(`   Missing anchor: #${issue.anchor}`);
    console.log();
  });
}

// Check navigation consistency
console.log('\n=== NAVIGATION CHECK ===\n');
const navLinks = ['Startseite', 'Leistungen', 'Team', 'Frankreich-Service', 'Kontakt'];
const navCheck = {};

files.forEach(file => {
  const content = fs.readFileSync(path.join(directoryPath, file), 'utf8');
  const dom = new JSDOM(content);
  const nav = dom.window.document.querySelector('.nav');
  
  if (!nav) {
    console.log(`⚠️  No navigation found in ${file}`);
    return;
  }
  
  const navItems = Array.from(nav.querySelectorAll('a')).map(a => a.textContent.trim());
  const navHrefs = Array.from(nav.querySelectorAll('a')).map(a => a.getAttribute('href'));
  
  navItems.forEach((item, i) => {
    if (!navCheck[item]) navCheck[item] = [];
    navCheck[item].push({ file, href: navHrefs[i] });
  });
});

// Check consistency
Object.entries(navCheck).forEach(([item, occurrences]) => {
  const hrefs = [...new Set(occurrences.map(o => o.href))];
  if (hrefs.length > 1) {
    console.log(`⚠️  Inconsistent link for "${item}":`);
    occurrences.forEach(o => console.log(`   ${o.file}: ${o.href}`));
  }
});

console.log('\n✅ Navigation check complete');

