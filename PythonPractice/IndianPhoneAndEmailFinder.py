#!python3

import re, pyperclip

#TODO : Create a regex for Phone Numbers

phoneRegex =  re.compile(r'''
# 918888888888, 8989898989

(
((\d\d)|(\(\d\d\)))?     #area code (optional)
\d\d\d\d\d\d\d\d\d\d        #last 10 digits
)
''', re.VERBOSE)

#TODO : Create a regex for Email Addresses

emailRegex  =  re.compile(r'''
# some.+_thing@(\d{2,9}))?.com

[a-zA-Z0-9_.+]+      #NamePart
@                    # @ symbol
[a-zA-Z0-9_.+]+      # domain name part

''', re.VERBOSE)

#TODO : Get text off the clipboard

text = pyperclip.paste()
#TODO : Extract all the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print (extractedPhone)
print (extractedEmail)

allPhoneNumbers =[]
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
#TODO : Copy the extracted email/phone to a clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
