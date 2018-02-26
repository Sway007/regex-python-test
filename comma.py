import re

txt = input('give me an integer: ')
pattern = r'(?<=\d)(?=(\d{3})+(?!\d))'
p = re.compile(pattern)
print(p.sub(',', txt))