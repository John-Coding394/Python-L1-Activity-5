Amount =int(input("please Enter Amount for Withdraw :"))
note_1 = Amount//100
print(note_1)
note_2 = (Amount%100)//50
print(note_2)
note_3 = ((Amount%100)%50)//10
print(note_3)
print("notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)