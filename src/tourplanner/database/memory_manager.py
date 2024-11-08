from .neo4j_connection import Neo4jConnection

# Initialize the Neo4j connection
db_connection = Neo4jConnection()

def store_user_preference(user_id, preference_type, preference_value):
    """
    Store user preferences in the Neo4j database.
    """
    query = """
    MERGE (u:User {id: $user_id})
    MERGE (p:Preference {type: $preference_type, value: $preference_value})
    MERGE (u)-[:PREFERS]->(p)
    RETURN p
    """
    params = {
        "user_id": user_id,
        "preference_type": preference_type,
        "preference_value": preference_value
    }
    return db_connection.query(query, params)

def retrieve_user_preferences(user_id):
    """
    Retrieve user preferences from the Neo4j database.
    """
    query = """
    MATCH (u:User {id: $user_id})-[:PREFERS]->(p:Preference)
    RETURN p.type AS type, p.value AS value
    """
    params = {"user_id": user_id}
    return db_connection.query(query, params)

def close_connection():
    """
    Close the Neo4j connection.
    """
    db_connection.close()