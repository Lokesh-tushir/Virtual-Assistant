import wikipedia

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results