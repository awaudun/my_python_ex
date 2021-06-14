
current_number = 30
total_numb = 100
bar_length = 10

num_equals = int(bar_length * current_number / total_numb)
equals = "=" * num_equals
spaces = " " * (bar_length - num_equals - 1)
print(f"|{equals}>{spaces}|")
