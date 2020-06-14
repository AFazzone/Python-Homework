
l,m,n,o = eval(input("Enter scores:"))
score_list =[l, m, n ,o]
best = max(score_list)
a = best - 10
b = best - 20
c = best - 30
d = best - 40


for i in range(4):
    if score_list[i] >= a:
        print ("Student", i, "score is",  score_list[i], "and the grade is A")
    elif score_list[i] >= b:
        print ("Student", i, "score is" , score_list[i], "and the grade is B")
    elif score_list[i] >= c:
        print ("Student", i, "score is", score_list[i], "and the grade is C")
    elif score_list[i] >= d:
        print ("Student", i, "score is", score_list[i], "and the grade is D")
    else:
        print ("Student", i,"score is", score_list[i], "and the grade is F")