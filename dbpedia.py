from SPARQLWrapper import SPARQLWrapper, JSON

# Set up the SPARQL endpoint
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

# Query string
query = """
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX dbc: <http://dbpedia.org/resource/Category:>
    SELECT DISTINCT ?uri
    WHERE {
        ?uri dct:subject dbc:Assassins_of_Julius_Caesar
    }
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