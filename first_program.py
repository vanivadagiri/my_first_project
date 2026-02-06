students = {}

def add_student(roll,name,marks):
    students[roll] = {"name":name,"marks":marks}

def view_student_details():
    for i,j in students.items():
        print(i,j["name"],j["marks"])

add_student(1,"vani",98)
add_student(2,"vinutha",98)
add_student(3,"ajaay",100)
view_student_details()

#-----------------------------------------------------------------------------




