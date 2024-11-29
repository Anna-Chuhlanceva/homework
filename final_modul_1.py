grades =  [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_student = sorted (students)
print( "отсортированный список студентов: ", sorted_student) #сортируем в алфавитном порядке список
#summa_ball_studentov = [ sum(grades[0]), sum(grades[1]), sum(grades[2]), sum(grades[3]), sum(grades[4])]
#print("Сумма баллов студентов" , summa_ball_studentov)
#p=len(grades) #считаем количество элементов в списке
#print (p)
sr_ball_1 = float(sum(grades[0])/len(grades[0])) #считаем среднее арифместическое первого ученика из отсортированного списка
sr_ball_2 = float(sum(grades[1])/len(grades[1]))
sr_ball_3 = float(sum(grades[2])/len(grades[2]))
sr_ball_4 = float(sum(grades[3])/len(grades[3]))
sr_ball_5 = float(sum(grades[4])/len(grades[4]))
ocenki = {}
ocenki.update ({sorted_student[0] : sr_ball_1,
                sorted_student[1]: sr_ball_2,
                sorted_student[2]: sr_ball_3,
                sorted_student[3]: sr_ball_4,
                sorted_student[4]: sr_ball_5})
print ('средний балл учеников ' , ocenki)