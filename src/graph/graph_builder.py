from src.graph.db import Neo4jDB


class GraphBuilder:
    def __init__(self, uri, user, password):
        self.db = Neo4jDB(uri, user, password)

        
    def close(self):
        self.db.close()

    def insert_entity(self,name, type_):
        query = """
        MERGE (e:Entity {name: $name})
        SET e.type = $type
        """
        self.db.run_query(query, {"name":name, "type":type_})


    def insert_relationship(self, source, relation, target):
        query = f"""
        MATCH (a:Entity {{name: $source}})
        MATCH (b:Entity {{name: $target}})
        MERGE (a)-[:{relation}]->(b)
        """
        self.db.run_query(query, {"source": source, "target": target})


    def link_chunk(self, entity, chunk_id, text):
        query = """
        MERGE (c:Chunk {id: $chunk_id})
        SET c.text = $text
        WITH c
        MATCH (e:Entity {name : $entity})
        MERGE (e)-[:MENTIONED_IN]->(c)
        """
        self.db.run_query(query,{
            "entity": entity,
            "chunk_id": chunk_id,
            "text": text
        })