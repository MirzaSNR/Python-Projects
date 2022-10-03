print("----------------- Cashier Program -----------------")
buyer= input("Enter Buyer's Name : ")
print ("Buyer's Name :", buyer) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Food Name -----------------")
   print("1. Fried Rice - Rp 15000")
   print("2. Soto - Rp 9000")
   print("3. Chicken Noodle - Rp 11000")
   nomor=int(input("Enter Choice : "))
   porsi= int(input("How Many Servings : "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," portion Fried Rice With Egg = Rp", totalmkn)
       mkn=("Fried Rice")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," portion Soto = Rp", totalmkn)
       mkn=("Soto")
   elif nomor==3:
       totalmkn=porsi*11000
       print (porsi, " portion Chicken Noodle = Rp", totalmkn)
       mkn=("Chicken Noodle")
   else:
      print("There is no option,Please Enter Again!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Drinks Menu -----------------")
   print("1. Iced Tea - Rp 2000")
   print("2. Orange Juice - Rp 3500")
   print("3. Ice Coffea - Rp 4000")
   nomor=int(input("Enter Option : "))
   gelas= int(input("How Many Glasses : "))

   if nomor==1:
       totalmnm=gelas*2000
       print (gelas," Iced Tea = Rp", totalmnm)
       mnm=(" Glass Iced Tea")
   elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, " Glass Orange Juice = Rp", totalmnm)
       mnm=("Orange Juice")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Glass Ice Coffea = Rp", totalmnm)
       mnm=("Ice Coffea")
   else:
      print("here is no option,Please Enter Again!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal Must be Paid: Rp",totalsemua)
uang=int(input("Buyer Cash : Rp "))
kembalian=int(uang-totalsemua)
print("Return :",kembalian)

print("\n==================================")
print("========== BUYER'S RECEIPT =========")
print("==================================")
print ("Name\t\t:",buyer)
print ("Buy\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Bill\t\t: Rp",totalsemua)
print ("Paid\t\t: Rp",uang)
print ("Return\t: Rp",kembalian)
print("==================================")
print("==================================")
