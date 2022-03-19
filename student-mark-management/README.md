# Practical work 1: Student mark management
## Functions
 + Input functions:
 + Input number of students in a class
 + Input student information: id, name, date of birth
 + Input number of courses
 + Input course information: id, name
 + Select a course, input marks for student in this course
````py
# Function
# 1) Input functions:
def Studentscount():
	s = int(input("The total number of students is: "))
	return s

# How many courses are there?
def Coursescount():
	c = int(input("The total number of courses is: "))
	return c

# Info Student
def Studentinfo():
	id = input("\tStudent's ID is: ")
	name = input("\tYour name: ")
	DoB = input("\tDate of birth: ")
	s = {"ID": id, "Name": name, "DoB": DoB}
	return s

# Courses Info
def Coursesinfo():
	id = input("\tCourse ID: ")
	name = input("\tCourse name: ")
	c = {"ID": id, "name": name}
	return c

# Mark students
def studentMarks():
	sel_course_id = input("Select a course ID: ")
	for i in range(len(course)):
		if course[i].get("ID") == sel_course_id:
			cid = course[i].get("name")
			m = {"Course": cid, "Students and marks": []}
			print("Course name: " + course[i].get("name") + "\n")
			for j in range(len(students)):
				mark = float(input("\tEnter " + students[j].get("Name") + "'s mark "))
				sid = students[j].get("Name")
				m["Students and marks"].append((sid, mark))
			return m
````

## Listing functions:
  + List courses
  + List students
  + Show student marks for a given course


```py
# 2) Display functions
# List students
def Studentsprint():
	print("\nThe list of all student is: ")
	print('\n'.join(map(str, students)))

# List courses
def Coursesprint():
	print("\nThe list of all courses is: ")
	print('\n'.join(map(str, course)))

# Display marks
def displayMarks():
	choose = input("\n---------------------------------\nPlease choose the course that you want to see marks (course name only): ")
	for i in range(len(marks)):
		if marks[i].get("Course") == choose:
			print(marks[i])

# Main
# I/ Students and Courses
# 1) Input
students = []
scount = Studentscount()
print("Please enter the information of the student: ")
for i in range(0, scount):
	s = Studentinfo()
	students += [s]
	print("\n---------------------------------")

course = []
ccount = Coursescount()
print("\nPlease enter the information of the course: ")
for i in range(0, ccount):
	c = Coursesinfo()
	course += [c]
	print("\n---------------------------------")

# 2) Display
Studentsprint()
Coursesprint()

# II/ Marks
# 1) Input
rawmarks = []
marks = []
print("\n---------------------------------\nPlease enter the marks of the course: ")
x = 'yes'
while x == 'yes':
	ma = studentMarks()
	rawmarks += [ma]
	x = input("\n*** Do you want to select another course? (yes or no) *** ")
	if (x != "yes") and (x != "no"):
		print("Invalid choice! Please choose again.")
		x = "yes"
marks = list(filter(None, rawmarks))

# 2) Display
y = 'yes'
while y == 'yes':
	displayMarks()
	y = input("\n*** Do you want to select another course? (yes or no) *** ")
	if (y != "yes") and (y != "no"):
		print("Invalid choice! Please choose again.")
		y = "yes"
```

