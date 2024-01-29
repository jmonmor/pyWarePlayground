from googlesearch import search

def google_search(query, num_results=5):
  """
  Perform a Google search and return a list of results.

  Parameters:
  - query (str): The search query.
  - num_results (int): Number of search results to retrieve (default is 5).

  Returns:
  - List of search results.
  """
  search_results = []

  try:
    # Perform Google search
    for result in search(query, num_results=num_results, stop=num_results):
        search_results.append(result)

    return search_results

  except Exception as e:
    print(f"An error occurred: {e}")
    return None
    