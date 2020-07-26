#Email address text scraper

import re

text = 'random string. My_name1-2-3@website.com . some more random text. Your_Name7-7-7@company.net'

pattern = re.compile("[a-zA-z0-9\_\.\-]+\@[a-zA-z0-9]+\.[a-zA-z]+")

result = pattern.findall(text)
print(result)