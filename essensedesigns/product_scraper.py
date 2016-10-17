from lxml import html
import requests


def fetch_product_info(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    description = tree.xpath('//*[@id="tabs-description"]/p/text()')[0]
    style = tree.xpath('/html/body/div/article/div[3]/div[1]/span/text()')[0]
    fabric = tree.xpath('//*[@id="tabs-details"]/p[1]/text()[1]')
    detail_options = tree.xpath('//*[@id="tabs-details"]/p[2]/text()')
    fabric_colours = tree.xpath('//*[@id="tabs-details"]/p[3]/text()')
    back = tree.xpath('//*[@id="tabs-details"]/p[4]/text()')[0]
    designer_notes = tree.xpath('//*[@id="tabs-designer"]/p/text()')
    images = tree.xpath('/html/body/div/article/div[2]/img/@data-original')
    designer = tree.xpath('//*[@id="tabs-designer"]/h3[2]/text()')[0]

    print


fetch_product_info('https://www.essensedesigns.com/essense-of-australia/wedding-dresses/d2027/')



