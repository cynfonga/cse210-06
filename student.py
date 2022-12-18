class Student:

    def _init (self,rollno,name,age):
        self.rollno=rollno
        self.name=name
        self.age=age


    def display(self):
        print (self.rollno, end='\t\t') 
        print(self.name,end='\t\t')   
        print(self.age)

print ('student details entry...')
rollno = input('\tRollno: ') 
name= input('\tName:') 
age = int(input('\tAge:'))  
st=Student(rollno,name,age)  
print('student information')
print('Rollno\t\tName\t\tAge')
st.display()