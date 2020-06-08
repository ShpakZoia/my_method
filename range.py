my_list = [a for a in range(20, 87)]
def my_numbers():
    even_numbers = []
    for number in my_list:
        if number % 2 == 0:
            even_numbers.append(number)
            return even_numbers

print(my_numbers())
