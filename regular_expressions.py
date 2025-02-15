# To allow regular expressions
import re
# then we write the regular expressions for the firls we want to match:
# regular expression for e-mails
emails_regex = r"\w+@\w+[a-zA-Z]"
# regular expression for hashtags
hashtags_regex = r"#\w"
# regular expression for phone numbers
phonenumbers_regex = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{3,4})"
# regular expression for currencies
currency_regex = r"\$\s?\d{1,3}(,\d{3})*(\.\d{2})?"
# regular expression for urls
url_regex = r"https://[a-zA-Z0-9]+\.[a-zA-Z]{1,3}"

def matched_data(field, text):
    return re.findall(field, text)

# Now we add the texts that we want to match
texts = {
    "emails" : [
        "akezadivine@gmail.com",
        "uwamwezijohana@gmail.com",
        "Niyonkuru-gabin.com",
        "@Janemuhizigmail"
    ],
    "hashtags" : [
        "#BlackLivesMatter",
        "#Fashionweek",
        "BringBackShame"
    ],
    "phone_numbers" : [
        "(250)-789-3997",
        "250-757-3453",
        "250 789 399 976",
        "078 939 9976",
        "338.99-467"
    ],
    "currencies" : [
        "$56.7",
        "$100,999,999.99",
        "RWF30,000",
        "29.876"
    ],
    "url" : [
        "hhtps://www.google.com",
        "https://www.google.com",
        "https:/ww.anyone.123"
    ]
}


# now we write the function to help us find our matches
def matches(field, texts, regex):
    # we define the match function first
    print(f"\n{field}: ")
    # first shows the field we are analyzing
    for item in texts:
        # goes through items in text
        find_match = matched_data(regex, item)
        # finds the match between the regex pattern and the item
        print(f"{item} = {'correct' if find_match else 'False'}")

# Now we run our functions

matches("emails", texts["emails"], emails_regex) 
matches("hashtags", texts["hashtags"], hashtags_regex) 
matches("phone numbers", texts["phone_numbers"], phonenumbers_regex)
matches("currencies", texts["currencies"], currency_regex)  
matches("url", texts["url"], url_regex) 


