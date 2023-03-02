#เกมสุ่มตัวเลข
import random
import time

target = 72
minnumber = 0
maxnumber = 100

for num in range(1, maxnumber+1):
    print("เลือกเลข 1-100:")
    randomnumber = int(input(""))
    if num >= 100:
        print("คุณแพ้. เดาครบ 100 ครั้งแล้ว!!")
        break
    if randomnumber > maxnumber or randomnumber < minnumber:
        print("ตัวเลขที่เดาเกินครอบเขตของตัวเลข โปรดเลือกเลข 1-100!")
    elif randomnumber < target:
        print("ตัวเลขที่เดาต่ำเกินไป ลองที่สูงกว่านี้!!")
    elif randomnumber > target:
        print("ตัวเลขที่เดาสูงเกินไป ลองที่ต่ำกว่านี้")
    else:
        print("ยินดีด้วยคุณเดาถูก จำนวนครั้งที่เดาทั้งหมดคือ  " + str(num) + "!\n")
        break


time.sleep(1)

#เกมโบวลิ่ง
maxround = 10
maxscore = 10
totalscore = 0
maxbowling = 2

for x in range(1, maxround+1):
    score = 0
    round = 0
    leftscore = 10
    print("รอบ " + str(x) + ":")
    for z in range(1, maxbowling+1):
        rand = random.randint(0, leftscore)
        round += 1
        score += rand
        print("ลูกที่ " + str(z) + " คะแนน: " + str(rand))
        if score >= maxscore and round == 1:
            print("Strike!, เป็นการยิงที่เยี่ยมมาก!")
            score = 10
            break
        elif score >= maxscore and round == 2:
            print("Spare!, เป็นการยิงที่เยี่ยมมาก!")
            score = 10
        elif score < 10 and round == 2:
            print("Open Frame!, เป็นการยิงที่เยี่ยมมาก!")
        totalscore += rand
        leftscore -= rand
    print("รอบที่ " + str(x) + " คะแนนทั้งหมด: " + str(score) + "!\n")

print("คะแนนรวมของคุณทั้งหมดคือ" + str(totalscore) + "!")

        
            

