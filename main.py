from database import *
import os

mySubject = ["maths","science","english","geography","history"]

def calculateGrade(percentage):
    x = ""
    if percentage > 90:
        x = "A"
    elif percentage > 80:
        x = "B"
    elif percentage > 70:
        x = "C"
    elif percentage > 60:
        x = "D"
    elif percentage > 36:
        x = "E"
    else: 
        x = "F"
    return x

def display_student(val):
    print("\n--------------------------------------------------------------------")
    print("Name of Student : " , val["name"].upper())
    print("Roll Number of Student : " , val["roll"])
    print("\nMaths : " , val["maths"])
    print("Science : " , val["science"])
    print("English : " , val["english"])
    print("Geography : " , val["geography"])
    print("History : " , val["history"])
    print("\nTotal Marks (?/500) : " , val["total"])
    print("Grade : " , val["grade"])
    print("Percentage : " , val["percentage"])

class student:

    def add(self):
        mydict = {}
        total = 0
        grade = ""
        try:
            mydict["name"] = input("Name of Student : ").lower()
            mydict["roll"] = int(input("Roll number of Student : "))
            for subject in mySubject:
                marks = float(input(f"Enter {subject} Marks (?/100) : "))
                mydict[subject] = marks
                total += marks

            mydict["total"] = total
            percentage = total / 5
            grade = calculateGrade(percentage)

            mydict["percentage"] = percentage
            mydict["grade"] = grade

            mycol.insert_one(mydict)
            os.system("cls")
            print("\nStudent data inserted..!!\n\n")        
        except Exception as err:
            os.system("cls")
            print("\nError in Data Fromat which is entered..!\n")
            start()

    def select(self):
        result = mycol.find()
        return result

    def select_single(self , roll):
        result = mycol.find_one({"roll":roll})
        return result


def start():
    
    obj = student()

    print("\nAdd Student : 1")
    print("Select Student : 2")
    print("Select All Student : 3")
    print("Exit : 4")

    try:     
        num = int(input("\nSelect : "))
    except Exception as err:
        os.system("cls")
        print("\nEnter Proper Data...!\n")
        start()

    if num == 1:
        obj.add()
        start()

    elif num == 2:
        roll = int(input("Enter Roll Number : "))
        result = obj.select_single(roll = roll)
        os.system("cls")
        if result != None:
            display_student(result)
            input("\n\nPress Enter to Continue...")
            os.system("cls")
        else:
            print(f"No Data for Roll No. {roll}..!\n")
        start()

    elif num == 3:
        result = obj.select()
        os.system("cls")
        for val in result:
            display_student(val)
        input("\n\nPress Enter to Continue...")
        os.system("cls")
        start()

    elif num == 4:
        print("\nQuitting..!\n")
        exit()
        
            
if __name__ == "__main__":
    start()