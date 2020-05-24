def nested_list_2nd_lower():

    #students = []
    #for _ in range(int(input("Enter Number of Students: "))):
    #  name = input("Enter Name: ")
    #  score = float(input("Enter Score: "))
    #  students.append([name, score])
    #students=[['x', 12.21], ['y', 6.65], ['z', -12.32],['x1', 7.21],['y1', 37.21],['y2', 6.65]]

    students=[['xr', 20], ['y', 20], ['z', 19],['x1', 19],['x3', 21]]


    print(students)
  
    #print(sorted(students));

    def take_marks(item):
      return item[1]

    def take_name(item):
      return item[0]

    #print(sorted(students, key=take_marks))
    first_lowest_grade = min (sorted (students, key=take_marks) , key = take_marks)
    print(first_lowest_grade)
    for student in students[:]:
      print("student ", student)
      if student[1] == first_lowest_grade[1]:
        students.remove(student)
    print("students " ,students)
    ##print(sorted(students, key=take_marks))

    second_lowest_grade_makrs = sorted(students, key=take_marks)[0][1]
    #print(second_lowest_grade_makrs)

    second_lowest_grade_names = []
    sorted_by_name = sorted(students, key=take_name)

    for item in sorted_by_name:
      if ( item[1] == second_lowest_grade_makrs):
        second_lowest_grade_names.append(item[0]);

    for item in second_lowest_grade_names:
      print(item)
    
    





    
