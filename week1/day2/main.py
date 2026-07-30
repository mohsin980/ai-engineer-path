skills = ["Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS"]
print("first skill:", skills[0]) # Python

user = {"name": "John", "age": 20, "city": "New York"}
print("user name:", user["name"]) # John

skills.append("React")
print("Last skill:", skills[-1]) # ["Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "React"]

languages = {"English", "Urdupani", "Hindi", "Punjabi"}
print("languages:", languages) # {"English", "Urdupani", "Hindi", "Punjabi"}

numbers = [1, 2, 3, 4, 5]
print("double numbers:", [n * 2 for n in numbers]) # [2, 4, 6, 8, 10]

print("even numbers: ", [n for n in numbers if n % 2 == 0]) # [2, 4]

print("odd numbers:", [n for n in numbers if n % 2 != 0]) # [1, 3, 5]