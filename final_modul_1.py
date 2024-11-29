grades =  [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_student = sorted (students)
print( "отсортированный список студентов: ", sorted_student) #сортируем в алфавитном порядке список
sr_ball=(sum(grades[0]))
sr_1_ball=(sum(grades[1]))
sr_2_ball=(sum(grades[2]))
sr_3_ball=(sum(grades[3]))
sr_4_ball=(sum(grades[4]))
print (int(sr_ball))
summa_ball_studentov = [ sum(grades[0]), sum(grades[1]), sum(grades[2]), sum(grades[3]), sum(grades[4])]
print("Сумма баллов студентов" , summa_ball_studentov)
a=len(grades[0])
b=len(grades[1])
c=len(grades[2])
d=len(grades[3])
e=len(grades[4])
#p=len(grades) #считаем количество элементов в списке
#print (p)
#print("количество оценок первого ученика" , a)
#print("количество оценок второго ученика" , b)
#print("количество оценок третьего ученика" , c)
#print("количество оценок четвертого ученика" , d)
#print("количество оценок пятого ученика" , e)
sr_ball_1 = float(sr_ball/a) #считаем среднее арифместическое первого числа списка
sr_ball_2 = float(sr_1_ball/b)
sr_ball_3 = float(sr_2_ball/c)
sr_ball_4 = float(sr_3_ball/d)
sr_ball_5 = float(sr_4_ball/e)
#print("среднее арифметическое оценок первого ученика" , sr_ball_1)
#ocenki = {sorted_student[0] : sr_ball_1}
ocenki = {}
#print ('средний балл учеников ' , ocenki)
ocenki.update ({sorted_student[0] : sr_ball_1,
                sorted_student[1]: sr_ball_2,
                sorted_student[2]: sr_ball_3,
                sorted_student[3]: sr_ball_4,
                sorted_student[4]: sr_ball_5})
print ('средний балл учеников ' , ocenki)