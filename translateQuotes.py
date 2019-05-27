import requests
import smtplib
import random
import configparser

config = configparser.ConfigParser()
config_file = config.read("config.ini")
api_key = config.get("default", "api_key")
email_user = config.get("default", "email_user")
email_password = config.get("default", "email_user")
phone_number = config.get("default", "phone_number")



def preparequote():
    categories = ["inspire", "management", "sports", "life", "funny", "love", "art", "students"]
    category = random.choice(categories)
    endpoint = "http://quotes.rest/qod.json?"
    quote_request = "{}category={}".format(endpoint, category)
    return quote_request


def getquote(quote_request):
    response = requests.get(quote_request).json()
    quote = response['contents']['quotes'][0]['quote']
    author = response['contents']['quotes'][0]['author']
    return quote


def preparetranslation(translatetext, languages=['es'], api_key=api_key):
    api_requests = []
    for elem in languages:
        api_request = "https://translation.googleapis.com/language/translate/" \
                      "v2?target={}&key={}={}".format(elem, api_key, translatetext)
        api_requests.append(api_request)
    return api_requests


def gettranslation(api_requests, quote):
    translations = ["English: \"{}\" ".format(quote)]

    for elem in api_requests:
        response = requests.post(elem).json()
        translation = response['data']['translations'][0]
        translatedtext = translation['translatedText']
        sourceLanguage = translation['detectedSourceLanguage']
 #       preparedtext = "English: \"{}\" \n Spanish: \"{}\" ".format(translatedtext, translatedtext)
        preparedtext = "{}: \"{}\" ".format(sourceLanguage, translatedtext)
        translations.append(preparedtext)
    translations = ' '.join(translations)
    return translations


def preparetext(translations, quote, phone_number):
    sender = 'Mike'
    to = ['{}@mms.att.net'.format(phone_number)]
    subject = "Daily Translation"
    text = translations
    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sender, ", ".join(to), subject, text)
    return message, sender, to


def sendtext(message, sender, to, email_user, email_password):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(sender, to, message.encode('utf8'))
    server.quit()

def sendemail(to, sender, message):
    from email.message import  EmailMessage
    em = EmailMessage()
    em.set_content(format(to, sender, message))
    em['To'] = to
    em['From'] = sender
    em['Subject'] = 'test'






# quote = (request.json())['quote']
# subprocess.call('espeak ' + quote, shell=True)
