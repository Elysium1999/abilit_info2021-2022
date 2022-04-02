	#moto rettilineo uniforme
	x0 = float(input('posizione iniziale:    '))
	v  = float(input('velocità:     '))
	t  = float(input("tempo: "))
	x = v*t + x0
	print("x(t) = ",x,"\n")

	#moto rettilineo uniformemente accelerato
	x0 = float(input('posizione iniziale:    '))
	v0 = float(input('velocità iniziale:       '))
	a = float( input('accelerazione:   '))
	t  = float(input("tempo: "))
	x =  .5 * a * t**2 + v*t + x0
	print("x(t) = ",x)
