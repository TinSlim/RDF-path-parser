filas = []

resultado = [{'n0': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q113005365'},
'e1': {'type': 'uri', 'value': 'http://www.wikidata.org/prop/direct/P1038'},
'e0': {'type': 'uri', 'value': 'http://www.wikidata.org/prop/direct/P40'}},

{'e3': {'type': 'uri', 'value': 'http://schema.org/description'}, 
'n1': {'xml:lang': 'ar', 'type': 'literal', 'value': 'ممثل أسترالي'}, 
'e2': {'type': 'uri', 'value': 'http://schema.org/description'}},

{'e3': {'type': 'uri', 'value': 'http://schema.org/description'},
'n1': {'xml:lang': 'ca', 'type': 'literal', 'value': 'actor australià'},
'e2': {'type': 'uri', 'value': 'http://schema.org/description'}}]



aristas_dict = {'?e1': ['wd:22','?e0','?n0'], '?e2': ['?n0','?e1','wd:33']}
to_parse = ['wd:22','?e0','?n0','?e1','wd:33']
# reccorrer el aristas_dict resultado
def parse_to_nt(resultado, to_parse):
  aristas_dict = {}
  for row_arista in to_parse:
    for index in range((len(row_arista) - 1) // 2):
      aristas_dict[row_arista[index*2 +1]] = row_arista[index*2:(index*2)+3]
  #aristas_dict = {to_parse[index*2 +1] : to_parse[index*2:(index*2)+3] for index in range(2)}
  print("DICCIONARIO: ", aristas_dict, '\n')
  for row in resultado:
    #print(row)
    for key in row.keys():
      if (aristas_dict.get('?'+key)):
        try:
          v0 = aristas_dict['?'+key][0] if (':' in aristas_dict['?'+key][0]) else row[aristas_dict['?'+key][0].replace('?','')]['value']
          v1 = aristas_dict['?'+key][1] if (':' in aristas_dict['?'+key][1]) else row[aristas_dict['?'+key][1].replace('?','')]['value']
          v2 = aristas_dict['?'+key][2] if (':' in aristas_dict['?'+key][2]) else row[aristas_dict['?'+key][2].replace('?','')]['value']
          if (('wd:' in v0) or ('wikidata.org/entity' in v0)) and (('wd:' in v1) or ('wikidata.org/prop/direct' in v1)) and (('wd:' in v2) or ('wikidata.org/entity' in v2)):
            filas.append([v0,v1,v2])
        except:
          pass
  #print(filas)
  return filas

def to_nt_file(filas):

  with open('output.nt', 'w') as f:
    for fila in filas:
      v0 = fila[0].replace('wd:', 'http://www.wikidata.org/entity/')
      v2 = fila[2].replace('wd:', 'http://www.wikidata.org/entity/')
      f.write('<{}> <{}> <{}> .\n'.format(v0, fila[1], v2))