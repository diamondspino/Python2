print('ป้อนชื่ออาหารสุดโปรดของคุณหรือ exit เพื่อออกจากโปรแกรม')
num =1
b = []
f1 = " "
c = 1
while f1 != 'exit' :
    f1 = input('อาหารโปรดอันดับที่ :' +str(num)+ " คือ\t") 
    b.append(f1)
    num+= 1
b.pop()

print('อาหารสุดโปรดของคุณมีดังนี้',end='')
for i in b :
    print(str(c)+"."+i+" ",end='')
    c+=1