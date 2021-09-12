course = {
        'CS101':['3004',"Haynes","8:00 am"],
        'CS102':['4501',"Alvarado","9:00 am"],
        'CS103':['6755',"Rich","10:00 am"],
        'NT110':['1244',"Burke","11;00 am"],
        'CM241':['1411',"Lee","1;00 pm"]
}
Course_Number =input("What's your course number ?"'\n')


if Course_Number in course:
        print(course[Course_Number])
        #print("Room Number:" , course[Course_Number][0},"Instrutor: ",course[Course_Number]{1},"Meeting time:",course[Course_Number]{2})
else:
        print("your course is not found!")



