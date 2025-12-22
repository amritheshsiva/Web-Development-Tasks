try:
  name=input("Enter Name :")
  feedback=input("Enter Feedback :")
  if not name or not feedback:
    raise ValueError("Name and feedback cannot be empty.")
  print("Thanks for the feedback!")
  print("Name:", name)
  print("Feedback:", feedback)

except ValueError as i:
    print("Error:", i)
    
finally:
  print("Feedback system closed safely.")