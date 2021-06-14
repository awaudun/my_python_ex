##punichment_text = "You are not my good friend!"
punichment_text = input("Type in your punichment text here: ")
numb_of_repetition = int(input("How many times do you want it typed? "))

num_that = punichment_text.lower().count("that")
punichment_text = punichment_text.replace("not", "")
punichment_text = punichment_text.replace("good", "bad")

print((punichment_text + "\n") * numb_of_repetition)
print(f"The occurrence of the word THAT in the original sentence is: {num_that}")