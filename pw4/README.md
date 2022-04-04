# Practical work 4: modularization
- Split your program 3.student.mark.oop.math.py to modules and packages in a new `pw4` directory (both Jupyter Notebook and Python sources code)
   - `input.py`: module for input
   - `output.py`: module for `curses` output
   - `domains`: package for classes
   - `main.py`: main script for coordination
- Push your work to corresponding forked [Github repository](https://github.com/quanganh2001/pp2022)

## module for input
```py
class Input:
  def __init__(self, stName="", stId="", stDob="", courses=""):
    self.stName   = stName
    self.stId    = stId
    self.stDob    = stDob
    self.courses = courses
    self.student_list = []

  def inputSt(self, name, stId, stDob, courses):
    st = Input(name, stId, stDob, courses)
    self.student_list.append(st)

  def deleteSt(self, name):
    for i in range(len(self.student_list)):
      if name == self.student_list[i].stName:
        print(f'student {name} is deleted')
        del self.student_list[i]
```
## module for curses output
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
        print(f"Marks of {i.courses[j][0]} :", i.courses[j][1])
      print("************************************")
```
## package for classes
```py
class domain:
  def __init__(self):
      pass
  def execute(self):
    st = Input('' ,'', '' ,  0)
    st.inputSt('Nguyễn Quang Anh', 'BA10-002', '2001', (('Advanced Python Programming ','15'), ('French ','14'), ('Singal ','12')))
    st.inputSt('Kim Nhật Thành', 'BA10-065', '2001', (('Advanced Python Programming ','11'), ('French ','16'), ('Singal ','8.5')))
    st.inputSt('Nguyễn Thị Khánh Huyền', 'BA10-048', '2001', (('Advanced Python Programming ','10'), ('French ','14.75'), ('Singal ','12.5')))

    display = Output(None)
    display.listSt(st.student_list)
```
## main script for coordination
```py
if __name__ == "__main__":
  main = domain()
  main.execute()
```
The result is
```txt
Name: Nguyễn Quang Anh
Id: BA10-002
Date Of Birth: 2001
Marks of Advanced Python Programming  : 15
Marks of French  : 14
Marks of Singal  : 12
************************************
Name: Kim Nhật Thành
Id: BA10-065
Date Of Birth: 2001
Marks of Advanced Python Programming  : 11
Marks of French  : 16
Marks of Singal  : 8.5
************************************
Name: Nguyễn Thị Khánh Huyền
Id: BA10-048
Date Of Birth: 2001
Marks of Advanced Python Programming  : 10
Marks of French  : 14.75
Marks of Singal  : 12.5
************************************
```