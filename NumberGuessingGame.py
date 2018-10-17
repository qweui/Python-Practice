import random
import time

print ('嗨，歡迎來到猜數字遊戲，你有五次機會可以嘗試。')
print (" ")
number = random.randint(1, 101)
guess = int(input('猜一個數字(1~100): '))
taken = 0


while taken < 4:
    if guess < number:
        print ('你還有' + str(4-taken) + '次機會')
        guess = int(input('猜一個大一點的數字: '))
        print ('')
        
    elif guess > number:
        print ('你還有' + str(4-taken) + '次機會')
        guess = int(input('猜一個小一點的數字: '))
        print ('')
        
    elif guess == number:
        break
        
    taken += 1
    
    
if guess == number:
    print ('好棒! 你花了' + str(1 + taken) + '次機會就猜對了。')
    
else:
    print ('抱歉，機會用完了，正確數字是：' + str(number) + '。')
    

time.sleep(3)
