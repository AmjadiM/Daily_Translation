import random
import requests

class Quote():

    def __init__(self, cat):
        self.cat = cat

    def prepare(self):
        categories = ["inspire", "management", "sports", "life", "funny", "love", "art", "students"]
        category = random.choice(categories)
        endpoint = "http://quotes.rest/qod.json?"
        quote_request = "{}category={}".format(endpoint, category)
        return quote_request

    def getquote(self, quote_request):
        response = requests.get(quote_request).json()
        quote = response['contents']['quotes'][0]['quote']
        author = response['contents']['quotes'][0]['author']
        return quote
