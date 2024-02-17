
from termcolor import colored, cprint
day=0
from termcolor import colored, cprint

import random
money=0
meat=0
hp=0
damage=0
while hp!=-1:
    print('Тeкущий день %s'%(day))
    cprint(f'Деньги {money}','light_yellow') 
    cprint(f'Здоровье {hp} ','green')
    cprint(f'Мясо {meat}','light_red')
    cprint(f'урон {damage}','blue')
    sms=int(input('Что будешь делать?(1-охота 2-поеть 3-поспать 4-Продать мясо (если есть мясо)'))
    if sms==1:
        print('Вы упешно по охотились')
        day+=1
        meat+=1
    else:
        if sms==2: 
            print('Вы поели')
            hp+=1
        else:
            if sms==3:
                print('Вы поспали') 
                day+=1
                meat+=1
            else:
                if sms==4:
                    print('Вы продали мясо ') 
                    money+=1000
                    meat-=1
                    day+=0.5
                else:
                    if sms==5:
                        print ('Вы купили меч ')
                        damage+=10
                        money-=1000
                            

    