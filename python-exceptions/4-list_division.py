#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                print("wrong type")
                result_list.append(0)
                continue

            result = num1 / num2
        
        except IndexError:
            print("out of range")
            result_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except Exception as e:
            print("wrong type")
            result_list.append(0)
        else:
            result_list.append(result)
        finally:
            print("Finally block executed")

    return result_list
