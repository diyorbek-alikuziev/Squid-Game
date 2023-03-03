print("Kalmar o'yiniga xush kelibsiz!")
play = input("O'yinni boshlash uchun istalgan tugmani bosing: ")
if play:
  question1 = input("1-savol: 6 + 83 + 297 + 3729 + 92734 = ?    a)96899  b)96849  c)96829 >>> ").lower()
  if question1 == "b":
    print("to'g'ri topdingiz davom eting")
    question2 = input("2-savol: 72942 - 9457 - 568 - 89 - 3 = ?    a)62821  b)62829  c)62825 >>> ").lower()
    if question2 == "c":
      print("to'g'ri topdingiz davom eting")
      question3 = input("3-savol: 2 * 7 * 9 * 41 * 73 = ?    a)379118  b)373118  c)377118 >>> ").lower()
      if question3 == "c":
        print("to'g'ri topdingiz davom eting")
        question4 = input("4-savol: 99999 / 1111 / 111 / 11 / 1 = ?    a)0.07471  b)0.07371  c)0.07771 >>> ").lower()
        if question4 == "b":
          print("to'g'ri topdingiz davom eting")
          question5 = input("5-savol: 23 * 62 / 25 * 13 / 84 * 14 = ?    a)123.5866  b)682.0832  c)344.1224 >>> ").lower()
          if question5 == "a":
            print("to'g'ri topdingiz va siz $5 mlrd yutib oldingiz, karta raqamingizni yuboring!")
            card = input("card number: >>> ")
            print("Mazzami sizga mazzami 😂")
          else:
            print("Siz o'ldingiz!")
        else:
          print("Siz o'ldingiz!")
      else:
        print("Siz o'ldingiz!")
    else:
      print("Siz o'ldingiz!")
  else:
    print("Siz o'ldingiz!")
