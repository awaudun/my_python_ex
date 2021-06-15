
## 1a
var_1, var_2, var_3 = (4,7,2)
print(var_1, var_2, var_3)
## 1b
var_1, var_2 = (var_2, var_1)
print(var_1, var_2, var_3)
## 1c
var_1, var_3 = var_3, var_1
print(var_1, var_2, var_3)

## 2a
captured = ("Pikachu", "Pidgey", "Abra", "Pidgey", "Eevee", "Pidgey")
print(captured)
## 2b
## It is probably better to use tuple since we want to keep the order.
## 2c
print("num Pidgeys: ", captured.count("Pidgey"))
## 2d
print("Abra" in captured) ## input("pokemon name: ") in captured)
captured_set = set(captured)
print(len(captured), len(captured_set))

