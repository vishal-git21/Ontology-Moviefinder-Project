from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

def load_ontology_and_display_persons():
    # Create an RDF graph
    g = Graph()

    # Load the RDF data from file
    g.parse("data/Movies.rdf")

    # Define namespaces
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    owl = Namespace("http://www.semanticweb.org/owl/owlapi/turtle#")

    # Prepare the SPARQL query
    query_file = "data/person_query.ttl"
    with open(query_file, "r") as file:
        query_text = file.read()

    query = prepareQuery(query_text, initNs={"rdf": rdf, "owl": owl})
    
    # Execute the query and display results
    print("Persons:")
    for row in g.query(query):
        print(row.person.split("#")[1])

if __name__ == "__main__":
    load_ontology_and_display_persons()
