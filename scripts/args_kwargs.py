def area_rectangle(length=0, width=0):
    return length*width


def area_polycube(*args):
    result = 1
    for item in args:
        result *= item
    return result


def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


if __name__ == '__main__':
    my_polycube_tuple = (1, 2, 3, 4, 5, 6)
    my_polycube_list = [1, 2, 3, 4, 5, 6]
    my_dict = {
        "name": "Kay",
        "age": 26,
    }
    print(f"Result with input as a tuple: {area_polycube(*my_polycube_tuple)}")
    print(f"Result with input as a list: {area_polycube(*my_polycube_list)}")
    print_dict(**my_dict)
