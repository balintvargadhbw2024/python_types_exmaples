# Example 1: Creating a dictionary with key-value pairs
person_info = {'name': 'Alice', 'age': 25, 'gender': 'Female'}
print(person_info)

# Example 2: Accessing and modifying dictionary values
print(person_info['name'])  # Accessing value by key
person_info['age'] = 26  # Modifying value by key
print(person_info)

# Example 3: Dictionary comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print(squared_numbers)
