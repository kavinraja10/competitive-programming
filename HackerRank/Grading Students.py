def gradingStudents(grades):
    res=[]
    for i in grades:
        if i<38:
            res.append(i)
        elif ((((i//5)+1)*5)-i) <=2 :
            res.append(((i//5)+1)*5)
        else:
            res.append(i)
    return res
