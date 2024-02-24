from owlready2 import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
FILE_NAME = config.get('AGENT', 'FILE_NAME')

obj = "Criminal"

my_world = owlready2.World()
my_world.get_ontology(FILE_NAME).load()  # path to the owl file is given here

sync_reasoner_hermit(my_world)
graph = my_world.as_rdflib_graph()
# result = list(graph.query("Select ?p WHERE {?p <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://test.org/"+FILE_NAME+"#"+obj+">.}"))

result = list(graph.query("Construct {:Colonel_West  a  ?x} WHERE {:Colonel_West  a  ?x}"))

res_def = []

for element in result:
    e = str(element).split("'")[1]
    e_final = e.split("#")[1].split(".")
    final = ".".join(e_final[:-1])
    res_def.append(final)

print("\nReasoning: ", res_def)


