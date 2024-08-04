from owlready2 import *

# Load the ontology
onto = get_ontology("data/Movies.rdf").load()

# Get the namespace of the ontology
namespace = onto.get_namespace("http://www.semanticweb.org/owl/owlapi/turtle#")

# Function to get the full "namespace#name" form of a class or property
def get_full_name(entity):
    return "%s%s" % (entity.namespace.base_iri, entity.name)

# Define the rule
with onto:
    hasActor = get_full_name(namespace.hasActor)
    person = get_full_name(namespace.Person)
    actor = get_full_name(namespace.Actor)
    
    class Actor(Thing):  # Specify Actor as a subclass of Thing
        pass
    rule = Imp()
    rule.set_as_rule(person+"(?p), "+actor + "(?p), "+hasActor + "(?m, ?p) -> Actor(?p)")

print("Rules:")
for rls in onto.rules():
    print(rls)

# Run the reasoner
sync_reasoner_pellet(infer_property_values=True)

# Retrieve inferred individuals
Actor = list(onto.Actor.instances())
print("Actor individuals:")
for actor in Actor:
    print(actor)