Dictionary = {
    'boy' : '{0:<15}{1:<15}'.format('n.','เด็กชาย'),
    'now' : '{0:<15}{1:<15}'.format('adv.','ขณะนี้'),
    'afraid' : '{0:<15}{1:<15}'.format('adj.','กลัว'),
    'go' : '{0:<15}{1:<15}'.format('v.','ไป'),
    'door' : '{0:<15}{1:<15}'.format('n.','ประตู'),
}
i = 5
def menu():
    global Choice 
    print('\nพจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4 ออกจากโปรแกรม')
    Choice = input('input choice : ')

def addword():
    word = input('พิมพ์คำศัพท์    : ')
    types = input('ชนิดของคำศัพพ์(n.,v.,adj.,adv.): ')
    mean = input('ความหมาย    : ')
    Dictionary[word] = '{0:<15}{1:<15}'.format(types,mean)
    print('เพิ่มคำคัพพ์เรียบร้อยแล้ว')

def showwords():
    print('-'*45,'\n       มีคำศัพพ์ทั้งหมด','คำ\n'+'-'*45)
    print('{0: <15}{1: <15}{2: <15}' .format('คำศัพพ์','ประเภท','ความหมาย'))
    for k,v in Dictionary.items():
        print('{0:<15}{1:15}'.format(k,v))

def deleteword():
    remove = input('พิมพ์คำศัพพ์ที่ต้องการลบ : ')
    x = input('ต้องการลบ '+remove+' ใช่หรือไม่ (y/n) :')
    if x == 'y':
        Dictionary.pop(remove)
        print('ลบ'+remove+'เรียบร้อย')
    elif x == 'n':
        print('')
while True:
    menu()
    if Choice == "1":
        addword()
        i +=1
    elif Choice == "2":
        showwords()
    elif Choice == "3":
        deleteword()
        i -=1
    else:
        exitt = input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if exitt == 'y':
            print('ออกจากโปรแกรมเรียบร้อยแล้ว')
            break
        elif exitt == 'n':
            continue