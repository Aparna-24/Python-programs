punctuation= "!@#$%^&*():;{}[]+-_=/*-+?><,./~`"
str=" hello!!! mr.patrick ??"
no_punc=""
for i in str:
    if i not in punctuation:
        no_punc=no_punc+i

print(no_punc)