- Push your work to corresponding forked [Github repository](https://github.com/quanganh2001/pp2022)

Here is my full source code:

```py
# Function
# 1) Input functions:
def Studentscount():
	s = int(input("The total number of students is: "))
	return s

# How many courses are there?
def Coursescount():
	c = int(input("The total number of courses is: "))
	return c

# Info Student
def Studentinfo():
	id = input("\tStudent's ID is: ")
	name = input("\tYour name: ")
	DoB = input("\tDate of birth: ")
	s = {"ID": id, "Name": name, "DoB": DoB}
	return s

# Courses Info
def Coursesinfo():
	id = input("\tCourse ID: ")
	name = input("\tCourse name: ")
	c = {"ID": id, "name": name}
	return c

# Mark students
def studentMarks():
	sel_course_id = input("Select a course ID: ")
	for i in range(len(course)):
		if course[i].get("ID") == sel_course_id:
			cid = course[i].get("name")
			m = {"Course": cid, "Students and marks": []}
			print("Course name: " + course[i].get("name") + "\n")
			for j in range(len(students)):
				mark = float(input("\tEnter " + students[j].get("Name") + "'s mark "))
				sid = students[j].get("Name")
				m["Students and marks"].append((sid, mark))
			return m

# 2) Display functions
# List students
def Studentsprint():
	print("\nThe list of all student is: ")
	print('\n'.join(map(str, students)))

# List courses
def Coursesprint():
	print("\nThe list of all courses is: ")
	print('\n'.join(map(str, course)))

# Display marks
def displayMarks():
	choose = input("\n---------------------------------\nPlease choose the course that you want to see marks (course name only): ")
	for i in range(len(marks)):
		if marks[i].get("Course") == choose:
			print(marks[i])

# Main
# I/ Students and Courses
# 1) Input
students = []
scount = Studentscount()
print("Please enter the information of the student: ")
for i in range(0, scount):
	s = Studentinfo()
	students += [s]
	print("\n---------------------------------")

course = []
ccount = Coursescount()
print("\nPlease enter the information of the course: ")
for i in range(0, ccount):
	c = Coursesinfo()
	course += [c]
	print("\n---------------------------------")

# 2) Display
Studentsprint()
Coursesprint()

# II/ Marks
# 1) Input
rawmarks = []
marks = []
print("\n---------------------------------\nPlease enter the marks of the course: ")
x = 'yes'
while x == 'yes':
	ma = studentMarks()
	rawmarks += [ma]
	x = input("\n*** Do you want to select another course? (yes or no) *** ")
	if (x != "yes") and (x != "no"):
		print("Invalid choice! Please choose again.")
		x = "yes"
marks = list(filter(None, rawmarks))

# 2) Display
y = 'yes'
while y == 'yes':
	displayMarks()
	y = input("\n*** Do you want to select another course? (yes or no) *** ")
	if (y != "yes") and (y != "no"):
		print("Invalid choice! Please choose again.")
		y = "yes"
```
As you can see, how many students are there is the total of students, enter course you should enter ID course and name course.

Now you want to show mark courses, you should input name course only to see marks course. For example input is French Language, so the result is 12.5

The result is:
```txt
The total number of students is: 1
Please enter the information of the student:
        Student's ID is: BA10-002
        Your name: Nguyen Quang Anh
        Date of birth: 27 October 2001

---------------------------------
The total number of courses is: 1

Please enter the information of the course:
        Course ID: FR2.1
        Course name: French Language

---------------------------------

The list of all student is:
{'ID': 'BA10-002', 'Name': 'Nguyen Quang Anh', 'DoB': '27 October 2001'}

The list of all courses is:
{'ID': 'FR2.1', 'name': 'French Language'}

---------------------------------
Please enter the marks of the course:
Select a course ID: FR2.1
Course name: French Language

        Enter Nguyen Quang Anh's mark 12.5

*** Do you want to select another course? (yes or no) *** no

---------------------------------
Please choose the course that you want to see marks (course name only): French Language
{'Course': 'French Language', 'Students and marks': [('Nguyen Quang Anh', 12.5)]}

*** Do you want to select another course? (yes or no) *** no
```
Other method (you can reference)
```py
def get_number_of_students():
    return int(input('-> Enter number of students: '))

def get_student_information():
    return {'id': input('-> Enter student id: '),
            'name': input('-> Enter student name: '),
            'dob': input("-> Enter student's date of birth: ")}

def get_number_of_courses():
    return int(input('-> Enter number of courses: '))

def get_course_information():
    return {'id': input('-> Enter course id: '),
            'name': input('-> Enter course name: ')}

def update_marks_of_course(course):
    print(f"-> Enter marks for the course {course['name']}: ")
    course['marks'] = []

    for student in students:
        course['marks'].append((student,
            input(f"-> Enter mark for student {student['name']}: ")))

def list_courses():
    print('Listing available courses: ')

    for course in courses:
        print(f"- [{course['id']}] {course['name']}", end='')
        print(' (mark available)' if 'marks' in course else '')

def list_students():
    print('Listing students: ')
    print(f'{"ID":^10}{"DATE OF BIRTH":^15}{"NAME":^20}')

    for student in students:
        print(f"{student['id']:^10}{student['dob']:^15}{student['name']:>20}")
    
    print()

def show_marks_of_course(course):
    if 'marks' in course:
        print(f"Show marks of the course {course['name']}: ")

        print(f'{"NAME":^20}{"MARK":^5}')
        for student, mark in course['marks']:
            print(f"{student['name']:<20}{mark:>5}")
    else:
        print('This course has no marks.')

def select_course_prompt(intro_message):
    list_courses()
    print(intro_message)

    return input('-> Choose a course (Enter nothing to skip): ')

def search(List, keyword):
    for item in List:
        if keyword in item.values():
            return item
    
    empty_item = List[0].copy()
    empty_item.clear()
    return empty_item

def action_loop(msg=None, callback=None):
    while True:
        keyword = select_course_prompt(f'-> {msg}')
        if not keyword:
            print()
            break
        callback(search(courses, keyword))
        print()

if __name__ == '__main__':
    students = []
    courses = []

    for _ in range(get_number_of_students()):
        students.append(get_student_information())
    
    for _ in range(get_number_of_courses()):
        courses.append(get_course_information())
    
    list_students()
    action_loop(msg='Marking courses...', callback=update_marks_of_course)
    action_loop(msg='Select a course to show marks...', callback=show_marks_of_course)

    print('Thank you for using the service!')
```
The result is:
```txt
-> Enter number of students: 3
-> Enter student id: BA10-002
-> Enter student name: Nguyen Quang Anh
-> Enter student's date of birth: 27 October 2001
-> Enter student id: BA10-046
-> Enter student name: Tran Ngoc Bach
-> Enter student's date of birth: 25 July 2001
-> Enter student id: BA10-069
-> Enter student name: Kieu Khanh Huyen
-> Enter student's date of birth: 21 September 2001
-> Enter number of courses: 3
-> Enter course id: FR2.1
-> Enter course name: French Language
-> Enter course id: ADS1
-> Enter course name: Algorithm
-> Enter course id: Linear_algebra
-> Enter course name: Linear Algebra
Listing students: 
    ID     DATE OF BIRTH         NAME        
 BA10-002 27 October 2001    Nguyen Quang Anh
 BA10-046  25 July 2001        Tran Ngoc Bach
 BA10-069 21 September 2001    Kieu Khanh Huyen

Listing available courses: 
- [FR2.1] French Language
- [ADS1] Algorithm
- [Linear_algebra] Linear Algebra
-> Marking courses...
-> Choose a course (Enter nothing to skip): FR2.1
-> Enter marks for the course French Language: 
-> Enter mark for student Nguyen Quang Anh: 12.5
-> Enter mark for student Tran Ngoc Bach: 10
-> Enter mark for student Kieu Khanh Huyen: 18

Listing available courses: 
- [FR2.1] French Language (mark available)
- [ADS1] Algorithm
- [Linear_algebra] Linear Algebra
-> Marking courses...
-> Choose a course (Enter nothing to skip): ADS1
-> Enter marks for the course Algorithm: 
-> Enter mark for student Nguyen Quang Anh: 7.5
-> Enter mark for student Tran Ngoc Bach: 10
-> Enter mark for student Kieu Khanh Huyen: 17.6

Listing available courses: 
- [FR2.1] French Language (mark available)
- [ADS1] Algorithm (mark available)
- [Linear_algebra] Linear Algebra
-> Marking courses...
-> Choose a course (Enter nothing to skip): Linear_algebra
-> Enter marks for the course Linear Algebra: 
-> Enter mark for student Nguyen Quang Anh: 18
-> Enter mark for student Tran Ngoc Bach: 17
-> Enter mark for student Kieu Khanh Huyen: 12.5

Listing available courses: 
- [FR2.1] French Language (mark available)
- [ADS1] Algorithm (mark available)
- [Linear_algebra] Linear Algebra (mark available)
-> Marking courses...
-> Choose a course (Enter nothing to skip): 

Listing available courses: 
- [FR2.1] French Language (mark available)
- [ADS1] Algorithm (mark available)
- [Linear_algebra] Linear Algebra (mark available)
-> Select a course to show marks...
-> Choose a course (Enter nothing to skip): FR2.1
Show marks of the course French Language: 
        NAME        MARK 
Nguyen Quang Anh     12.5
Tran Ngoc Bach         10
Kieu Khanh Huyen       18

Listing available courses: 
- [FR2.1] French Language (mark available)
- [ADS1] Algorithm (mark available)
- [Linear_algebra] Linear Algebra (mark available)
-> Select a course to show marks...
-> Choose a course (Enter nothing to skip): ADS1
Show marks of the course Algorithm: 
        NAME        MARK 
Nguyen Quang Anh      7.5
Tran Ngoc Bach         10
Kieu Khanh Huyen     17.6

Listing available courses: 
- [FR2.1] French Language (mark available)
- [ADS1] Algorithm (mark available)
- [Linear_algebra] Linear Algebra (mark available)
-> Select a course to show marks...
-> Choose a course (Enter nothing to skip): Linear_algebra
Show marks of the course Linear Algebra: 
        NAME        MARK 
Nguyen Quang Anh       18
Tran Ngoc Bach         17
Kieu Khanh Huyen     12.5

Listing available courses: 
- [FR2.1] French Language (mark available)
- [ADS1] Algorithm (mark available)
- [Linear_algebra] Linear Algebra (mark available)
-> Select a course to show marks...
-> Choose a course (Enter nothing to skip): 

Thank you for using the service!
```