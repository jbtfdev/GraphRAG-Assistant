from dotenv import load_dotenv
from src.graph.graph_builder import GraphBuilder
from src.graph.entity import extract_entities
from src.graph.relations import extract_relations
import os

load_dotenv()

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")



builder = GraphBuilder(
    uri = uri,
    user = user,
    password =password
)

def process_chunk(chunk, chunk_id):
    entities = extract_entities(chunk)
    relations = extract_relations(chunk)

    for e in entities:
        name = e["entity"].lower().strip()
        type_= e["type"]
        builder.insert_entity(name, type_)


    for r in relations:
        source = r["source"].lower().strip()
        target = r["target"].lower().strip()
        relation = r["relation"].upper()

        builder.insert_relationship(source, relation, target)

    #for entities to chunk
    for e in entities:
        name=e["entity"].lower().strip()
        builder.link_chunk(name, chunk_id, chunk)

    
if __name__ == "__main__":
    chunk = "Chronic hyperglycemia is a hallmark of Type 2 Diabetes. Metformin is widely used to treat this condition, while lifestyle changes such as diet and exercise are also recommended to manage blood glucose levels."
    process_chunk(chunk, chunk_id=2)

    builder.close()