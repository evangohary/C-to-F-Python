##
## Open a .txt file containing a list of grades, check if they are correct and use that
## Information to get a Score, Number correct, Number wrong, Questions missed, and say passed or failed exam
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
filepath = filedialog.askopenfilename()

print(filepath)
file = open(filepath,'r')
userans = []
for line in file:
    userans.append(line.rstrip('\n'))


correctans =  ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
numcorrect = 0
numwrong = []

for i in range(0,len(userans)):
    if userans[i] == correctans[i]:
        numcorrect = numcorrect+1
        
    else:
        numwrong.append(i+1)


percent = (numcorrect*20)


## prints
print()
print('Name of Examinee: Evan G')
print("Score:", (numcorrect*100)/20,'%')

if numcorrect >= 15:
    print('Congratulation, you passed the exam!')

else:
    print('Sorry, you did not pass the exam this time')


print('Number correct: ',numcorrect)
print('Number incorrect: ', 20-numcorrect)
print('Questions missed: ', numwrong)

