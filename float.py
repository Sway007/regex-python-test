import re 

pattern = '(\.\d{3}[1-9]?)\d*'
p = re.compile(pattern)

txt = input('give me a float: ')
sub = p.search(txt).group(1)

if sub:
    print(re.sub(pattern, sub, txt))
else:
    print('invalid')