#FERTILIZANTE
hectarea=float(input("ingrese cantidad de hectarea: "))
comp=float(input("ingrese cantidad de compuesto en %: "))
matorral=(input("hay matorral? si/no: "))
compuesto=hectarea*comp
if compuesto >=10 and matorral== "no":
	print("es factible la utilizacion de fertilizantes")
else:
	print("no es factible la utilizacion de fertilizantes")