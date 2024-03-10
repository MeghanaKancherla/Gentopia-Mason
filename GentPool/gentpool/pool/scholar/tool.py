### Define your custom tool here. Check prebuilts in gentopia.tool (:###
from gentopia.tools import *
from gentopia.tools.google_search import GoogleSearch

class GoogleSearchTest(PromptTemplate):
   
    def handle_search_query(self, query):
        search_tool = GoogleSearch()
        search_results = search_tool._run(query)
        return search_results

    def generate_response(self, query):
        if 'search' in query:
            return self.handle_search_query(query)
