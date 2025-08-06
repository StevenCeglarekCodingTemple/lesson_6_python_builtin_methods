user_input = "  Hello, World!  "

# user_input_stripped = user_input.strip()

print(f"Original: '{user_input}'")
print(f"Stripped: '{user_input.strip()}'")  # Removes whitespace from both ends of a String
print(f"Lower: '{user_input.lower()}'")
print(f"Upper: '{user_input.upper()}'")
print(f"Title: '{user_input.title()}'")

clean_input = user_input.strip().title()
print(f"Cleaned: '{clean_input}'")

# Real-World Example: Clean user names
names = ["   alice SMITH ", "BOB Jones", "   Charlie Brown   "]
cleaned_names = []
for name in names:
    clean_name = name.strip().title()
    cleaned_names.append(clean_name)
print("Cleaned Names: ", cleaned_names)

sentence = "Python is amazing and Python is fun and Python is powerful"

# Finding and Counting
print(f"Count of 'Python': {sentence.count('Python')}")
print(f"First 'is' at position: {sentence.find('is')}")
print(f"Last 'is' at position: {sentence.rfind('is')}")

# Checking string properties
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'powerful': {sentence.endswith('powerful')}")
print(f"Contains 'amazing': {'amazing' in sentence}")

# Replacing text
new_sentence = sentence.replace("Python", "Programming")
# new_sentence = sentence.replace(" ", "") How to get rid of all spaces in a string
print(f"Replaced: {new_sentence}")

# Replace only first occurrence
first_only = sentence.replace("Python", "Programming", 1)
print(f"First only: {first_only}")

# Validation examples
username = "alice123"
email = "user@example.com"
print(f"Username is alphanumeric: {username.isalnum()}")  # .isdigit() 
print(f"Contains @ symbol: {'@' in email}")

# Function to process CSV-like data
def parse_person_data(data_line):
    """Parse a CSV line into person information"""
    fields = data_line.split(",")
    if len(fields) >= 4:
        name, age, job, city = fields[:4]
        return {
            "name": name.strip().title(),
            "age": age.strip(),
            "job": job.strip().title(),
            "city": city.strip().title()
        }
    return None

# Function to format person information
def format_person(person_data):
    """Format person adta into a readable string"""
    if person_data:
        return f"{person_data['name']} ({person_data['age']}) works as {person_data['job']} in {person_data['city']})"
    return "Invalid Data"

# Function to create shopping list display
def format_shopping_list(items, separator=", "):
    """Create a formatted shopping list string"""
    if not items:
        return "No items in list"
    return f"Shopping list: {separator.join(items)}"

# Using our functions
data_line = "john doe,25,engineer,new york"
person = parse_person_data(data_line)
print("Parsed person:", person)
print("Formatted:", format_person(person))

shopping_items = ["milk", "bread", "eggs", "cheese"]
print(format_shopping_list(shopping_items))
print(format_shopping_list(shopping_items, " | "))
print(format_shopping_list(shopping_items, " - "))

# Process multiple people
people_data = [
    "alice smith,30,teacher,boston",
    "bob jones,25,developer,seattle",
    "charlie brown,35,doctor,chicago"
]

print("\nProcessed people:")
for data in people_data:
    person = parse_person_data(data)
    print(format_person(person))