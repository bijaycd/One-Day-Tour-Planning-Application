from .neo4j_connection import Neo4jConnection

# Initialize the Neo4j connection
db_connection = Neo4jConnection()

def get_attractions(city):
    """
    Fetch popular attractions in a specified city from the database.
    """
    query = """
    MATCH (a:Attraction {city: $city})
    RETURN a.name AS name, a.type AS type, a.description AS description
    """
    params = {"city": city}
    return db_connection.query(query, params)

def store_itinerary(user_id, itinerary):
    """
    Store an itinerary in the Neo4j database for a specific user.
    """
    query = """
    MERGE (u:User {id: $user_id})
    WITH u
    UNWIND $itinerary AS item
    MERGE (i:Itinerary {name: item.name, time: item.time})
    MERGE (u)-[:HAS_ITINERARY]->(i)
    RETURN i
    """
    params = {
        "user_id": user_id,
        "itinerary": itinerary  # itinerary should be a list of dictionaries, each with `name` and `time`
    }
    return db_connection.query(query, params)

def close_connection():
    """
    Close the Neo4j connection.
    """
    db_connection.close()