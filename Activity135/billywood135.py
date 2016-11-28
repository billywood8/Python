def how_eligible(essay):
    punctuation=  0
    if '?' in str(essay):
        punctuation= punctuation+ 1
    if '"' in str(essay):
        punctuation= punctuation + 1
    if ',' in str(essay):
        punctuation= punctuation + 1
    if '!' in str(essay):
        punctuation= punctuation+ 1
    print (punctuation)