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
