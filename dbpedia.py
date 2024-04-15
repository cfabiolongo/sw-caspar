from SPARQLWrapper import SPARQLWrapper, JSON

# Set up the SPARQL endpoint
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

# Query string
query = """
PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX res: <http://dbpedia.org/resource/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?uri WHERE { ?uri dbo:publisher res:GMT_Games }
"""

# Set the query string
sparql.setQuery(query)

# Set the return format to JSON
sparql.setReturnFormat(JSON)

# Execute the query and convert results to JSON
results = sparql.query().convert()

# Print the results
for result in results["results"]["bindings"]:
    print(result["uri"]["value"])