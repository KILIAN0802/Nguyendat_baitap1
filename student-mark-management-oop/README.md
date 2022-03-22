Practical work 2: OOP’ed student mark management
- Copy your practical work 1 to 2.student.mark.oop.py
- Make it OOP’ed
- Same functions
  - Proper attributes and methods
  - Proper encapsulation
  - Proper polymorphism
    - e.g. ```.input(), .list()``` methods
- Push your work to corresponding forked [Github repository](https://github.com/quanganh2001/pp2022)

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

m.mark('Nguyen Quang Anh', 'French Language', '12.5')
m.mark('Tran Ngoc Bach', 'French Language', '11')
m.mark('Kieu Khanh Huyen', 'French Language', '18.5')

for i in range(len(student_list)):
    st.listSt(student_list[i])
```
The result is:
```txt
Name: Nguyen Quang Anh
Id: BA10-002
Date Of Bird: 27 October 2001
Mark for French Language: 12.5
*****************

Name: Tran Ngoc Bach
Id: BA10-046
Date Of Bird: 24 May 2001
Mark for French Language: 11
*****************

Name: Kieu Khanh Huyen
Id: BA10-064
Date Of Bird: 25 December 2001
Mark for French Language: 18.5
*****************
```
