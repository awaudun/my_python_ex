students = ["tonje andersen","rasmus andreasson","alland atroshi","troels bjornskov","Robert flytoren","fredrik harberg","alexis kan","susan klingsell","kristoffer laursen","maria skripova","audun soberg"]
stud_cop = students.copy()

print(len(students))
print(students[2])
print(students[2][0])

## 1d
third = students[2].split()
students[2] = "Ole " + " ".join(third[1:])
print(students[2])

## 1e
third = students[2].split()
students[2] = " ".join(third[:1]) + " Nordmann"
print(students[2])

## 1f
print(len(students))
students.append(stud_cop[2])
print(students)
print(len(students))

## 1g
students.insert(4, "Monty Python")
print(students)

## 1h
print(len(students))
students.remove("Ole Nordmann")
print(len(students))

## 1i
print(students.index("Monty Python"))

## 1j
print(students[:3])

## 1k
students_reverse = students[::-1] ##list(reversed(students))
print(students_reverse)

## 1l
students_even = students[::2]
print(students_even)

## 1m
students_odd = students[1::2]
print(students_odd)

print("-------------------------------------------------------")

## 2
import random
dice = [1,2,3,4,5,6]
n_dices = 5
rand_dices = random.choices(dice, k = n_dices)
print(rand_dices)
if max(rand_dices) == min(rand_dices):
    print("Yahtzee!!!")
else:
    print("Not Yahtzee.")
print(sorted(rand_dices))

print("-------------------------------------------------------")

## 4

list_of_lists = [1,[2,3,"4"], [5, [6, "7", 8], 9, 10]]
print(list_of_lists)
list_of_lists[1][2] = 4
list_of_lists[2][1][1] = 7
print(list_of_lists)

