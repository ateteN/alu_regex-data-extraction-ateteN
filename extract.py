# To allow regular expressions
import re

# defining our functions to extract the data we want. 
#defined the function email_found to match emails
def email_found(text):
    # The regex expression for matching our emails
    regex_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    # we use re.findall to match every pattern
    return re.findall(regex_email, text)

def phone_number_found(text):
    regex_phone_number = r"\+?\d{0,2}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{3,4}"
    return re.findall(regex_phone_number, text)

def hashtag_found(text):
    regex_hashtag = r"#\w+"
    return re.findall(regex_hashtag, text)

def currencies_found(text):
    regex_currency = r"\$\s?\d+(?:,\d{3})*(?:\.\d{2})?"
    return re.findall(regex_currency, text)

def url_found(text):
    regex_url = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?"
    return re.findall(regex_url, text)

# Now the text containing the data we want to extract
text = "Welcome to NewLife Academy. If you need more information please contact us at newlifeacademy@co.uk, if you need further guidance on your next application steps, call at 250 789 399 976 for further guidance, or you can also call 250-757-3453, our internation office for immigration inquiries. Please make sure to follow our social medias and mention us with the #NewLifeAcademy and #welcometotheundergrads. If you want to know more about the campus life, visit our website at https://www.newlife.com and don't be shy to leave a message for us as well! Be sure to send your application fee of just $345 for local students, and $600 for international students!"

# The extracted values that we need
emails = email_found(text)
phone_number = phone_number_found(text)
hashtag = hashtag_found(text)
currency = currencies_found(text)
url = url_found(text)

# Now the print function to view our matched data
print("Emails:")
for email in emails:
    print(f"{email}")
print("\nPhone Numbers:")
for phone in phone_number:
    print(f"{phone}")
print("\nHashtags:")
for hashtag in hashtag:
    print(f"{hashtag}")
print("\nCurrencies:")
for currency in currency:
    print(f"{currency}")
print("\nURL:")
for url in url:
    print(f"{url}")
