# # Task 1

def calculate (num1 , num2 , op= "add"):
  op = op.lower()
  if op in ("d","add"):
    return num1 + num2
  elif op in ("s","sub"):
    return num1 - num2
  elif op in ("m", "multibly"):
    return num1 * num2
  else:
    print("operation not found")

print(calculate (5 , 6, "d")) 
print(calculate(4 , 8, "s"))


# Task 2

def addition (*numbers):
  result = 0
  for num in numbers:
    if num == 10:
      continue
    elif num ==5:
      result -= num
    else:
      result += num

  return result    
print(addition(10,5,3,4,))


# Task 3

def show_skills(name,*skill):
  if len(skill)>0:
    print(f"hello {name} your skills is :")
    for skills in skill:
      print(f"- {skills}")
  else:
    print(f"hello {name} you has not skills")
    
show_skills("osama","python","html","css")
show_skills("ahmed")


# Task 4

def say_hello(name="unknown",age="unknown",country="unknown"):
  print(f"hello {name} your age is {age} and you live in {country}")
  
say_hello("Osama",30,"Egypt")  
say_hello()
