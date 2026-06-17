people = [
{"ten" : "manh" , "number" : "0832651683"},
 {"ten" : "phin" , "number" : "0354247456"}
]
name = input("dien ten : ")
for person in people :
 if person["ten"] == name :
  print(f"sdt la {person['number']}")
  break
 else : 
  print("khong tim thay")
       