number = input("Enter to value: ")


if number >= 100:
	odd100 = number / 100
	odd100 = int(odd100)
	print ("NOTAS:")
	print ("{} nota(s) de R$ 100.00".format(odd100))
	mul100 = 100 * int(odd100)
	number = number - mul100
	#print (number)
else: 
	print ("NOTAS:")
	print ("0 nota(s) de R$ 100.00")

if  number >= 50:
	odd50 = number / 50
	odd50 = int(odd50)
        print ("{} nota(s) de R$ 50.00".format(odd50))
	mul50 = 50 * int(odd50)
	number = number - mul50
	#print (number)
else: 
        print ("0 nota(s) de R$ 50.00")

if number >= 20:
        odd20 = number / 20
	odd20 = int(odd20)
        print ("{} nota(s) de R$ 20.00".format(odd20))
        mul20 = 20 * int(odd20)
        number = number - mul20
        #print (number)
else:
        print ("0 nota(s) de R$ 20.00")

if number >= 10:
        odd10 = number / 10
	odd10 = int(odd10)
        print ("{} nota(s) de R$ 10.00".format(odd10))
        mul10 = 10 * int(odd10)
        number = number - mul10
        #print (number)
else:
        print ("0 nota(s) de R$ 10.00")

if number >= 5:
        odd5 = number / 5
	odd5 = int(odd5)
        print ("{} nota(s) de R$ 5.00".format(odd5))
        mul5 = 5 * int(odd5)
        number = number - mul5
        #print (number)
else:
        print ("0 nota(s) de R$ 5.00")

if number >= 2:
        odd2 = number / 2
        odd2 = int(odd2)
        print ("{} nota(s) de R$ 2.00".format(odd2))
        mul2 = 2 * int(odd2)
        number = number - mul2
        #print (number)
else:
        print ("0 nota(s) de R$ 2.00")

if number >= 1:
        odd1 = number / 1
	odd1 = int(odd1)
	print ("MOEDAS:")
        print ("{} moeda(s) de R$ 1.00".format(odd1)) 
        mul1 = 1 * int(odd1)
        number = number - mul1
        #print (number)
else:
	print ("MOEDAS:")
        print ("0 moeda(s) de R$ 1.00")

if number >= 0.50:
        odd05 = number / 0.50
        odd05 = int(odd05)
        print ("{} moeda(s) de R$ 0.50".format(odd05))
        mul05 = 0.50 * int(odd05)
        number = number - mul05
        #print (number)
else:
        print ("0 moeda(s) de R$ 0.50")

if number >= 0.25:
        odd025 = number / 0.25
        odd025 = int(odd025)
        print ("{} moeda(s) de R$ 0.25".format(odd025))
        mul025 = 0.25 * int(odd025)
        number = number - mul025
        #print (number)
else:
        print ("0 moeda(s) de R$ 0.25")

if number >= 0.10:
        odd01 = number / 0.10
        odd01 = int(odd01)
        print ("{} moeda(s) de R$ 0.10".format(odd01))
        mul01 = 0.10 * int(odd01)
        number = number - mul01
        #print (number)
else:
        print ("0 moeda(s) de R$ 0.10")

if number >= 0.05:
        odd005 = number / 0.05
        odd005 = int(odd1)
        print ("{} moeda(s) de R$ 0.05".format(odd005))
        mul005 = 0.05 * int(odd005)
        number = number - mul005
        #print (number)
else:
        print ("0 moeda(s) de R$ 0.05")

if number >= 0.01:
        odd001 = number / 0.01
        odd001 = int(odd001)
        print ("{} moeda(s) de R$ 0.01".format(odd001))
        mul001 = 0.01 * int(odd001)
        number = number - mul001
       #print (number)
else: 
	print ("0 moeda(s) de R$ 0.01")
