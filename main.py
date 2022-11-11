# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON
import certifi
import ssl

endpoint_url = "https://query.wikidata.org/sparql"

query = """SELECT DISTINCT *
WHERE 
{
  {wd:Q54314 ?a1 wd:Q32045.}
  UNION
  {wd:Q32045 ?a2 wd:Q54314.}
  UNION
  {  
  wd:Q54314 ?a3 ?n1.
  ?n1 ?a6 wd:Q32045.
  }
  UNION
  {
  ?n2 ?a5 wd:Q54314.
  wd:Q32045 ?a4 ?n2.
  }

  
}
"""


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent,context=ssl.create_default_context(cafile=certifi.where()))
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)
