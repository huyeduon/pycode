def format_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


formatted_name = format_name(first_name="james", last_name="bond")
print(formatted_name)


def multiply(a,b):
    """Takes two numbers and multiplies them.
    Args:
    a (int): integer is passed
    b (int): another integer

    Returns:
    int: the product result
    """
    return a * b


print(multiply(5,6))

plants = ['lemon-tree','mango-tree', 'apple-tree']

def water_plants(plants):
    for plant in plants:
        action = f"Watering the {plant}"
        print(action)


water_plants(plants=plants)




def sum_numbers(*args):
    return sum(args)


print(f"The sum: ${sum_numbers(1,2,3)}")


def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info

print(build_profile("huyen","duong", location="SG"))














