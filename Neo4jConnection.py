import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            records = [record.data() for record in result]
            summary = result.consume()
            return records, summary

# load_dotenv()
# uri = os.getenv("NEO4J_URI")
# user = os.getenv("NEO4J_USER")
# password = os.getenv("NEO4J_PASSWORD")
#
# conn = Neo4jConnection(uri, user, password)
#
# try:
#     conn.query("CREATE (n:TestNode {name: 'Test'}) RETURN n")
#
#     result, _ = conn.query("MATCH (n:TestNode {name: 'Test'}) RETURN n.name AS name")
#     print("Node created, name:", result)
#
# except Exception as e:
#     print("Error occurred:", e)
#
# conn.close()