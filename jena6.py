from owlready2 import *

# Load the ontology
onto = get_ontology("data/Movies.rdf").load()

# Get the namespace of the ontology
namespace = onto.get_namespace("http://www.semanticweb.org/owl/owlapi/turtle#")

# Function to get the full "namespace#name" form of a class or property
def get_full_name(entity):
    return "%s%s" % (entity.namespace.base_iri, entity.name)

# Define the rules
with onto:
    hasGenre = get_full_name(namespace.hasGenre)
    hasActor = get_full_name(namespace.hasActor)
    movie = get_full_name(namespace.Movie)
    actor = get_full_name(namespace.Actor)
    
    genre = get_full_name(namespace.Genre)
    crime_genre = "http://www.co-ode.org/ontologies/ont.owl#Crime"
    action_genre = "http://www.co-ode.org/ontologies/ont.owl#Action"
    thriller_genre = "http://www.co-ode.org/ontologies/ont.owl#Thriller"
    
    class Movie(Thing):  # Specify Movie as a subclass of Thing
        pass
    class ActionThrillerMovie(Thing):  # Specify ActorDirector as a subclass of Thing
        pass
    class ThrillerCrimeMovie(Thing):  # Specify MoviesWithActors as a subclass of Thing
        pass
    class CrimeMovie(Thing):  # Specify CrimeMovie as a subclass of Thing
        pass
    class ThrillerMovie(Thing):  # Specify ThrillerMovie as a subclass of Thing
        pass
    class Actors(Thing):  # Specify MaleActors as a subclass of Thing
        pass

    rule1 = Imp()
    rule1.set_as_rule(movie + "(?m), "+hasGenre + "(?m,"+action_genre+"), " + hasGenre + "(?m, "+thriller_genre+") -> ActionThrillerMovie(?m)")

    rule2 = Imp()
    rule2.set_as_rule(movie + "(?m), "+hasGenre + "(?m, "+crime_genre+") -> CrimeMovie(?m)")

    rule3 = Imp()
    rule3.set_as_rule(movie + "(?m), "+hasGenre + "(?m, "+thriller_genre+") -> ThrillerMovie(?m)")

    rule_all_movies = Imp()
    rule_all_movies.set_as_rule(movie + "(?m) -> Movie(?m)")

    rule_actors = Imp()
    rule_actors.set_as_rule(movie + "(?m), "+hasActor + "(?m, ?p), " +actor + "(?p) -> Actors(?p)")

print("Rules:")
for rls in onto.rules():
    print(rls)

# Run the reasoner
sync_reasoner_pellet(infer_property_values=True)

# Retrieve inferred things
Movie = list(onto.Movie.instances())
ActionThrillerMovie = list(onto.ActionThrillerMovie.instances())
CrimeMovie = list(onto.CrimeMovie.instances())
ThrillerMovie = list(onto.ThrillerMovie.instances())
Actors = list(onto.Actors.instances())

print("ActionThrillerMovie Movies:")
for actionThrillerMovie in ActionThrillerMovie:
    print(actionThrillerMovie)
print("="*20)

print("CrimeMovie Movies:")
for crimeMovie in CrimeMovie:
    print(crimeMovie)
print("="*20)

print("ThrillerMovie Movies:")
for thrillerMovie in ThrillerMovie:
    print(thrillerMovie)
print("="*20)

print("Movies:")
for movie in Movie:
    print(movie)
print("="*20)

print("Actors:")
for actor in Actors:
    print(actor)