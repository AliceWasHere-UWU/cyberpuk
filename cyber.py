import random

#char creation - background
print('choose your background', '1. corpo','2 streetkid',' normad')
background = input()
if background == '1' or 'corpo':
    print('selected corpo')
    start = 'corpo'
elif backgound == '2' or 'streetkid':
    print('selcted corpo')
    start = 'streetkid'
elif background == '3' or 'normad':
    print('selected normad')
    start = 'normad'
elif background == '77':
    print('samuri')
    background = random.randint(1,3)
    if background == '1' or 'corpo':
        start = 'corpo'
    elif backgound == '2' or 'streetkid':
        start = 'streetkid'
    elif background == '3' or 'normad':
        start = 'normad'


#char creation - stats
temp1 = random.randint(1,20)
temp2 = random.randint(1,20)
temp3 = random.randint(1,20)
tmep4 = random.randint(1,20)
temp5 = random.randint(1,20)
temp6 = random.randint(1,20)

print('where would you like the',temp1,'points?', '1 body', '2 reflexes', '3 technical ability', '4 intelligence', '6 cool')
decision = input
if decision == '1' or 'body':
    print(temp1, ' points added to body')
    body = temp1 
