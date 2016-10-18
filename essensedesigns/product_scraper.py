import boto3
from lxml import html
import requests
from elastic import product_creator


def fetch_and_store(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    description = tree.xpath('//*[@id="tabs-description"]/p/text()')[0]
    style = tree.xpath('/html/body/div/article/div[3]/div[1]/span/text()')[0]
    fabric = tree.xpath('//*[@id="tabs-details"]/p[1]/text()[1]')
    detail_options = tree.xpath('//*[@id="tabs-details"]/p[2]/text()')
    fabric_colours = tree.xpath('//*[@id="tabs-details"]/p[3]/text()')
    back = tree.xpath('//*[@id="tabs-details"]/p[4]/text()')[0]
    designer_notes_list = filter(None, tree.xpath('//*[@id="tabs-designer"]/p/text()'))
    designer_notes = ' '.join(designer_notes_list)
    images = tree.xpath('/html/body/div/article/div[2]/img/@data-original')
    designer = tree.xpath('//*[@id="tabs-designer"]/h3[2]/text()')[0]

    product_creator.create_new_dress(
        url,
        description,
        style,
        fabric,
        detail_options,
        fabric_colours,
        back,
        designer_notes,
        designer,
        images
    )

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='essense_products')

while queue.receive_messages(1):
    for message in queue.receive_messages(10):
        print("Processing " + message.body)
        try:
            fetch_and_store(message.body)
        except Exception:
            print("Processing failed for " + message.body + " returning item to the queue")
            continue

        message.delete()

