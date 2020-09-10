# Author: Ismail Al Abdali ija5135@psu.edu
# Collaborator: Youngjae Bae yvb5135@psu.edu
# Collaborator: Jayesh Agarwala jpa5592@psu.edu
# Collaborator: Harshvardhan Singh hms5805@psu.edu
# Collaborator:Tylor Holman trh5481@psu.edu
# Section: 011R
# Breakout: 4

def getLetterGrade():
  grade = float(input("Enter your CMPSC 131 grade: "))
  if grade>= 93.0:
    g = "A"
  elif grade >= 90.0:
    g = "A-"
  elif grade >= 87.0:
    g = "B+"
  elif grade >= 83.0:
    g = "B"
  elif grade >= 80.0:
    g = "B-"
  elif grade >= 77.0:
    g = "C+"
  elif grade >= 70.0:
    g = "C"
  elif grade >= 60.0:
    rg = "D"
  elif grade < 60.0:
    g = "F"
  print(F"Your letter grade for CMPSC 131 is {g}.")
def run():
  getLetterGrade()
  
if __name__ == "__main__":
  run()