import os
from dotenv import load_dotenv
from src.graph.db import Neo4jDB


load_dotenv()
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")


class GraphRetriever:
    def __init__(self, uri, user, password):
        self.db = Neo4jDB(uri, user, password)

    def get_graph_chunks(self, entity_name):
        query = """
        MATCH (e: Entity {name: $name})-[r]-(neighbour)
        MATCH (neighbour)-[:MENTIONED_IN]->(c:Chunk)
        RETURN c.text
        LIMIT 5
        """
        result = list(self.db.run_query(query, {"name": entity_name}))

        return [record["c.text"] for record in result]
    
    def close(self):
        self.db.close()
