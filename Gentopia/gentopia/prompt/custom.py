from gentopia.prompt import *
from gentopia import PromptTemplate
from tool import GoogleSearch

class GoogleSearchPrompt(PromptTemplate):
   
    def handle_search_query(self, query):
        search_tool = GoogleSearch()
        search_results = search_tool._run(query)
        return search_results

    def generate_response(self, query):
        if 'search' in query:
            return self.handle_search_query(query)
