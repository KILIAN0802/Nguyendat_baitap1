Practical work 2: OOP’ed student mark management
- Copy your practical work 1 to 2.student.mark.oop.py
- Make it OOP’ed
- Same functions
  - Proper attributes and methods
  - Proper encapsulation
  - Proper polymorphism
    - e.g. ```.input(), .list()``` methods
- Push your work to corresponding forked [Github repository](https://github.com/quanganh2001/pp2022)

# Jupyter Notebook source code
```py
student_list = []

class student:
    def __init__(self, stName="", stId="", stDob="", courses=""):
        self.stName   = stName
        self.stId    = stId
        self.stDob    = stDob
        self.courses = courses
    
    def inputSt(self, name, stId, stDob, courses):
        st = student(name, stId, stDob, courses)
        student_list.append(st)
    
    def listSt(self, st):
        print(f'Name: {st.stName}')
        print(f'Id: {st.stId}')
        print(f'Date Of Bird: {st.stDob}')
        for u, v in st.courses.items():
            print(f'Mark for {u}: {v}')
        print('*****************\n')
    
    def listCourse(self, course_name):
        
        anotherStList = []
        
        for i in range(len(student_list)):
            for u, v in student_list[i].courses.items():
                if course_name == u:
                    anotherStList.append(student_list[i].stName)
        
        print(f'number of student in {course_name}: {len(anotherStList)}')
        print('Student list: ')
        for i in anotherStList:
            print(f'             - {i}')
            
    def deleteSt(self, name):
        for i in range(len(student_list)):
            if name == student_list[i].stName:
                print(f'student {name} is deleted')
                del student_list[i]

course_list = []
class course:
    def __init__(self, courseId="", courseName=""):
        self.courseId = courseId
        self.courseName = courseName
    
    def inputCourse(self, courseId, courseName):
        c = course(courseId, courseName)
        course_list.append(c)
    
    def mark(self, name, courseName, mark):
        for i in range(len(student_list)):
            if name in student_list[i].stName:
                student_list[i].courses[courseName] = mark


st = student()
st.inputSt('Nguyen Quang Anh', 'BA10-002', '27 October 2001', {})
st.inputSt('Tran Ngoc Bach', 'BA10-046', '24 May 2001', {})
st.inputSt('Kieu Khanh Huyen', 'BA10-064', '25 December 2001', {})
m = course('','')
m.inputCourse(0, 'French Language')
m.inputCourse(1, 'Algorithm')

m.mark('Nguyen Quang Anh', 'French Language', '12.5')
m.mark('Tran Ngoc Bach', 'French Language', '11')
m.mark('Kieu Khanh Huyen', 'French Language', '18.5')

m.mark('Nguyen Quang Anh', 'Algorithm', '12.5')
m.mark('Tran Ngoc Bach', 'Algorithm', '16')
m.mark('Kieu Khanh Huyen', 'Algorithm', '17.5')

for i in range(len(student_list)):
    st.listSt(student_list[i])
```
The result is:
```txt
Name: Nguyen Quang Anh
Id: BA10-002
Date Of Bird: 27 October 2001
Mark for French Language: 12.5
Mark for Algorithm: 12.5
*****************

Name: Tran Ngoc Bach
Id: BA10-046
Date Of Bird: 24 May 2001
Mark for French Language: 11
Mark for Algorithm: 16
*****************

Name: Kieu Khanh Huyen
Id: BA10-064
Date Of Bird: 25 December 2001
Mark for French Language: 18.5
Mark for Algorithm: 17.5
*****************
```
# Python source code
```py
students = []
courses = []
class Student:
  def __init__(self, student_id, studentname, studentdob):
    self.id = student_id
    self.name = studentname
    self.dob = studentdob
    self.marks = {}
  
  def get_id(self):
    return self.id
  
  def get_name(self):
    return self.name
  
  def get_dob(self):
    return self.dob
  
  def get_mark(self):
    return self.marks
  
  def set_id(self, _id):
    self.id = _id
  
  def set_name(self, name):
    self.name = name
  
  def set_dob(self, dob):
    self.dob = dob
  
  def set_mark(self, course, mark):
    self.marks.update({course: mark})
  
  def displayStudent(self):
    print("Student ID: " + self.id)
    print("Student name: " + self.name)
    print("Student DoB: " + self.dob)
  
  def displayMark(self, course):
    print(self.name + "'s mark: " + str(self.marks.get(course)))


class Course:
  def __init__(self, course_id, coursename):
    self.id = course_id
    self.name = coursename
  
  def get_id(self):
    return self.id
  
  def get_name(self):
    return self.name
  
  def set_id(self, id):
    self.id = id
  
  def set_name(self, name):
    self.name = name
  
  def displayCourse(self):
    print("Course ID: " + self.id)
    print("Course name: " + self.name)

def numOfStudent():
    std_num = int(input("How many student in class? "))
    return std_num


def studentInfo():
  std_id = input("Student ID: ")
  std_name = input("Student name: ")
  std_dob = input("Student DoB: ")
  return std_id, std_name, std_dob

def numOfCourse():
    course_num = int(input("Number of courses: "))
    return course_num

def courseInfo():
  course_id = input("Course ID: ")
  course_name = input("Course name: ")
  return course_id, course_name


def findCourseName(courses, course_id):
  for course in courses:
    if course.get_id() == course_id:
      return course.get_name()
  print("Error: Invalid ID!")

if __name__ == "__main__":
  student_num = numOfStudent()
  print(student_num)
  for i in range(0, student_num):
    id, name, dob = studentInfo()
    students.append(Student(id, name, dob))
  
  course_num = numOfCourse()
  for i in range(0, course_num):
    id, name = courseInfo()
    courses.append(Course(id, name))
  
  print("Display students information:\n")
  for student in students:
    student.displayStudent()
  
  print("Display courses information:\n")
  for course in courses:
    course.displayCourse()
  
  a = 'b'
  while a == 'b':
    sel_course_id = input("Select a course ID: ")
    sel_course = findCourseName(courses, sel_course_id)
    print("Course name: " + sel_course + "\n")
    for student in students:
      mark = input("Enter " + student.name + "'s mark: ")
      student.set_mark(sel_course, mark)
    a = input("Select another course? y/n: ")
    print("-------")
  sel_course_id = input("Select a displayed course ID: ")
  sel_course = findCourseName(courses, sel_course_id)
  print(f"Display students' marks of course {sel_course}:\n")
  for student in students:
    student.displayMark(sel_course)
```
The result is:
```txt
How many student in class? 1
1
Student ID: BA10-002
Student name: QuangAnh
Student DoB: 27 Oct 2001
Number of courses: 1
Course ID: FR2
Course name: french
Display students information:

Student ID: BA10-002
Student name: QuangAnh
Student DoB: 27 Oct 2001
Display courses information:

Course ID: FR2
Course name: french
Select a course ID: FR2
Course name: french

Enter QuangAnh's mark: 12.5
Select another course? y/n: n
-------
Select a displayed course ID: FR2
Display students' marks of course french:

QuangAnh's mark: 12.5
```
# Other source code
```py
# Set class student mark management system
class System:
  def __init__(self):
    self.__students = []
    self.__courses = []
  
  # Setter and getter

  def setStudents(self):
    self.__students = []
    for i in range(self.__getInputNum__("students")):
      print("Student " + str(i + 1) + ":")
      self.__students.append(Student())
  
  def setCourses(self):
    self.__courses = []
    for i in range(self.__getInputNum__("courses")):
      print("Course " + str(i + 1) + ":")
      self.__courses.append(Course())
  
  def getStudents(self):
    return self.__students
  
  def getCourses(self):
    return self.__courses

  @staticmethod
  # Enter the number of students
  def __getInputNum__(type_):
    while True:
      try:
        i = int(input("Enter the number of " + type_ + ": "))
        return i
      except ValueError:
        print("Invalid input! Please try again!")
        pass
  
  # Input course name
  def __getInputCourse__(self):
    while True:
      courseName = input("Enter course name: ")
      for course in self.__courses:
        if courseName == course.getName():
          return course
      print("Invalid course! Try again!")
  
  # Choose action
  def __getActionId__(self):
    print("==========")
    print("Actions: ")
    print(" (1) List Courses")
    print(" (2) List Students")
    print(" (3) Set Marks (given course)") # Choose only one course
    print(" (4) Get Marks (given course)") # Choose only one course
    print(" (5) Finish")
    while True:
      try:
        i = self.__getInputNum__("Action")
        if i in (1, 2, 3, 4, 5):
          return i
      except ValueError:
        pass
      print("Invalid input! Try again!")
  
  def __action__(self):
    while True:
      actionId = self.__getActionId__()
      if actionId == 1:
        for course in self.__courses:
          print(course.getName())
      elif actionId == 2:
        for student in self.__students:
          print(student.getName())
      elif actionId == 3:
        course = self.__getInputCourse__()
        course.setMarks(self.__students)
      elif actionId == 4:
        course = self.__getInputCourse__()
        course.getInfo()
      else:
        print("Finish! Thank you!")
        break
  
  def run(self):
    self.setStudents()
    self.setCourses()
    self.__action__()

class Student:
  # Enter your student information
  def __init__(self):
    self.__id = input("Enter id of Student: ")
    self.__name = input("Enter name of Student: ")
    self.__dob = input("Enter DoB of Student: ")
  
  # Getter and setter class Student
  def setId(self, id_):
    self.__id = id_
  
  def setName(self, name_):
    self.__name = name_
  
  def setDoB(self, dob):
    self.__dob = dob
  
  def getId(self):
    return self.__id
  
  def getName(self):
    return self.__name
  
  def getDoB(self):
    return self.__dob
  
  def getInfo(self):
    # Print info student
    print("Student: " + self.__name + ":")
    print(" * Id: " + self.__id)
    print(" * Dob: " + self.__dob)

class Course:
  def __init__(self):
    # Input your course
    self.__name = input("Enter Course name: ")
    self.__id = input("Enter Course ID: ")
    self.__marks = []
  
  # Getter and setter class Course
  def setName(self, name):
    self.__name = name
  
  def setId(self, id_):
    self.__id = id_
  
  def setMarks(self, students):
    self.__marks = []
    print("=========")
    for student in students:
      # Caution: Input the mark, you should type float, not int
      mark = float(input("Enter mark of " + student.getName() + ": "))
      self.__marks.append([student.getName(), mark])
  
  def getName(self):
    return self.__name
  
  def getId(self):
    return self.__id
  
  def getMarks(self):
    return self.__marks
  
  def getInfo(self):
    # Print name Course, ID and mark for this course
    print("Course: " + self.__name + ":")
    print(" * Id: " + self.__id)
    print(" * Marks: ")
    for i in range(len(self.__marks)):
      print("     +   " + self.__marks[i][0] + ": " + str(self.__marks[i][1]))

# Run the code
System = System()
System.run()
```
The result is:
```txt
Enter the number of students: 2
Student 1:
Enter id of Student: BA10
Enter name of Student: Quang Anh
Enter DoB of Student: 27 October 2001
Student 2:
Enter id of Student: BA11
Enter name of Student: Tran Ngoc Bach
Enter DoB of Student: 26 September 2001
Enter the number of courses: 2
Course 1:
Enter Course name: French
Enter Course ID: FR2.1
Course 2:
Enter Course name: Algorithm
Enter Course ID: ADS1
==========
Actions: 
 (1) List Courses
 (2) List Students
 (3) Set Marks (given course)
 (4) Get Marks (given course)
 (5) Finish
Enter the number of Action: 1
French
Algorithm
==========
Actions: 
 (1) List Courses
 (2) List Students
 (3) Set Marks (given course)
 (4) Get Marks (given course)
 (5) Finish
Enter the number of Action: 2
Quang Anh
Tran Ngoc Bach
==========
Actions: 
 (1) List Courses
 (2) List Students
 (3) Set Marks (given course)
 (4) Get Marks (given course)
 (5) Finish
Enter the number of Action: 3
Enter course name: French
=========
Enter mark of Quang Anh: 12.5
Enter mark of Tran Ngoc Bach: 11.5
==========
Actions: 
 (1) List Courses
 (2) List Students
 (3) Set Marks (given course)
 (4) Get Marks (given course)
 (5) Finish
Enter the number of Action: 3
Enter course name: Algorithm
=========
Enter mark of Quang Anh: 8.75
Enter mark of Tran Ngoc Bach: 15.75
==========
Actions: 
 (1) List Courses
 (2) List Students
 (3) Set Marks (given course)
 (4) Get Marks (given course)
 (5) Finish
Enter the number of Action: 4
Enter course name: French
Course: French:
 * Id: FR2.1
 * Marks: 
     +   Quang Anh: 12.5
     +   Tran Ngoc Bach: 11.5
==========
Actions: 
 (1) List Courses
 (2) List Students
 (3) Set Marks (given course)
 (4) Get Marks (given course)
 (5) Finish
Enter the number of Action: 4
Enter course name: Algorithm
Course: Algorithm:
 * Id: ADS1
 * Marks: 
     +   Quang Anh: 8.75
     +   Tran Ngoc Bach: 15.75
==========
Actions: 
 (1) List Courses
 (2) List Students
 (3) Set Marks (given course)
 (4) Get Marks (given course)
 (5) Finish
Enter the number of Action: 5
Finish! Thank you!
```
In there:
Fix source code due to my source code has similarity for other friends
1. Add comments (Especially for getter and setter Class Student and Course)
2. Input the mark (Using float not int)
3. When input number 5, you can see the notification: Finish! Thank you!
