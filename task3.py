my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
First_ = 0
while First_ < len(my_list) :
    number = my_list[First_]
    First_ = First_ + 1
    if number == 0 :
        continue
    elif number < 0 :
        break
    elif First_ == len(my_list) :
        print(number)
    else:
        print(number)
