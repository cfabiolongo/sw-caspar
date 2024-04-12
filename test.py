from owlready2 import *

FILE_NAME = "west.owl"
obj = "Criminal"

# Lettura della query da query.txt
with open("query.txt", "r") as f:
    q = f.read()

my_world = owlready2.World()
my_world.get_ontology(FILE_NAME).load()  # path to the owl file is given here

sync_reasoner_pellet(my_world, infer_property_values = True)

graph = my_world.as_rdflib_graph()

# p = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> "
# p = p + "PREFIX : <http://test.org/west.owl#> "

# Estrazione degli appartenenti alla clsse Colonel_West
# q = p + "SELECT ?c WHERE { ?c rdf:type :Criminal. }"

# Estrazione degli elementi con property hadAdj
# q = q+" SELECT ?individual ?adjective WHERE {?individual :hasAdj ?adjective.}"

# q = q + "SELECT ?s ?p ?o WHERE {  ?s rdf:type/rdfs:subClassOf* :Verb. ?s ?p ?o.}"

#q = q + "SELECT ?i ?s ?o WHERE { ?verb rdf:type/rdfs:subClassOf* :Verb. ?i rdf:type ?verb. ?i :hasSubject ?s. ?i :hasObject ?o.}"

# q = p + "SELECT ?s ?i ?o WHERE {  ?i rdf:type/rdfs:subClassOf* :Verb.  ?i :hasSubject ?s.  ?i :hasObject ?o. }"

result = list(graph.query(q))

print(len(result))

print("\nResult: ", result)


res_def = []

""" for e in result:        
    chunk = str(e).split(",")
    
    c1 = chunk[0].split("#")[1]
    c2 = chunk[1].split("#")[1]
    c3 = chunk[2].split("#")[1]
    
    c1 = c1.split(".")[0]
    c2 = c2.split(".")[0]
    c3 = c3.split(".")[0]
    
    print(f"\nelement: {c2}({c1}, {c3})")
    print("---------------------------------------") """