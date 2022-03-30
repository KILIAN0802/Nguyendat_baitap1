# Practical work 3: some maths and decorations
- Copy your practical work 2 to 3.student.mark.oop.math.py
- Use math module to round-down student scores to 1-digitdecimal upon input, floor()
- Use numpy module and its array to
  - Add function to calculate average GPA for a given student
    - Weighted sum of credits and marks
  - Sort student list by GPA descending
- Decorate your UI with curses module
- Push your work to corresponding forked [Github repository](https://github.com/quanganh2001/pp2022)
## Jupyter Notebook source code
```py
import numpy as np
import math
```
```py
student_list = []

class student:
  def __init__(self, stName="", stId="", stDob="", courses=""):
    self.stName = stName
    self.stId = stId
    self.stDob = stDob
    self.courses = courses

  def inputSt(self, name, stId, stDob, courses):
    st = student(name, stId, stDob, courses)
    student_list.append(st)
  
  def listSt(self, st):
    print(f'Name: {st.stName}')
    print(f'Id: {st.stId}')
    print(f'Date of Birth: {st.stDob}')
    for u, v in st.courses.items():
      print(f'Mark for {u}: {v}')
    print('*****************\n')
  
  def listCourse(self, course_name):
    anotherStList = []

    for i in range(len(student_list)):
      for u, v in student_list[i].courses_items():
        if course_name == u:
          anotherStList.append(student_list[i].stName)
    
    print(f'number of student in {course_name}: {len(anotherStList)}')
    print('Student list: ')
    for i in anotherStList:
      print(f'             - {i}')
  
  def deleteSt(self, name):
    for i in range(len(student_list)):
      if name == student_list[i].stName:
        print(f'student {name} is deleted!')
        del student_list[i]
```
```py
course_list = []
class course:
  def __init__(self, courseId="", courseName=""):
    self.courseId = courseId
    self.courseName = courseName
  
  def inputCourse(self, courseId, courseName):
    c = course(courseId, courseName)
    course_list.append(c)
  
  def courseInfo(self, c):
    print(f"Course Name: {c.courseName}")
    print(f"Course Id: {c.courseId}")
  
  def mark(self, name, courseName, mark):
    for i in range(len(student_list)):
      if name in student_list[i].stName:
        student_list[i].courses[courseName] = math.floor(mark*10)/10
```
```py
class GPA:
  def __init__(self, name=''):
    self.name = name
  
  def calcGPA(self, name, credit):
    ls = []
    for i in range(len(student_list)):
      if name == student_list[i].stName:
        print(student_list[i].courses)
        ls.append(student_list[i].courses)
        grade = np.array([list(d.values()) for d in ls])
        credit = np.array(credit)
        gpa = grade.dot(credit)/sum(credit)
        return tuple((name, gpa))
  
  def sort(self):
    gpa_list = []
    for i in range(len(student_list)):
      gpa_list.append(self.calcGPA(student_list[i].stName, [3, 5]))
    sorted_list = sorted(gpa_list, key=lambda i: i[1])
    for head,tail in enumerate(sorted_list):
      print(f"Ranking {head+1} is {tail[0]} with {tail[1]} points")
```
```py
st = student()
st.inputSt('Nguyễn Quang Anh', 'BA10-002', '27 Oct 2001', {})
st.inputSt('Kim Nhật Thành', 'BA10-058', '11 July 2001', {})
st.inputSt('Nguyễn Thị Khánh Huyền', 'BA10-025', '24 May 2001', {})

m = course('','')
m.inputCourse(0, 'French Language')
m.inputCourse(1, 'Algorithm')

# French Language marks
m.mark('Nguyễn Quang Anh', 'French Language', 11.5)
m.mark('Kim Nhật Thành', 'French Language', 8.5)
m.mark('Nguyễn Thị Khánh Huyền', 'French Language', 16.75)

# Algorithm and Data Structures marks
m.mark('Nguyễn Quang Anh', 'Algorithm', 14.5)
m.mark('Kim Nhật Thành', 'Algorithm', 7.5)
m.mark('Nguyễn Thị Khánh Huyền', 'Algorithm', 19)

for i in range(len(student_list)):
  st.listSt(student_list[i])
```
The result is:
```txt
Name: Nguyễn Quang Anh
Id: BA10-002
Date of Birth: 27 Oct 2001
Mark for French Language: 11.5
Mark for Algorithm: 14.5
*****************

Name: Kim Nhật Thành
Id: BA10-058
Date of Birth: 11 July 2001
Mark for French Language: 8.5
Mark for Algorithm: 7.5
*****************

Name: Nguyễn Thị Khánh Huyền
Id: BA10-025
Date of Birth: 24 May 2001
Mark for French Language: 16.7
Mark for Algorithm: 19.0
*****************
```
### List Courses
```py
for i in range(len(course_list)):
  m.courseInfo(course_list[i])
```
The result is:
```txt
Course Name: French Language
Course Id: 0
Course Name: Algorithm
Course Id: 1
```
### Calculate GPA
```py
gpa = GPA()
gpa.sort()
```
The result is:
```txt
{'French Language': 11.5, 'Algorithm': 14.5}
{'French Language': 8.5, 'Algorithm': 7.5}
{'French Language': 16.7, 'Algorithm': 19.0}
Ranking 1 is Kim Nhật Thành with [7.875] points
Ranking 2 is Nguyễn Quang Anh with [13.375] points
Ranking 3 is Nguyễn Thị Khánh Huyền with [18.1375] points
```
## Python source code
```py
from math import *


class Student:
    def __init__(self, id="", name="", dob="", GPA=0):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__GPA = GPA

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def getGPA(self):
        return self.__GPA

    def setGPA(self, GPA):
        self.__GPA = GPA

    def input(self):
        self.__id = input("Enter Student Id: ")
        self.__name = input("Enter Student Name: ")
        self.__dob = input("Enter Student Date of Birth: ")

    def __str__(self):
        return "Student: " + self.__name + " with id of " + self.__id + " born in " + self.__dob

    def describe(self):
        print(self.__str__())


class Mark:
    def __init__(self, studentName, course, mark=0, credit=0, GPA=0):
        self.__studentName = studentName
        self.__course = course
        self.__credit = credit
        self.__mark = mark
        self.__GPA = GPA

    def input(self):
        print(f"Enter Student's mark for {self.__studentName}")
        self.__mark = float(input(f"in {self.__course}: "))
        self.__credit = Course.getCredit(course)

    def getMark(self):
        return floor(self.__mark * 10) / 10

    def getCourse(self):
        return self.__course

    def getGPA(self):
        return floor(self.__GPA * 10) / 10

    def setGPA(self, GPA):
        self.__GPA = GPA

    def getName(self):
        return self.__studentName

    def getCredit(self):
        return self.__credit

    def __str__(self):
        return "Student " + self.getName() + " has a mark of " + str(
            self.getMark()) + " in " + self.getCourse()

    def describe(self):
        print(self.__str__())


class Course:
    def __init__(self, id="", name="", credit=0):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCredit(self):
        return self.__credit

    def input(self):
        self.__id = input("Enter Course Id: ")
        self.__name = input("Enter Course Name: ")
        self.__credit = int(input("Enter credit : "))

    def __str__(self):
        return "Course: " + self.__name + " with id of " + self.__id + " and credit of " + str(self.__credit)

    def describe(self):
        print(self.__str__())


# create arrays
ClassRoom = []
ListOfCourse = []
Marks = []

# find the number of students
NumberStd = int(input("Enter number of Students: "))

# adding Student objects into array ClassRoom
for i in range(NumberStd):
    s = Student()
    s.input()
    ClassRoom += [s]

# print out all the students in ClassRoom
for student in ClassRoom:
    print(student)

# find the number of courses
NumberOfCourse = int(input("Enter number of Courses: "))

# adding Course objects into array ListOfCourse
for i in range(NumberOfCourse):
    c = Course()
    c.input()
    ListOfCourse += [c]

# print out all the courses in ListOfCourse
for c in ListOfCourse:
    print(c)


# choose a course
def choseCourse():
    Course = input("Enter the course name: ")
    return Course


# input marks for all student in a Course
def inputMark(Course):
    for i in range(NumberOfCourse):
        if Course == ListOfCourse[i].getName():
            for j in range(NumberStd):
                m = Mark(ClassRoom[j].getName(), ListOfCourse[i].getName(), ListOfCourse[i].getCredit())
                m.input()
                Marks.append(m)


# print the Mark for all student in a Course
def printMark(Course):
    for mark in Marks:
        if mark.getCourse() == Course:
            print([mark.getName(), mark.getMark(), mark.getCredit()])


# choose student
def chooseStudent():
    stdName = input("Enter a Student's name: ")
    return stdName


# average Mark
def averageMark(Name):
    x = y = 0
    for mark in Marks:
        if mark.getName() == Name:
            x += mark.getMark() * mark.getCredit()
            y += mark.getCredit()

    AverageMark = x / y
    AverageMark_fld = floor(AverageMark * 10) / 10
    print("Average Mark for " + Name + ": " + str(AverageMark_fld))

    for students in ClassRoom:
        if students.getName() == Name:
            students.setGPA(AverageMark_fld)


# array sorting
def arrSort():
    SortedArr = []

    for i in range(len(ClassRoom)):
        max_index = i
        for j in range(i + 1, len(ClassRoom)):
            if ClassRoom[max_index].getGPA() < ClassRoom[j].getGPA():
                max_index = j
        ClassRoom[i], ClassRoom[max_index] = ClassRoom[max_index], ClassRoom[i]

    for stds in ClassRoom:
        SortedArr.append(stds.getName())

    print("List of Student name in order of GPA from highest to lowest :")
    print(SortedArr)


# main
for course in ListOfCourse:
    print("-----Inputting marks -----")
    inputMark(choseCourse())

for course in ListOfCourse:
    print("-----Printing marks -----")
    printMark(choseCourse())

for std in ClassRoom:
    print("-----Calculating GPA -----")
    averageMark(chooseStudent())

arrSort()
```
The result is:
```txt
Enter number of Students: 2
Enter Student Id: BA10
Enter Student Name: QA
Enter Student Date of Birth: 29 Sep 2001
Enter Student Id: BA12
Enter Student Name: Kim Nhat Thanh
Enter Student Date of Birth: 20 Nov 2001
Student: QA with id of BA10 born in 29 Sep 2001
Student: Kim Nhat Thanh with id of BA12 born in 20 Nov 2001
Enter number of Courses: 2
Enter Course Id: FR2
Enter Course Name: French
Enter credit : 4
Enter Course Id: ADS1
Enter Course Name: Algorithm
Enter credit : 3
Course: French with id of FR2 and credit of 4
Course: Algorithm with id of ADS1 and credit of 3
-----Inputting marks -----
Enter the course name: French
Enter Student's mark for QA
in French: 12.5
Enter Student's mark for Kim Nhat Thanh
in French: 1
-----Inputting marks -----
Enter the course name: Algorithm
Enter Student's mark for QA
in Algorithm: 10.5
Enter Student's mark for Kim Nhat Thanh
in Algorithm: 18
-----Printing marks -----
Enter the course name: French
['QA', 12.5, 4]
['Kim Nhat Thanh', 1.0, 4]
-----Printing marks -----
Enter the course name: Algorithm
['QA', 10.5, 3]
['Kim Nhat Thanh', 18.0, 3]
-----Calculating GPA -----
Enter a Student's name: QA
Average Mark for QA: 11.6
-----Calculating GPA -----
Enter a Student's name: Kim Nhat Tha
Average Mark for Kim Nhat Thanh: 8.2
List of Student name in order of GPA
['QA', 'Kim Nhat Thanh']
```
