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

#to_parse = ['wd:22','?e0','?n0','?e1','wd:33']
#print({to_parse[index*2 +1] : to_parse[index*2:(index*2)+3] for index in range(2)})

dict = {'?e1': ['wd:22','?e0','?n0'], '?e2': ['?n0','?e1','wd:33']}
# reccorrer el diccionario resultado
for row in resultado:
  #print(row)
  for key in row.keys():
    if (dict.get('?'+key)):
      try:
        v0 = dict['?'+key][0] if (':' in dict['?'+key][0]) else row[dict['?'+key][0].replace('?','')]['value']
        v1 = dict['?'+key][1] if (':' in dict['?'+key][1]) else row[dict['?'+key][1].replace('?','')]['value']
        v2 = dict['?'+key][2] if (':' in dict['?'+key][2]) else row[dict['?'+key][2].replace('?','')]['value']
        filas.append([v0,v1,v2])
      except:
        pass
print(filas)