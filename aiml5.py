#create a python script to demonstrate the use of basic probablity  notations including ,events ,outcomes, and values( taking dice as an example and user will give the 
#event that needs to take place place )

import random

# Sample space for a fair 6-sided dice
sample_space = {1, 2, 3, 4, 5, 6}
print("Sample Space (S):", sample_space)
print("Number of outcomes in S:", len(sample_space))

# Ask user for event type
print("\nChoose an event:")
print("1. Even numbers")
print("2. Odd numbers")
print("3. Number greater than 4")
print("4. Number less than 3")
print("5. Specific number (like 2 or 5)")

choice = int(input("Enter your choice (1-5): "))

# Define events based on user choice
if choice == 1:
    event = {2, 4, 6}
    event_name = "Even numbers"
elif choice == 2:
    event = {1, 3, 5}
    event_name = "Odd numbers"
elif choice == 3:
    event = {5, 6}
    event_name = "Numbers greater than 4"
elif choice == 4:
    event = {1, 2}
    event_name = "Numbers less than 3"
elif choice == 5:
    num = int(input("Enter the number you want (1-6): "))
    if num in sample_space:
        event = {num}
        event_name = f"Number {num}"
    else:
        print("Invalid number! Exiting.")
        exit()
else:
    print("Invalid choice! Exiting.")
    exit()

# Probability Calculation
probability = len(event) / len(sample_space)

# Show results
print(f"\nEvent Chosen (E): {event_name}")
print(f"Favorable Outcomes (E): {event}")
print(f"Number of outcomes in E: {len(event)}")
print(f"Probability P(E) = |E| / |S| = {len(event)} / {len(sample_space)} = {probability:.2f}")

# Optional: Simulate a dice roll
roll = random.choice(list(sample_space))
print("\nSimulating a dice roll...")
print("Dice rolled:", roll)
if roll in event:
    print("The event occurred ")
else:
    print("The event did not occur ")

