#User Input with Validation
name = input("Enter your name: ")

#Ensure age is an integer
while True:
    try:
        age = int(input("Enter your age: "))
        break  # Break the loop if conversion to int is successful
    except ValueError:
        print("Please enter a valid integer for age.")

#Ensure location contains only words and numbers
while True:
    location = input("Enter your location: ")
    if location.isalnum():
        break  # Break the loop if location contains only words and numbers
    else:
        print("Please enter a location with only letters and numbers.")

#Personalized Message
message = f"Hello {name}, you are {age} years old and live in {location}."

print(message)
