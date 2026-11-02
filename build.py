import re
from ebooklib import epub
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

p = 'C:/Users/hops1/AppData/Local/hermes/profiles/madeline/cache/scratch/alchemist-aurelius/story.md'
text = open(p, encoding='utf-8').read()

# ---- EPUB ----
book = epub.EpubBook()
book.set_identifier('alchemist-aurelius')
book.set_title('The Alchemist, Aurelius')
book.set_language('en')
book.add_author('Hermes')

# split into chapters by "### " or "## "
chapters = re.split(r'(?=^#{2,3} )', text, flags=re.M)
body = ''
for ch in chapters:
    if not ch.strip():
        continue
    lines = ch.strip().splitlines()
    title = lines[0].lstrip('#').strip() if lines else 'Chapter'
    html = '<h1>' + title + '</h1>'
    for ln in lines[1:]:
        if ln.strip() == '':
            html += '<br/>'
        else:
            html += '<p>' + ln.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;') + '</p>'
    c = epub.EpubHtml(title=title, file_name='chap_' + str(hash(ch)) + '.xhtml', lang='en')
    c.content = html
    book.add_item(c)
    body += html

book.toc = (epub.Link('nav.xhtml', 'Table of Contents', 'nav'),)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
epub.write_epub('C:/Users/hops1/AppData/Local/hermes/profiles/madeline/cache/scratch/alchemist-aurelius/story.epub', book)
print('epub done')

# ---- PDF ----
doc = SimpleDocTemplate('C:/Users/hops1/AppData/Local/hermes/profiles/madeline/cache/scratch/alchemist-aurelius/story.pdf', pagesize=letter)
styles = getSampleStyleSheet()
flow = []
for ln in text.splitlines():
    if ln.strip() == '':
        flow.append(Spacer(1, 8))
    else:
        flow.append(Paragraph(ln.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'), styles['BodyText']))
doc.build(flow)
print('pdf done')