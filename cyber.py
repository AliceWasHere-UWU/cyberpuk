# add a tallie if it doesnt work 0
#when i wrote this only me and god knew how it works but now only he does


import random

#char creation - background
print('choose your background', '1. corpo','2 streetkid',' normad')
background = input()
if background == '1' or 'corpo':
    print('selected corpo')
    start = 'corpo'
elif background == '2' or 'streetkid':
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
    elif background == '2' or 'streetkid':
        start = 'streetkid'
    elif background == '3' or 'normad':
        start = 'normad'


#char creation - stats
temp1 = random.randint(1,20)
temp2 = random.randint(1,20)
temp3 = random.randint(1,20)
temp4 = random.randint(1,20)
temp5 = random.randint(1,20)

print('where would you like the',temp1,'points?', '1 body', '2 reflexes', '3 technical ability', '4 intelligence', '6 cool')
decision = input()
if decision == '1' or 'body':
    print(temp1, ' points added to body')
    body = temp1
elif decision == '2' or 'reflexes':
    print(temp1, ' points added to reflexes')
    reflexes = temp1
elif decision == '3' or 'technical ability':
    print(temp1, ' points added to technical ability')
    technical = temp1
elif decision == '4' or 'intelligence':
    print(temp1, ' points added to intelligence')
    intelligence = temp1
elif decision == '5' or 'cool':
    print(temp1, ' points added to cool')
    cool = temp1

print('where would you like the',temp2, 'points?','1 body', '2 reflexes', '3 technical ability', '4 intelligence', '6 cool')
decision = input()
if decision == '1' or 'body':
    print(temp2, ' points added to body')
    body = temp2
elif decision == '2' or 'reflexes':
    print(temp2, ' points added to reflexes')
    reflexes = temp2
elif decision == '3' or 'technical ability':
    print(temp2, ' points added to technical ability')
    technical = temp2
elif decision == '4' or 'intelligence':
    print(temp2, ' points added to intelligence')
    intelligence = temp2
elif decision == '5' or 'cool':
    print(temp2, ' points added to cool')
    cool = temp2

print('where would you like the',temp3)
decision = input()

if decision == '1' or 'body':
    print(temp3, ' points added to body')
    body = temp3
elif decision == '2' or 'reflexes':
    print(temp3, ' points added to reflexes')
    reflexes = temp3
elif decision == '3' or 'technical ability':
    print(temp3, ' points added to technical ability')
    technical = temp3
elif decision == '4' or 'intelligence':
    print(temp3, ' points added to intelligence')
    intelligence = temp3
elif decision == '5' or 'cool':
    print(temp3, ' points added to cool')
    cool = temp3

print("where would you like",temp4, "points?", '1 body', '2 reflexes', '3 technical ability', '4 intelligence', '6 cool')
decision = input()
if decision == '1' or 'body':
    print(temp4, ' points added to body')
    body = temp4
elif decision == '2' or 'reflexes':
    print(temp4, ' points added to reflexes')
    reflexes = temp4
elif decision == '3' or 'technical ability':
    print(temp4, ' points added to technical ability')
    technical = temp4
elif decision == '4' or 'intelligence':
    print(temp4, ' points added to intelligence')
    intelligence = temp4
elif decision == '5' or 'cool':
    print(temp4, ' points added to cool')
    cool = temp4

print('where would you like',temp5, 'points?','1 body', '2 reflexes', '3 technical ability', '4 intelligence', '6 cool')
decision = input()
if decision == '1' or 'body':
    print(temp5, ' points added to body')
    body = temp5
elif decision == '2' or 'reflexes':
    print(temp5, ' points added to reflexes')
    reflexes = temp5
elif decision == '3' or 'technical ability':
    print(temp5, ' points added to technical ability')
    technical = temp5
elif decision == '4' or 'intelligence':
    print(temp5, ' points added to intelligence')
    intelligence = temp5
elif decision == '5' or 'cool':
    print(temp5, ' points added to cool')
    cool = temp5

print('your stats are body:', body,"reflexes:" ,reflexes,"technical ability:" ,technical,"intelligence:" ,intelligence,"cool;" ,cool)

#extra info 
print('choose your name')
name = input()
print('choose your gender')
gender = input()
if gender == 'male':
    print('male selected')
    pronouns = 'he'
elif gender == 'female':
    print('female selected')
    pronouns = 'she'
else:
    print('other selected')
    pronouns = 'they'


print('night city used to be a beutiful city where people from all over the world would come to see but now it has fallen into gangs,drugs, and homelessness all caused by the megacorpos ')

#intro corpo 
if start == 'corpo':
    print('you are a corpo agent working for arasaka')
    print('you are at your desk filing all the paperwork befire you when you hear the lockdown alarm')
    print('what do you do?', '1 hide under your desk', '2 run to the nearest exit 3 call your boss')
    decision = input()
    if decision == '1' or 'hide under your desk':
        print('you hide under the desk waiting for the lockdown to end ')
        print('after 5 minutes, you hear all the moniters around you start to play all the attrocoties that they have done')
        print('what do you do?', '1 run to the nearest exit', '2 stay under your desk')
        decision = input()
        if decision == '1' or 'run to the nearest exit':
            print('you run to the nearest exit but the door is locked')
            print('what do you do?', '1 break the door down', '2 call your boss')
            decision = input()
            if decision == '1' or 'break the door down':
                print('you break the door down and run out into the street')
                print('after 2 minutes of running you turn around and the araska tower blows up')
                print('you feel a hand on your shoulder and look back to see a stranger in some ragged clothes ')
                if gender == 'female':
                    print('you alright miss?')
                elif gender == 'male':
                    print('you alright bud?')
                else:
                    print('you alright?')
                print('what do you do?', '1 yea im fine ','2 no im hurt')
                decision = input()
                if decision == '1' or 'yea im fine':
                    print('what the fuck happed')
                    print('what do you do?', '1 say i dont know', '2 tell them what you saw')
                    decision = input()
                    if decision == '1' or 'i dont know':
                        print('shame im oli by the way lets go get a drink')
                        print('you and oli go to a bar and talk for hours ')
                        print('two arasaka agents come up to you and ask if you want to work for them')
                        print('what do you do?', '1 yes', '2 no')
                        decision = input()
                        if decision == '1' or 'yes':
                            print('state your id number')
                            print('what do you do?', '1 say it', '2 dont say it')
                            decision = input()
                            if decision == '1' or 'say it':
                                print('just the one we needed')
                                print(name, 'what do you know about the attack?')
                                print('what do you do?', '1 tell them everything', '2 tell them nothing')
                                decision = input()
                                if decision == '1' or 'tell them everything':
                                    print('you tell them everything you know about the attack')
                                    print('you are off the network and you are no longer an arasaka employee')
                                    print('you feel all of your arasaka biomods shut down you fall to the grounds in pain')
                                    print(' the two agents walk out of the bar as oli picks you back up "yo choom you good?')
                                    print('what do you do?', '1. i cant breath saka turned off my biomods', '2. been better')
                                    decision = input()
                                    if decision == '1' or 'i cant breath saka turned off my biomods':
                                        print('oli helps you up "how about we get some revenge')
                                        exit() 
                                elif decision == '2 or 'tell them nothing':
                                    print('hiding something are we?')
                                    print('the agents grab you and you feel your biomods shutting down')
                                    print('you are off the network and you are no longer an arasaka employee')
                                    print('you fall to the ground in pain as the agents walk out of the bar')
                                    print('"yo good choom?" asks oli')
                                    