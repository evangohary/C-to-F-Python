
######### return avrage of 3 scores, with letter grade for each individualy as well

n1, n2, n3 = int(input("Score 1: ")),int(input("Score 2: ")),int(input("Score 3: "))

holder =(n1 + n2 + n3)

def calc_average(holder):
    return holder/3

print() 
print("Avrage test score:", str(calc_average(holder)))


def determin_grade(holder):
    
    if holder >= 90 and holder <= 100:   
         return "A"
    elif holder >= 80 and holder < 90:
         return "B"
    elif holder >= 70 and holder < 80:
         return "C"
    elif holder >= 60 and holder < 70:
         return "D"
    elif holder < 60:
         return "F"

print()    
print("Score", "     " ,"Letter Grade")
print(n1,"        ", determin_grade(n1))
print(n2,"        ", determin_grade(n2))
print(n3,"        ", determin_grade(n3))

print()
print("This program was written by evan g")
