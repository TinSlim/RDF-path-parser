
entidades = ["m1","m2"]




largo_camino = 1

def get_query(entidades,largo_camino):
	nodo_num = 0
	arista_num = 0
	querys = []
	x = 0
	while x< (2**largo_camino):

		text = bin(x)[2:].zfill(largo_camino)
		#print(text) # Bits combinaciones

		aristas = [entidades[0]]
		for arista in range(largo_camino):
			aristas.append(f"?e{arista_num}")
			arista_num+=1
			if (len(aristas) == largo_camino * 2):
				break
			aristas.append(f"?n{nodo_num}")
			nodo_num+=1
		aristas.append(entidades[1])
		act_query = ""
		for letter,index in zip(text,range(largo_camino)):
			actuals = aristas[index*2:(index*2)+3]
			if letter == '0':
				act_query += f"{actuals[0]} {actuals[1]} {actuals[2]}. \n"
			else:
				act_query += f"{actuals[2]} {actuals[1]} {actuals[0]}. \n"
		
		act_query = "{\n"+act_query+"}\n"
		querys.append(act_query)
		#print(act_query)
		x+=1

	big_query = 'UNION\n'.join(querys)
	big_query = 'SELECT DISTINCT *\nWHERE{\n' + big_query + '}'
	#print(big_query)
	return big_query

if __name__ == '__main__':
	print("ok")
	entidad_1 = input("Primera entidad (ej wd:214): ")
	entidad_2 = input("Segunda entidad (ej wd:214): ")
	largo_camino = int(input("Largo máximo de los caminos (ej 3): "))
	print("\n\n")
	print(get_query([entidad_1, entidad_2],largo_camino))

