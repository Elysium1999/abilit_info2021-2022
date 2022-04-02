	#Dichiaro le variabili con il typecasting esplicito
	int1 = 7
	int2 = 45
	flt1 = 76.2
	flt2 = -2.65.1
	com1 = 2. + 3.j
	com2 = complex("-5+7.j")
	boo1 = bool(3) #-> True
	boo2 = False
	str1 = "j"
	str2 = str(2.+3.j)

	#Operazioni fra int
	print("\nOperazioni fra int")
	print("somma:\t\t", int1+int2)
	print("modulo:\t\t", int1%int2 )

	#Operazioni fra float
	print("\nOperazioni fra float")
	print("divisione:\t", flt1/flt2 )

	#Operazioni fra complessi
	print("\nOperazioni fra complessi")
	print("divisione:\t", com1/com2 )
	print("somma:\t\t", com1+com2)

	#Operazioni fra booleani
	print("\nOperazioni fra booleani")
	print("OR:\t\t\t", boo1 or boo2 )
	print("AND:\t\t", boo1 and boo2)
	print("NAND:\t\t", not(boo1 and boo2 ))

	#Operazioni fra stringhe
	print("\nOperazioni fra stringhe")
	print("'Somma':\t", str2+str1)
	print("'Sottrazione':\t", str2.replace(str1,''))
	#print("NAND:\t\t", not(boo1 and boo2 ))

	#Typecasting implicito
	print("\nOperazioni logiche su numeri")
	print("AND fra numeri - secondo dei due numeri:\t")
	print("45 - (7 and 45):\t",int2 - (int1 and int2))
	print("NOT(com1):\t", not(com1))
	print("NOT(-1):\t", not (-1) )
	print("7 + True:\t",7 + True)
	
	print("\nOperazioni fra numeri di tipi diversi")
	print("7+76.2:\t", int1+flt1)
	print("76.2 + 2+3j:\t", flt1+com1)
