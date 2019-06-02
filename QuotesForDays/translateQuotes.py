import requests
import smtplib
import random
import configparser

config = configparser.ConfigParser()
config_file = config.read("config.ini")
api_key = config.get("default", "api_key")
user_config = config.get("default", "user_config")

email_user = config.get("default", "email_user")
email_password = config.get("default", "email_password")
phone_number = config.get("default", "phone_number")
domain = 'mms.att.net'

# ToDo: Prepend language to translated object
# ToDo: Create Quote class for all functions
# ToDo: Create getters and setters to override defaults
# ToDo: Setup timer so that each user receives one update per 24 hours --> allow users to select which hour
# ToDo: Create configuration file and classes to drive the code

"""
This script will pull a random quote, translate it to any language (Spanish by default) and then send
it as a text message to the user
"""
# Prepare to pull the quote by pre-selecting a category and creating API request
def preparequote():
    categories = ["inspire", "management", "sports", "life", "funny", "love", "art", "students"]
    category = random.choice(categories)
    endpoint = "http://quotes.rest/qod.json?"
    quote_request = "{}category={}".format(endpoint, category)
    return quote_request

# Send API request and extract the quote and author
def getquote(quote_request):
    response = requests.get(quote_request).json()
    quote = response['contents']['quotes'][0]['quote']
    author = response['contents']['quotes'][0]['author']
    return quote

# Prepare the API call for the translation for each language
def preparetranslation(translatetext, languages=['es'], api_key=api_key):
    api_requests = []
    for elem in languages:
        api_request = "https://translation.googleapis.com/language/translate/" \
                      "v2?target={}&key={}={}".format(elem, api_key, translatetext)
        api_requests.append(api_request)
#        language = elem
    return api_requests


# Send each request and receive translation responses to store in one object
def gettranslation(api_requests, quote, languages=['es']):
    translations = ["English: \"{}\" ".format(quote)]
    x = 0
    for elem in api_requests:
        response = requests.post(elem).json()
        translation = response['data']['translations'][0]
        translatedtext = translation['translatedText']
        sourceLanguage = translation['detectedSourceLanguage']
 #       preparedtext = "English: \"{}\" \n Spanish: \"{}\" ".format(translatedtext, translatedtext)
        preparedtext = "{}: \"{}\" ".format(languages[x], translatedtext)
        x += 1
        translations.append(preparedtext)
    translations = '\n \n'.join(translations)
    return translations

# Prepare text message with the original quote and it's translations
def preparetext(translations, quote, phone_number=phone_number, domain=domain):
    sender = 'Mike'
    to = ['{}@{}'.format(phone_number, domain)]
    subject = "Daily Translation"
    text = translations
    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sender, ", ".join(to), subject, text)
    return message, sender, to

# Send the text message using SMTP
def sendtext(message, sender, to, email_user=email_user, email_password=email_password, phone_num=phone_number):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, email_password)
#    phone_num = phone_num.split(' ')
#    for nums in phone_num:
    server.sendmail(sender, to, message.encode('utf8'))
    server.quit()

# EXPERIMENTAL -- Sends email/text .. likely won't use it
def sendemail(to, sender, message):
    from email.message import  EmailMessage
    em = EmailMessage()
    em.set_content(format(to, sender, message))
    em['To'] = to
    em['From'] = sender
    em['Subject'] = 'test'

def timer(hr):
    return hr

