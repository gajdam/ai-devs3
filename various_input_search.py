# TODO:
#     1. Read the text file (.txt) and store its content in a variable.
#     2. Send the content of the file to OpenAI API as the prompt, asking it to identify the people mentioned in the text and their connections (relationships).
#     3. Parse the API response to extract the names of people and their associated connections.
#     4. For each recognized person, send a request to the /people API endpoint to retrieve the cities associated with each person.
#     5. Parse the API response for each person to extract the list of cities.
#     6. For each city, send a request to the /places API endpoint to get information about that city (e.g., description, notable places, etc.).
#     7. Collect and store the information about each city for further use.
#     8. Compile all of the extracted information (people, cities, and city information) and include it in the prompt context.
#     9. Ask OpenAI API about the whereabouts of "Barbara" based on the gathered context (people, cities, places).
