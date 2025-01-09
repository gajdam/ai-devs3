import os
import pandas as pd
import requests
from dotenv import load_dotenv
from neo4j import GraphDatabase


def fetch_data_from_api(api_url, payload):
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def prepare_data():
    connections_payload = {
        "task": "database",
        "apikey": hq_apikey,
        "query": "select * from connections"
    }

    users_payload = {
        "task": "database",
        "apikey": hq_apikey,
        "query": "select * from users"
    }
    users_data = fetch_data_from_api(api_url, users_payload)
    connections_data = fetch_data_from_api(api_url, connections_payload)

    users_df = pd.DataFrame(users_data["reply"])
    connections_df = pd.DataFrame(connections_data["reply"])

    # Save to CSV files instead of Excel
    users_df.to_excel("users.xlsx", index=False, engine="openpyxl")
    connections_df.to_excel("connections.xlsx", index=False, engine="openpyxl")


def import_csv_to_neo4j(df):
    neo_uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(neo_uri, auth=('neo4j', '20Vn3grs24!'))

    def create_relationships(tx, user1_id, user2_id):
        query = """
            MERGE (u1:User {id: $user1_id})
            MERGE (u2:User {id: $user2_id})
            MERGE (u1)-[:KNOWS]->(u2)
        """
        tx.run(query, user1_id=user1_id, user2_id=user2_id)

    with driver.session() as session:
        for _, row in df.iterrows():
            session.execute_write(create_relationships, row['user1_id'], row['user2_id'])
    driver.close()


def find_shortest_path_to_node(driver, start_id, end_id):
    query = """
    MATCH (start:User {id: $start_id}), (end:User {id: $end_id}),
    p = shortestPath((start)-[:KNOWS*]-(end))
    RETURN p
    """
    with driver.session() as session:
        result = session.run(query, start_id=start_id, end_id=end_id)
        path = result.single()
        if path:
            return path["p"]
        else:
            return None


load_dotenv()
hq_apikey = os.getenv("HEADQUARTERS_API_KEY")
api_url = "https://centrala.ag3nts.org/apidb"
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

# prepare_data() - loading data from api

# creating database
# df2 = pd.read_excel(r'./connections.xlsx')
# print(df2.columns)  # Print column names to debug
# import_csv_to_neo4j(df2)

driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
path = find_shortest_path_to_node(driver, 28, 39)  # change to get_user_id(Rafał), get_user_id(Barbara)

if path:
    print(f"Shortest route from 28 to 39:", [node["id"] for node in path.nodes])
else:
    print("Shortest route not found")

driver.close()


