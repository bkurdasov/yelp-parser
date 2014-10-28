import requests
from lxml.html import fromstring
import csv

LINKSFILENAME='links.txt'
DATAFILENAME='result.csv'
with open(LINKSFILENAME) as linksfile:
    total_links=sum(1 for _ in linksfile)
print "Total %s links" % total_links
with open(LINKSFILENAME) as linksfile, open(DATAFILENAME,'wb') as resultfile:
    writer=csv.writer(resultfile)
    writer.writerow(['Name','Group','Address','City','State','Zip','Neighborhood','Phone','Website'])
    for line_num,line in enumerate(linksfile):
        print "Processing link %4s of %4s ..." % (line_num,total_links),
        url=line.strip()
        r=requests.get(url)
        doc=fromstring(r.text)
        name=doc.xpath('//h1[@itemprop="name"]/text()')[0].strip()
        group=doc.xpath('//span[@class="category-str-list"]/a/text()')[0].strip()
        address=' '.join(doc.xpath('//span[@itemprop="streetAddress"]/text()'))
        city=doc.xpath('//span[@itemprop="addressLocality"]/text()')[0].strip()
        state=doc.xpath('//span[@itemprop="addressRegion"]/text()')[0].strip()
        zipcode=doc.xpath('//span[@itemprop="postalCode"]/text()')[0].strip()
        neighborhood=doc.xpath('//span[@class="neighborhood-str-list"]/text()')[0].strip()
        phone=doc.xpath('//span[@class="biz-phone"]/text()')[0].strip()
        website=doc.xpath('//div[@class="biz-website"]/a/text()')[0].strip()
        #print name,group,address,city,state,zipcode,neighborhood,phone,website
        writer.writerow((name,group,address,city,state,zipcode,neighborhood,phone,website))
        print "done."
print "All done."