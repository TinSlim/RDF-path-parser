import main
import parseToNt
import time


def get_query(entidades,largo_camino):
	nodo_num = 0
	arista_num = 0
	querys = []
	lista_aristas = []
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
		lista_aristas.append(aristas)

	big_query = 'UNION\n'.join(querys)
	big_query = 'PREFIX wd: <http://www.wikidata.org/entity/> SELECT DISTINCT *\nWHERE{\n' + big_query + '}'
	#print(big_query)
	return big_query, lista_aristas

if __name__ == '__main__':
	entidad_1 = input("Primera entidad (ej wd:214): ")
	#entidad_1 = 'wd:Q13'
	entidad_2 = input("Segunda entidad (ej wd:214): ")
	#entidad_2 = 'wd:Q34'
	largo_camino = int(input("Largo máximo de los caminos (ej 3): "))
	print("\n\n")
	#print(get_query([entidad_1, entidad_2],largo_camino))
	endpoint_url = "http://192.168.0.136:9999/blazegraph/sparql"
	#t
	t1 = time.time()
	query, aristas = get_query([entidad_1, entidad_2],largo_camino)
	print(query)
	result = main.get_results(endpoint_url, query)
	#t
	t2= time.time()
	
	print("RESULTS BINDINGS:", result["results"]["bindings"], '\n')
	print("ARISTAS:", aristas, '\n')
	print("TIME ELAPSED:", t2-t1, "s","\n")
	parsed_to_nt = parseToNt.parse_to_nt(result["results"]["bindings"], aristas)
	parseToNt.to_nt_file(parsed_to_nt)
