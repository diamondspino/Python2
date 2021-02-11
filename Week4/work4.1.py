import os
choice = 0
listcom = [0,0,0,0,0,]
pick = 0
def menu():
    global choice
    print('\tโปรแกรมร้านเเต่งคอม\n','1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ : ')
    screen_clear()

def showmenu(): 
    print('\tรายการสินค้าร้านแต่งคอม')
    print('\t1.จอภาพ 500 บาท\n','\t2.เคส 450 บาท\n','\t3.แรม 600 บาท\n','\t4.ซีพียู 700 บาท\n','\t5.คีย์บอร์ด 300 บาท')

def pickmenu():
    global pick
    print('\tรายการสินค้า\n 1.จอภาพล\n 2.เคส\n 3.เเรม\n 4.ซีพียู\n 5.คีย์บอร์ด')
    pick = int(input('เลือกหยิบสินค้าหมายเลข :'))
    if pick == 1:
        listcom[0] += 1
    elif pick == 2:
        listcom[1] += 1
    elif pick == 3:
        listcom[2] += 1
    elif pick == 4:
        listcom[3] += 1
    elif pick == 5:
        listcom[4] += 1
    screen_clear()

def showuserpick():
    list_score = ['จอภาพล','เคส','เเรม','ซีพียู','คีย์บอร์ด']
    list_price = [355,460,565,755,950]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(list_score[i],list_price[i],listcom[i],listcom[i]*list_price[i]))

def deletuserpick():
    print('\t\nรายการสินค้า\n 1.จอภาพล\n 2.เคส\n 3.เเรม\n 4.ซีพียู\n 5.คีย์บอร์ด')
    depick = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if depick == 1:
        listcom[0] -= 1
    elif depick == 2:
        listcom[1] -= 1
    elif depick == 3:
        listcom[2] -= 1
    elif depick == 4:
        listcom[3] -= 1
    elif depick == 5:
        listcom[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        showmenu()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showuserpick()
    elif choice == '4':
        deletuserpick()
        screen_clear()
    elif choice == '5':
        c = input('ต้องการใช้โปรแกรมต่อหรือไม่ y/n: ')
        if c.lower() == 'n':
            screen_clear()
        elif c.lower() == 'y':
            screen_clear()
            break