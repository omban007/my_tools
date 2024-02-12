import wikidata_sdk


def search_wikidata(question):
    # Search for entities based on the question
    search_results = wikidata_sdk.search_entities(question)

    if search_results:
        # Get the first entity from the search results
        entity_id = search_results[0]

        # Retrieve the entity data
        entity_data = wikidata_sdk.entity(entity_id)

        # Extract desired information from the entity data
        # For example, if you want the entity label and description:
        label = entity_data.get('labels', {}).get('en', {}).get('value', '')
        description = entity_data.get('descriptions', {}).get('en', {}).get('value', '')

        return label, description

    return None


# Example usage
question = "Who is the president of the United States?"
result = search_wikidata(question)
if result:
    label, description = result
    print(f"Label: {label}")
    print(f"Description: {description}")
else:
    print("No results found.")