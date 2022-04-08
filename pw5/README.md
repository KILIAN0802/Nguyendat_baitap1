# Practical work 5: persistent info
- Update your input functions
  - Write student info to `students.txt` after finishing input
  - Write course info to `courses.txt` after finishing input
  - Write marks to `marks.txt` after finishing input
- Before closing your program
  - Select a compression method
  - Compress all files aboves into students.dat
- Upon starting your program,
  - Check if `students.dat` exists
  - If yes, decompress and load data from it
- Push your work to corresponding forked [Github repository](https://github.com/quanganh2001/pp2022)

## Import zipfile
```py
import zipfile
import sys
import codecs
```
## Write info students mark management after finishing input
```py
# Write info students mark management after finishing input
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
  
  def compress(self, nameFile):
    list_files = ['students.txt', 'courses.txt', 'marks.txt']

    compression = zipfile.ZIP_DEFLATED
    z = zipfile.ZipFile(nameFile, mode="w")

    for file in list_files:
      z.write(file, file, compress_type=compression)
    z.close()
  
  def decompress(self):
    try:
      with zipfile.ZipFile("students.dat", "r") as zip_ref:
        zip_ref.extractall("decompress")
    except Exception as e:
      print("students.dat not found")
      print("error :",e)
  
  def writeFile(self, st):
    for i in st:
      with open("students.txt", "a+", encoding='utf-8') as f1:
        f1.write("Name: "+i.stName+'\n')
        f1.write("ID: "+i.stId+'\n')
        f1.write("Date of birth: "+i.stDob+'\n')
        f1.write("----------------------------\n")
      
      with open('courses.txt', 'a+', encoding='utf-8') as f2:
        f2.write('Name: '+i.stName+'\n')
        for j in i.courses:
          f2.write('Courses: '+j[0]+'\n')
          f2.write('-------------------\n')
      
      with open('marks.txt', 'a+', encoding='utf-8') as f3:
        f3.write('Name: '+i.stName+'\n')
        for j in i.courses:
          f3.write(f'{j[0]}:'+j[1]+'\n')
          f3.write('------------------\n')
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
## Input student info, course info and marks info
```py
# Input student info, course info and marks info
st = Input('' ,'', '' ,  0)
st.inputSt('Nguyen Quang Anh', 'BA10-002', '27/10/2001', (('Operating System', '10.5'), ('French Language', '13.1'), ('Numerical Methods', '6.5')))
st.inputSt('Nguyen Thi Khanh Huyen', 'BA10-025', '25/09/2001', (('Operating System', '14.0'), ('French Language', '16.5'), ('Numerical Methods', '8.0')))
st.inputSt('Nguyen Van Tai', 'BA10-055', '21/04/2001', (('Operating System', '19.0'), ('French Language', '18.0'), ('Numerical Methods', '18.3')))
```
## Export to txt files
```py
# Export to txt files
st.writeFile(st.student_list)
```
The results are:
### students.txt
```txt
Name: Nguyen Quang Anh
ID: BA10-002
Date of birth: 27/10/2001
----------------------------
Name: Nguyen Thi Khanh Huyen
ID: BA10-025
Date of birth: 25/09/2001
----------------------------
Name: Nguyen Van Tai
ID: BA10-055
Date of birth: 21/04/2001
----------------------------

```
### courses.txt
```txt
Name: Nguyen Quang Anh
Courses: Operating System
-------------------
Courses: French Language
-------------------
Courses: Numerical Methods
-------------------
Name: Nguyen Thi Khanh Huyen
Courses: Operating System
-------------------
Courses: French Language
-------------------
Courses: Numerical Methods
-------------------
Name: Nguyen Van Tai
Courses: Operating System
-------------------
Courses: French Language
-------------------
Courses: Numerical Methods
-------------------

```
### marks.txt
```txt
Name: Nguyen Quang Anh
Operating System:10.5
------------------
French Language:13.1
------------------
Numerical Methods:6.5
------------------
Name: Nguyen Thi Khanh Huyen
Operating System:14.0
------------------
French Language:16.5
------------------
Numerical Methods:8.0
------------------
Name: Nguyen Van Tai
Operating System:19.0
------------------
French Language:18.0
------------------
Numerical Methods:18.3
------------------

```
## Compress all files
```py
# - Before closing your program
#   - Select a compression method
#   - Compress all files aboves into students.dat
st.compress('students.dat')
st.decompress()
```
This will create `decompress` folder with these txt files are similarity and `students.dat` file
## Print the persistent info
```py
# Print the output persistent info
display = Output()
display.listSt(st.student_list)
```
The result is:
```txt
Name: Nguyen Quang Anh
Id: BA10-002
Date Of Birth: 27/10/2001
Marks of Operating System:  10.5
Marks of French Language:  13.1
Marks of Numerical Methods:  6.5
*************************
Name: Nguyen Thi Khanh Huyen
Id: BA10-025
Date Of Birth: 25/09/2001
Marks of Operating System:  14.0
Marks of French Language:  16.5
Marks of Numerical Methods:  8.0
*************************
Name: Nguyen Van Tai
Id: BA10-055
Date Of Birth: 21/04/2001
Marks of Operating System:  19.0
Marks of French Language:  18.0
Marks of Numerical Methods:  18.3
*************************
```