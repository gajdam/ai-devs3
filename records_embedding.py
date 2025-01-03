import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams

from openai_service import OpenAiService


def load_reports(folder_path):
    reports = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as f:
                reports.append({"content": f.read(), "file_name": file_name})
    return reports


def create_vector_database(qdrant_host, qdrant_api_key, collection_name, embedding_dim):
    client = QdrantClient(
        url=qdrant_host,  # Cloud instance URL
        api_key=qdrant_api_key  # API key for authentication
    )
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=embedding_dim,  # Vector dimension
            distance="Cosine"  # Metric for similarity
        )
    )
    return client


def add_reports_to_database(client, openai_client: OpenAiService, collection_name, reports):
    points = []
    for idx, report in enumerate(reports):
        embedding = openai_client.generate_embedding(report["content"])
        metadata = {"file_name": report["file_name"]}
        points.append(PointStruct(id=idx, vector=embedding, payload=metadata))
    client.upsert(collection_name=collection_name, points=points)


def search_database(client, openai_client: OpenAiService, collection_name, query, top_k=1):
    query_embedding = openai_client.generate_embedding(query)
    results = client.search(
        collection_name=collection_name,
        query_vector=query_embedding,
        limit=top_k
    )
    return results


def main(folder_path, openai_service: OpenAiService, qdrant_host, qdrant_api_key, collection_name="weapons_tests"):
    print("Loading reports from folder...")
    reports = load_reports(folder_path)
    print(f"Found {len(reports)} reports.")

    print("Creating vector database...")
    embedding_dim = 1536  # Dimension of the embedding for text-embedding-ada-002
    client = create_vector_database(qdrant_host, qdrant_api_key, collection_name, embedding_dim)

    print("Generating embeddings and adding reports to the database...")
    add_reports_to_database(client, openai_service, collection_name, reports)

    print("Creating query and searching the database...")
    query = "In the report, from which day is there mention of a weapon prototype theft?"
    results = search_database(client, openai_service, collection_name, query, top_k=1)

    if results:
        best_match = results[0]
        print(f"Best result: {best_match.payload}")
        return best_match.payload.get("file_name", "No date found")
    else:
        print("No search results found.")
        return "No results found"


if __name__ == "__main__":
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")

    qdrant_host = "https://b9ec3a8f-20a4-4bf3-aae1-972121a12b54.us-east4-0.gcp.cloud.qdrant.io:6333"

    openai_service = OpenAiService(openai_key)
    folder_path = r"C:\Users\gajda\Downloads\pliki_z_fabryki\weapons_tests\do-not-share"
    result = main(folder_path, openai_service, qdrant_host, qdrant_api_key)
    print(f"Report date with theft: {result}")
