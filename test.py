entidades = ["m1","m2"]
vals = []

nodo_num = 0
arista_num = 0


largo_camino = 3

query = ''

vals = []
x = 0
while x< (2**largo_camino):

	text = bin(x)[2:].zfill(largo_camino)
	print(text)

	aristas = [entidades[0]]
	for arista in range(largo_camino):
		aristas.append(f"e{arista_num}")
		arista_num+=1
		if (len(aristas) == largo_camino * 2):
			break
		aristas.append(f"n{nodo_num}")
		nodo_num+=1
	aristas.append(entidades[1])
	print(aristas)
	act_query = ""
	for letter,index in zip(text,range(largo_camino)):
		actuals = aristas[index*2:(index*2)+3]
		if letter == '0':
			act_query += f"{actuals[0]} {actuals[1]} {actuals[2]}. \n"
		else:
			act_query += f"{actuals[2]} {actuals[1]} {actuals[0]}. \n"
	print(text)
	print(act_query)
	print("&&&&")
	x+=1

