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
