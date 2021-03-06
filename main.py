# Author: Ismail Al Abdali ija5135@psu.edu
# Collaborator: Youngjae Bae yvb5135@psu.edu
# Collaborator: Jayesh Agarwala jpa5592@psu.edu
# Collaborator: Harshvardhan Singh hms5805@psu.edu
# Collaborator:Tylor Holman trh5481@psu.edu
# Section: 011R
# Breakout: 4

def getLetterGrade(grade):
  if (grade>= 93.0):
    return "A"
  elif (grade >= 90.0):
    return "A-"
  elif (grade >= 87.0):
    return "B+"
  elif (grade >= 83.0):
    return "B"
  elif (grade >= 80.0):
    return "B-"
  elif (grade >= 77.0):
    return "C+"
  elif (grade >= 70.0):
    return "C"
  elif (grade >= 60.0):
    return "D"
  elif (grade < 60.0):
    return "F"
  
def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  g = getLetterGrade(grade)
  print(F"Your letter grade for CMPSC 131 is {g}.")
if __name__ == "__main__":
  run()