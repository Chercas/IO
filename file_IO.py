# jabber = open('sample.txt', 'r')
#
# for line in jabber:
#     if 'jabberwock' in line.lower():
#         print(line, end='')
#
# jabber.close()
with open('sample.txt', 'r') as jabber:
    for line in jabber:
        if 'JAB' in line.upper():
            print(line, end='')
