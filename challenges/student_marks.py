def student_m():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_makrs = student_marks[query_name]
    marksSum = sum(student_makrs)
    avgMarks = marksSum/len(student_makrs)
    print(format(avgMarks, '.2f'));





  



  