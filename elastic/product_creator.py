from datetime import datetime
from elasticsearch_dsl import DocType, String
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['search-bridalspot-ohifbvwt4q4qxu54lc4uhcjl3m.eu-west-1.es.amazonaws.com:80'])


class Dress(DocType):
    description = String(analyzer='snowball')
    style = String(analyzer='snowball')
    fabric = String(analyzer='snowball')
    detail_options = []
    fabric_colours = []
    back = String(analyzer='snowball')
    designer = String(analyzer='snowball')
    designer_notes = String(analyzer='snowball')
    images = []

    class Meta:
        index = 'dresses'


def create_new_dress(url, description, style, fabric, detail_options, fabric_colours, back, designer_notes, designer, images):
    # create the mappings in elasticsearch
    Dress.init()

    # create and save and dress
    dress = Dress(
        meta={'id': url},
        description=description,
        style=style,
        fabric=fabric,
        detail_options=detail_options,
        fabric_colours=fabric_colours,
        back=back,
        designer=designer,
        designer_notes=designer_notes,
        images=images
    )
    dress.save()
