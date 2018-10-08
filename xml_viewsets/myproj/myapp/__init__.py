class CoinsFromXML(object):
    def __init__(self, _id, name, website, exchange_id):
        self._id = _id
        self.name = name
        self.website = website
        self.exchange_id = exchange_id


# have to change lines 44-47 in get_xml.py if using the class below 
# class CoinsFromXML(object):
#     def __init__(self, **kwargs):
#         for field in ('id', 'name', 'website', 'exchange_id'):
#             setattr(self, field, kwargs.get(field, None))
        