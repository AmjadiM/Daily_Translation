

class Translate:
    def __init__(self, languages):
        self.languages = languages

    def preparetranslation(self, translatetext, languages=['es'], api_key=api_key):
        api_requests = []
        for elem in languages:
            api_request = "https://translation.googleapis.com/language/translate/" \
                          "v2?target={}&key={}={}".format(elem, api_key, translatetext)
            api_requests.append(api_request)
        #        language = elem
        return api_requests
