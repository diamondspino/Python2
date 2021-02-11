import datetime
now = datetime.datetime.now()
name_s = []
pts_s = []
time_s = []
ht = []
def menu():
    for i in range(num):
        name = input('ป้อนชื่อ :')
        pts = float(input('คะแนน :'))
        time = float(input('ระยะเวลาที่ใช้ :'))
        ht.append(pts/time)
        name_s.append(name)
        pts_s.append(pts)
        time_s.append(time)
    for i in range(num):
        j = i
        for j in range(num):
            if ht[i] > ht[j]:
                a,b,c,d = ht[i],name_s[i],pts_s[i],time_s[i]
                ht[i],name_s[i],pts_s[i],time_s[i] = ht[j],name_s[j],pts_s[j],time_s[j]
                ht[j],name_s[j],pts_s[j],time_s[j] = a,b,c,d

def show():
    print('Shotgun sumday training 2021')
    print('Condition : 1')
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print('{0: <10}{1: <10}{2: <10}{3: <18}{4: <15}{6: <10}'.format('No.','PTS','TIME','COMETITER#Name','HIT FACTOR','STATE POINS','STATE PERCENT'))
    for i in range(num):
        SPS = ht[i]/ht[0]*50
        SPT = SPS/(ht[0]/ht[0]*50)*100
        print('{0: <10}{1: <10}{2: <10}{3: <18}{4: <15}{4: <15}{5: <15}{6: <10}'.format(i+1,int(pts_s[i]),'%.2f'%time_s[i],name_s[i],'%.4f'%ht[i],'%.4f'%SPS,'%.2f'%SPT))

num = int(input("จำนวนคนยิง"))
menu()
show()