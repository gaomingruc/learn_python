class StudentSystem(object):
    def __init__(self):
        self.students = list()
        self.current = 0

    def add(self):
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        student = dict()
        student["姓名"] = name
        student["年龄"] = age
        self.students.append(student)

    def __str__(self):
        return str(self.students)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.students):
            self.current += 1
            return self.students[self.current - 1]
        else:
            self.current = 0
            raise StopIteration
    

if __name__ == "__main__":
    student_system = StudentSystem()
    student_system.add()
    student_system.add()
    student_system.add()
    for s in student_system:
        print(s)
    for s in student_system:
        print(s)