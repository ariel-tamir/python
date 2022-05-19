import urllib.request
from bs4 import BeautifulSoup
from lxml import etree

html = urllib.request.urlopen('https://www.ynet.co.il/home/0,7340,L-8,00.html').read()
soup = BeautifulSoup(html, 'html.parser')
dom = etree.HTML(str(soup))
findings = dom.xpath('/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/a/span')
for finding in findings:
    print(finding.text)