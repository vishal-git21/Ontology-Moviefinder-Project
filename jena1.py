from rdflib import Graph, Namespace

def display_persons():
    # Create an RDF graph
    g = Graph()

    # Load the RDF data from file
    g.parse("data/Movies.rdf")

    # Define namespaces
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    owl = Namespace("http://www.semanticweb.org/owl/owlapi/turtle#")

    # Find individuals of the class "Person" or its subclasses
    persons = set(g.subjects(rdf.type, owl.Person))

    print("Persons:")
    # Print the local names of individuals
    for person in persons:
        print(person.split("#")[1])

if __name__ == "__main__":
    display_persons()
