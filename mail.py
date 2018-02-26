import re


pSubject = re.compile('^Subject: (.*)', flags=re.IGNORECASE)
pDate = re.compile('^Date: (.*)', flags=re.IGNORECASE)
pReply = re.compile('^Reply: (.*)', flags=re.IGNORECASE)
pFrom = re.compile('^From: (\S+)\s\(([^()]*)\)', flags=re.IGNORECASE)
pContent = re.compile('^\w+[^:]\s')

addr = date = reply = subject = from_name = ''

mail_contents = []

f = open('email')
for line in f.readlines():
    objSubject = pSubject.match(line)
    if objSubject:
        subject = objSubject.group(1)

    objDate = pDate.match(line)
    if objDate:
        date = objDate.group(1)

    objReply = pReply.match(line)
    if objReply:
        reply = objReply.group(1)

    objFrom = pFrom.match(line)
    if objFrom:
        addr = objFrom.group(1)
        from_name = objFrom.group(2)

    objContent = pContent.match(line)
    if objContent:
        mail_contents.append('|> ' + line)

f = open('email-2', 'w')
f.write('''To: {addr} {name}
From: Sway007
Subject: Re: {subject}

On {date} {fromRname} wrote:
'''
.format(addr=addr, name=from_name, subject=subject, date=date, 
fromRname=from_name))
for extra in mail_contents[1:]:
    f.write(extra)