import re

pattern = '^([-+]?\d+(?:\.\d*)?)\s*([CF])?$'

match = '0'

match = input('try to validate a temperature:\n')

while match is not '#':
    m = re.match(pattern, match, flags=re.IGNORECASE)
    if m:
        print('pass, and class is {}'.format(m.group(2)))
    else:
        print('invalid')
    match = input('try to validate a temperature:\n')