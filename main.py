from time import sleep
while 1:

  print('''What type are you going to work with?
  [1] Binary
  [2] Hexadecimal
  [3] Octal
  [4] Exit''')
  decision = int(input("Enter the decision: "))

  #Binary converter
  if decision == 1:

    print("-=-" *20)
    print('''What conversion will you do?
    [1] Decimal to binary
    [2] Binary to decimal''')
    decision = int(input("Enter the decision: "))

    #Decimal to Binary
    if decision == 1:
      print("-=-" *20)
      number = int(input("Enter the number for converter: "))
      print("The number {} decimal converted to binary = {}".format(number, bin(number)[2:]))

    #Binary to Decimal  
    elif decision == 2:
      print("-=-" *20)
      number = (input("Enter the number for converter: "))
      print("The number {} binary converted to decimal = {}".format(number, int(number, 2))) #Base 2 = Binary

  #Hexadecimal Converter
  elif decision == 2:
    print("-=-" *20)
    print('''What conversion will you do?
    [1] Decimal to hexadecimal
    [2] Hexadecimal to decimal''')
    decision = int(input("Enter the decision: "))

    #Decimal to Hexadecimal
    if decision == 1:
      print("-=-" *20)
      number = int(input("Enter the number for converter: "))
      print("The number {} decimal converted to hexadecimal = {}".format(number, hex(number)[2:]))

    #Hexadecimal to Decimal  
    elif decision == 2:
      print("-=-" *20)
      number = (input("Enter the number for converter: "))
      print("The number {} hexadecimal converted to decimal = {}".format(number, int(number, 16))) #Base 16 = Hexadecimal

  #Octal Converter
  elif decision == 3:
    print("-=-" *20)
    print('''What conversion will you do?
    [1] Decimal to octal
    [2] Octal to decimal''')
    decision = int(input("Enter the decision: "))

    #Decimal to Octal
    if decision == 1:
      print("-=-" *20)
      number = int(input("Enter the number for converter: "))
      print("The number {} decimal converted to octal = {}".format(number, oct(number)[2:]))

    #Octal to Decimal
    elif decision == 2:
      print("-=-" *20)
      number = (input("Enter the number for converter: "))
      print("The number {} octal converted to decimal = {}".format(number, int(number, 8))) #Base 8 = Octal

  #Close program
  elif decision == 4:
    break

  print("-=-" *20)
  sleep(2) #Pause for 2 seconds before next task
