import os
name_list = ['ข้าวมันไก่หน้าเป็ด','ข้าวหมูแดงทอดกรอบ','ข้าวขาหมูโลกันต์','ข้าวเปล่า ไม่เอาไม่เป็นไร']
price_list = [59,39,39,29]
class market :
    def list_def(self):
        for x in range(0,len(name_list)):
            print(x+1,name_list[x],price_list[x],'บาท')
    def choose(self):
        print('***********ครัวไอ่ต้าวสปีโน่***********')
        print('\tแสดงรายการสินค้า[a]\n\tเพิ่มรายการสินค้า[s]\n\tออกจากระบบ[x]')
    def input_choise(self):
        global choise
        choise = input('กรุณาเลือกคำสั่ง :\t')
    def add_list(self):
        while True:
            print('เพิ่มรายการสินค้า หากต้องการ กรอก exit')
            add_name = input('เพิ่มชื่อสินค้า :')
            if add_name == 'exit':
                break
            else : 
                add_price = input('เพิ่มราคาสินค้า :')
                name_list.append(add_name)
                price_list.append(add_price)
            add = input ('ต้องการเพิ่มสินค้าอีกหรือไม่ [y/n] :')
            if add == 'n' :
                break
            elif add == 'y' :
                os.system('cls')

while True:
    x = market()
    x.choose()
    x.input_choise()
    if choise == 'a' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        x.list_def()
    if choise == 's' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        x.add_list()
    if choise == 'x' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        close = input('ต้องการปิดโปรแกรมหรือไม่ [y/n] : ')
        if close == 'n' :
            os.system('cls')
        if close == 'y' :
            os.system('cls')
            print('ปิดโปรแกรม')
            break