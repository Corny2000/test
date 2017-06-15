# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import lxml.html
from lxml import etree
from lxml.etree import tostring
from datetime import datetime
import scraperwiki
import StringIO
#
# # Read in a page
house_html = scraperwiki.scrape("https://www.spareroom.co.uk")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")
house_parser = etree.HTMLParser()
house_tree = etree.parse(StringIO.StringIO(house_html), house_parser)
#    house_text = house_tree.xpath('string(//div[@class="propertyDetailDescription"])')
    # Only look at houses with the word 'views' in the ad text. 
house = {}
house['yes'] = 'no'
#stopped_phrase = None
        # Check for stop phrases
#        title = house_tree.xpath('string(//h1[@id="propertytype"])')

#        image_url = tostring(house_tree.xpath('//img[@id="mainphoto"]')[0])
#        price = house_tree.xpath('string(//div[@id="amount"])')
#        nearby_stations = house_tree.xpath('string(//div[@id="nearbystations"]/div)')
#        ns = nearby_stations.split("(")
#        distance = ns[-1].replace(")","")
#        distance = ' '.join(distance.split()).strip()
#        if float(distance.replace(" miles",""))>1.5:
#            return False
#        map_img = house_tree.xpath('//a[@id="minimapwrapper"]/img')
#        if map_img:
#            map_img = tostring(house_tree.xpath('//a[@id="minimapwrapper"]/img')[0])
#        else:
#            map_img = ''
#        house['title'] = "%s - %s, %s, %s from station" % (title, town, price, distance)
        #print 'HOUSE FOUND! %s, %s ' % (house['title'], HOUSE_URL)
#        item_text = '<a href="' + HOUSE_URL + '">' + image_url + '</a>'
        #item_text += '<div style="position:relative;">'
#        item_text += '<a href="' + HOUSE_URL + '">' + map_img + '</a>'
        #item_text += '<img id="googlemapicon" src="http://www.rightmove.co.uk/ps/images11074/maps/icons/rmpin.png"'
        #item_text += ' style="position:absolute;top:100px;left:100px;alt="Property location" /></div>'
#        item_text += house_text
#        item_text = item_text.replace("views","<span style='font-weight:bold;color:red;'>views</span>")
#        house['description'] = item_text.replace("fireplace","<span style='font-weight:bold;color:red;'>fireplace</span>")
#        if stopped_phrase:
#            house['stop'] = stopped_phrase
#        else:
#            house['stop'] = ''
#        house['link'] = HOUSE_URL
#        house['pubDate'] = datetime.now()
#scraperwiki.sqlite.save(['link'], house)

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
