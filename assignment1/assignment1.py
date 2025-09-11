#task 1, function that returns Hello!

def hello():
  return 'Hello!'

#print('worked!')


#task 2, Greet function

def greet(name):
  return (f"Hello, " + name + "!")

print(greet('John'))

# task 3, calculation functions

def calc(a, b, operation='multiply'):
  try:
     match operation:
       case 'add':
         return a + b
       
       case 'subtract':
         return a - b
       
       case 'multiply':
         return a * b
       
       case 'divide':
         return a / b
       
       case 'modulo':
         return a % b
       
       case 'int_divide':
         return a // b
       case 'power':
         return a ** b
       case _:
         return "Invalid input"
  except ZeroDivisionError:
    return "You can't divide by 0!"
  except TypeError: 
        return "You can't multiply those values!"
print(calc(4, 2, 'add'))



  #task 4, Data type conversion
        
def data_type_conversion(value, converted_type):
  try:
    match converted_type:
       case 'int':
         return int(value)     
       case 'float':
         return float(value)
       case "str":
         return str(value)
  except ValueError:
    return f"You can't convert {value} into a {converted_type}."
  except TypeError:
        return "Invalid value is passed for conversion"
  

print(data_type_conversion("123", 'int'))
print(data_type_conversion("10", 'float'))
print(data_type_conversion('123', 'str'))
print(data_type_conversion("John", 'int'))



  
#task 5, Grading System - *args

def grade(*scores):
  try:
    avg = sum(scores) / len(scores)
  
    if avg >= 90:
      return "A"
    
    elif avg >= 80:
      return "B"
    
    elif avg >= 70:
      return "C"
    
    elif avg >= 60:
      return "D"
    
    else:
      return "F"
    
  except TypeError:
      return "Invalid data was provided."
print(grade(100, 100, 100))



#task 6, for loop with a Range

def repeat(text, count):
  result = []
  for _ in range(count):
    result.append(text)
  return "".join(result)
print(repeat("up", 4))


#task 7, **kwargs
def student_scores(option, **kwargs):

    if option == 'best':
      return max(kwargs, key = kwargs.get)
    elif option == 'mean':
      return sum(kwargs.values()) / len(kwargs)
    else:
      return "Invalid entry"
  
print(student_scores("mean", Tom=75, Dick=89, Angela=91))

# task 8, Titleize, with String and List Operations

def titleize(text):
  little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
  words = text.split()
  result = []
  for i, word in enumerate(words):
    if i == 0 or i == len(words) -1 or word.lower() not in little_words:
      result.append(word.capitalize())
    else:
      result.append(word.lower())
  return " ".join(result)

print(titleize('book and pen'))

# task 9, Hangman, with more String Operations

def hangman(secret, guess):
  result = []
  for letter in secret:
    if letter in guess:
      result.append(letter)
    else:
      result.append('_')
  return "".join(result)

hangman("hello", "llo")


#Task 10, Pig Latin, Another String Manipulation Exercise


def pig_latin(string):
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    for word in string.split():
        print(word[:2])
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word):
                if word[i] in vowels:
                    # Handle "qu" together if it appears before the first vowel
                    if i > 0 and word[i - 1] == "q":
                        result.append(word[i + 1:] + word[:i + 1] + "ay")
                    else:
                        result.append(word[i:] + word[:i] + "ay")
                    break
                i += 1
    return " ".join(result)