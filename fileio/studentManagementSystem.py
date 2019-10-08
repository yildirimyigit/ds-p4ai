# -*- coding: utf-8 -*-

#
# Burada file'dan okuyup listeleri dolduruyoruz
#

stunums = []
names = []
grades = []

while True:
    print('1- Enter user and grade')
    print("2- Search for user's grade")
    print('3- Remove user and grade')
    print('4- Look at the top scorer')
    print('0- Exit')
    print('===')   
    print(stunums)   
    print(names)
    print(grades)
    print("*****")
    try:
        sel = int(input('What do you want to do?\n'))
    except ValueError:
        print("No!")
        sel = -1

    
    if sel == 1:
        stunum = input('Student Number: ')
        name = input('Name: ')
        grade = float(input('Grade: '))
        
        stunums.append(stunum)
        names.append(name)
        grades.append(grade)
    elif sel == 2:
        name = input('Name: ')
        for i in range(len(names)):
            if names[i] == name:
                print(name +': '+ str(grades[i]))
                break
    elif sel == 3:
        name = input('Name: ')
        for i in range(len(names)):
            if names[i] == name:
                stunums.pop(i)
                names.pop(i)
                grades.pop(i)
                break
    elif sel == 4:
        top_score = -1
        top_name = ''
        for i in range(len(names)):
            if grades[i] > top_score:
                top_score = grades[i]
                top_name = names[i]
        print(top_name + ": " + str(top_score))
        
    elif sel == 0:
		#
		# Burada lıstelerı file'a yazıyoruz
		#

        break
    else:
        print("Error!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
