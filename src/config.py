import os
wand_db_username = os.environ.get("WANDDB_USERNAME")

config = {
    'project': "llmapps",
    'entity': None,
    'job_type': "production",
    'vector_store_artifact': f"{wand_db_username}/llmapps/vector_store:latest",
    'model_name':"gpt-3.5-turbo",
    'chat_temperature': 0.3,
    'max_fallback_retries': 1
}