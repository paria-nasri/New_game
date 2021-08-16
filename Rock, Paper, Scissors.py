import random
while True:
    pc=random.randint(1,3)
    man = int(input(' Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n'))
    
    while (man >3 or man <1):
        man = int(input(' Enter valid number: choice \n 1. Rock \n 2. paper \n 3. scissor \n'))
        
        
    while pc == man:
        pc=random.randint(1,3)

    if man ==1:
        man_choice_name='rock'
    if man ==2:
        man_choice_name='paper'
    else:
        man_choice_name='rock'
        
    if pc == 1:
        comp_choice_name = 'Rock'
    elif pc == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print('your choice is : ',man_choice_name)    
    print('pc choice is : ',comp_choice_name)
    
    if(pc ==1 and man==2) or (pc==2 and man==1):
        print('paper wins')
        result='paper'
    elif(pc==2 and man==3) or (pc==3 and man ==2):
        print('scissors wins')
        result='scissors'
    else:
        print('rock wins')
        result='rock'

    if result == man_choice_name:
        print('man won')

    else:
        print('pc won')

    ans=input('wanna carry on?\t')

    if (ans =='n' or ans=='no' ):
        print('thanks for choosing this game')
        break
 



