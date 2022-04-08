# Practical work 6: pickled management system
- Copy your pw5 directory into pw6 directory
- Upgrade the persistence feature of your system to use pickle instead, still with compression
- Push your work to corresponding forked [Github repository](https://github.com/quanganh2001/pp2022)

```py
import pickle
```
```py
class Input:
    def __init__(self, stName="", stId="", stDob="", courses=""):
        self.stName = stName
        self.stId = stId
        self.stDob = stDob
        self.courses = courses
        self.student_list = []
    
    def inputSt(self, name, stId, stDob, courses):
        st = Input(name, stId, stDob, courses)
        self.student_list.append(st)
    
    def pickleCompress(self, nameFile):
        list_files = ['students.txt','courses.txt','marks.txt']

        pickle_file = open(nameFile, 'ab')
        pickle.dump(list_files, pickle_file)
    
    def pickleDecompress(self):
        with open('students.dat', 'rb') as f:
            data = pickle.load(f)
            print(data)
    
    def writeFile(self, st):
        for i in st:
            with open("students.txt", "a+") as f1:
                f1.write("Name: " +i.stName+'\n')
                f1.write("ID: " +i.stId+'\n')
                f1.write("Date of birth: " +i.stDob+'\n')

            with open("courses.txt", "a+") as f2:
                f2.write("Name: " +i.stName+'\n')
                for j in i.courses:
                    f2.write("Course: "+j[0]+'\n')
            
            with open("marks.txt", "a+") as f3:
                f3.write("Name: "+i.stName+'\n')
                for j in i.courses:
                    f3.write(f'{j[0]}:'+j[1]+'\n')
        f1.close()
        f2.close()
        f3.close()
    
    def deleteSt(self, name):
        for i in range(len(self.student_list)):
            if name == self.student_list[i].stName:
                print(f'student {name} is deleted')
                del self.student_list[i]
```
```py
class Output:
  def __init__(self, student_list=''):
    self.student_list = student_list
  
  def listSt(self, student_list):
    for i in student_list:
      print(f"Name: {i.stName}")
      print(f"Id: {i.stId}")
      print(f"Date Of Birth: {i.stDob}")
      for j in range(len(i.courses)):
        print(f"Marks of {i.courses[j][0]}: ", i.courses[j][1])
      print("*************************")
```
```py
st = Input('' ,'', '' ,  0)
st.inputSt('Nguyen Quang Anh', 'BA10-002', '27/10/2001', (('Operating System', '10.5'), ('French Language', '13.1'), ('Numerical Methods', '6.5')))
st.inputSt('Nguyen Thi Khanh Huyen', 'BA10-025', '25/09/2001', (('Operating System', '14.0'), ('French Language', '16.5'), ('Numerical Methods', '8.0')))
st.inputSt('Nguyen Van Tai', 'BA10-055', '21/04/2001', (('Operating System', '19.0'), ('French Language', '18.0'), ('Numerical Methods', '18.3')))
```
```py
# Upgrade the persistence feature of your system to use pickle instead, still with compression
st.pickleCompress('students.dat')
st.pickleDecompress()
```
This will be create `students.dat` file