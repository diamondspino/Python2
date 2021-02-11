print("-----แนะนำตัว-----")
print('*'*20)
class yourname :
    def __init__(self,firstname,lastname,gender,year,department,city) :
        self.firstname = firstname 
        self.lastname = lastname
        self.gender = gender
        self.year = year
        self.department = department
        self.city = city
    
    def showyour(self) :
        print('*'*10,"แนะนำตัว",'*'*10)
        print("ชื่อ : ",self.firstname)
        print("สกุล : ",self.lastname)
        print("เพศ : ",self.gender)
        print("ชั้นปี : ",self.year)
        print("สาขาวิชา : ",self.department)
        print("เมืองที่อยู่ : ",self.city)

firstname = input("ชื่อ :")
lastname = input("สกุล :")
gender = input("เพศ :")
year = input("ชั้นปี :")
department = input("สาขาวิชา :")
city = input("เมืองที่อยู่:")
x = yourname(firstname,lastname,gender,year,department,city)
x.showyour()
