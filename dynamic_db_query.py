import os
import requests
from openai_service import OpenAiService

# TODO:
#  1. Develop a method to interact with an API.
#  2. Query the API to:
#     - Discover the database structure.
#     - Explore the schema of each table contained within the database.
#  3. Construct a prompt using the retrieved information to formulate a query via the OpenAI API.
#  4. Send the constructed prompt to the OpenAI API.
#  5. Utilize the response from the OpenAI API to extract relevant information from the database.