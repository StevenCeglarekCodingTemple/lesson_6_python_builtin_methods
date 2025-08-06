# Starting with an empty list
shopping_cart = []
print("Empty Cart: ", shopping_cart)

# Adding single Items
shopping_cart.append("milk")
shopping_cart.append("bread")
print("After append: ", shopping_cart)

# Adding at a specific position
shopping_cart.insert(0, "eggs")
shopping_cart.insert(2, "cheese")
print("After Insert: ", shopping_cart)


# Adding Multiple Items
more_items = ["butter", "yogurt"]
shopping_cart.extend(more_items)
print("After extend: ", shopping_cart)

# Removing Items
shopping_cart.remove("bread")
print("After Remove: ", shopping_cart)

# Pop (removes and returns)
last_item = shopping_cart.pop()
print(f"Removed: {last_item}")
print("Car Now: ", shopping_cart)

first_item = shopping_cart.pop(0)
print(f"Removed: {first_item}")
print("Cart Now: ", shopping_cart)


# Function to calculate comprehensive statistics
def analyze_scores(scores):
    """Calculate comprehensive statistics for a list of scores"""
    if not scores:
        return "No scores to analyze"
    
    stats = {
        "count": len(scores),
        "total": sum(scores),
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
        "range": max(scores) - min(scores)
    }
    
    return stats

def categorize_scores(scores, passing_grade=70):
    """Categorize scores into passing and failing"""
    passing = []
    failing = []

    for score in scores:
        if score >= passing_grade:
            passing.append(score)
        else:
            failing.append(score)
    
    return {
        "passing": passing,
        "failing": failing,
        "pass_rate": len(passing) / len(scores) * 100 if scores else 0
    }
    

# Function to get top performers
def get_top_performers(scores, names, top_n=3):
    """Get the top N performers with their names"""
    if len(scores) != len(names):
        return "Error: Scores and names lists must be the same length"
    
    # Combine scores and names, then sort by score
    combined = list(zip(names, scores))
    combined.sort(key=lambda x: x[1], reverse=True)
    
    return combined[:top_n]

# Using our functions
test_scores = [85, 92, 78, 95, 88, 76, 90]
student_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]

# Analyze the scores
stats = analyze_scores(test_scores)
print("Score Statistics:")
for key, value in stats.items():
    if key == "average":
        print(f"  {key.title()}: {value:.1f}")
    else:
        print(f"  {key.title()}: {value}")

# Categorize performance
categories = categorize_scores(test_scores)
print(f"\nPassing scores: {categories['passing']}")
print(f"Failing scores: {categories['failing']}")
print(f"Pass rate: {categories['pass_rate']:.1f}%")

# # Get top performers
top_students = get_top_performers(test_scores, student_names)
print("\nTop 3 performers:")
for i, (name, score) in enumerate(top_students, 1):
    print(f"  {i}. {name}: {score}")


# Checking list contents
students = ["Alice", "Bob", "Diana", "Charlie"]
print("Students: ", students)

# Membership testing
print(f"Is 'Alice' in class: {'Alice' in students}")
print(f"Is 'Eve' in class: {'Eve' in students}")

# Safe Operations
def safe_remove(lst, item):
    if item in lst:
        lst.remove(item)
        return f"Removed: {item}"
    else:
        return f"{item} not Found"

print(safe_remove(students, "Bob"))
print(safe_remove(students, "Eve"))
print("Students Now: ", students)

# Mixed list with mixed data
mixed_list = [1, "hello", 2.5, True, [1, 2, 3]]
print("Mixed List: ", mixed_list)

# Filter by type
numbers_only = []
strings_only = []

for item in mixed_list:
    if isinstance(item, (int, float)) and not isinstance(item, bool):
        numbers_only.append(item)
    elif isinstance(item, str):
        strings_only.append(item)

print("Numbers: ", numbers_only)
print("Strings: ", strings_only)

# Clear all elements
test_list = [1, 2, 3, 4, 5, 6]
print("Before clear: ", test_list)
test_list.clear()
print("After clear: ", test_list)


# Basic math functions
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

# Working with different data types
prices = [19.99, 25.50, 12.75, 8.25]
print("\nPrices:", prices)
print(f"Total cost: ${sum(prices):.2f}")
print(f"Cheapest: ${min(prices):.2f}")
print(f"Most expensive: ${max(prices):.2f}")

# Math functions on strings (length)
words = ["python", "programming", "is", "fun"]
print("\nWords:", words)
print(f"Word count: {len(words)}")
print(f"Longest word: {max(words, key=len)}")
print(f"Shortest word: {min(words, key=len)}")

# Rounding and absolute values
values = [3.14159, -2.7, 4.999, -10.1]
print("\nOriginal values:", values)
print("Rounded:", [round(x, 2) for x in values])
print("Absolute values:", [abs(x) for x in values])


# enumerate() - get index and value
fruits = ["apple", "banana", "orange"]
print("Using Enumerate: ")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    
print("\nWith custom Start")
for position, fruit in enumerate(fruits, start=1):
    print(f"#{position}: {fruit}")

# zip() - combine multiple list
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Orlando", "Miami"]

print("\n Using zip:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}) lives in {city}")
    
# Creating a list of tuples
combined = list(zip(names, ages))
print("Combined List: ", combined)

# Sorting with numbers
numbers = [3, 1, 2, 5, 7, 9, 4, 5, 2]
print("Original: ", numbers)
print("Sorted: ", sorted(numbers))
print("Reverse: ", sorted(numbers, reverse=True))

# Sorting strings
words = ["python", "java", "javascript", "go"]
print("\nWords: ", words)
print("Alphabetical: ", sorted(words))
print("By length: ", sorted(words, key=len))
print("By length (desc): ", sorted(words, key=len, reverse=True))

# type() and isinstance()
sample_data = [42, "hello", 3.14, True, [1, 2, 3]]
print("\n Type Checking")
for item in sample_data:
    print(f"{item} is {type(item).__name__}")
    
# isinstance for safe type checking
print("\nFiltering by type:")
numbers_only = [x for x in sample_data if isinstance(x, (int, float)) and not isinstance(x, bool)]
strings_only = [x for x in sample_data if isinstance(x, (str))]

# Same as above
# for x in sample_data:
#     if isinstance(item, (int, float)) and not isinstance(item, bool):
#         numbers_only.append(item)
#     elif isinstance(item, str):
#         strings_only.append(item)
        
print("Numbers: ", numbers_only)
print("Strings", strings_only)

# any() and all()
test_scores = [85, 92, 78, 95, 69]
print(f"\nAll scores >= 70: {all(score >= 70 for score in test_scores)}")
print(f"\nAny score >= 90: {any(score >= 90 for score in test_scores)}")

# range() for generating sequences
print("\nUsing Range: ")
print("Range(5):", list(range(5)))
print("Range(2, 8):", list(range(2, 8)))
print("Range(0, 10, 2):", list(range(0, 11, 2)))