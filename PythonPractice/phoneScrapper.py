#!python3

import re, pyperclip

#TODO : Create a regex for Phone Numbers

phoneRegex =  re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?     #area code (optional)
(\s|-)        #first seperatior
\d\d\d       #First 3 Digits
-       #Separator
\d\d\d\d        #last 4 digits
(((ext(\.)?\s) |x) #extension word part (optional)
(\d{2,5}))?   )    #extension number part (optional)
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

allPhoneNumbers =[]
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
#TODO : Copy the extracted email/phone to a clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
