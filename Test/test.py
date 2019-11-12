import re

text = '123'
pattern = re.compile(r'(\d+)')
m = pattern.search(text)
print(m.group())
print(len(m.group()))
