from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

# Load the RDF data
g = Graph()
g.parse("data/Movies.rdf")

# Define namespaces
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
ont = Namespace("http://www.semanticweb.org/owl/owlapi/turtle#")

# Read the name of the movie
movie_name = input("Enter the name of the movie: ")
# Query RDF graph for movie information
query_text = """
SELECT ?year ?country ?genre ?actor
WHERE {
    ?movie rdf:type ont:Movie ;
           rdfs:label ?title .
    OPTIONAL { ?movie ont:hasYear ?year }
    OPTIONAL { ?movie ont:hasCountry ?country }
    OPTIONAL { ?movie ont:hasGenre ?genre }
    OPTIONAL { ?movie ont:hasActor ?actor }
    FILTER (?title = "%s")
}

""" % movie_name

query = prepareQuery(query_text, initNs={"rdf": rdf, "ont": ont , "rdfs": rdfs})
results = g.query(query)

# Check if any results are found
if len(results) == 0:
    print("Movie not found in the database.")
else:
    # Display the results
    for row in results:
        year, country, genre, actor = row
        if year:
            print("Year:", year)
        else:
            print("Year: Not available")
        if country:
            print("Country:", country)
        else:
            print("Country: Not available")
        if genre:
            print("Genre:", genre.split("#")[1])
        else:
            print("Genre: Not available")
        if actor:
            print("Actor:", actor.split("#")[1])
        else:
            print("Actor: Not available")
