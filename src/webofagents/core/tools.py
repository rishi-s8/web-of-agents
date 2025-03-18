from smolagents import Tool

class AgentSearch(Tool):
    name = "agent_search"
    description = """
    Given a query, returns the name of the best expert.
    This tool should be used to get more specialized and accurate answers for particular domains.
    It returns a string with the expert's identifier. You can use the identifier as expert_name in the expert_agent tool. The expert_name should not be modified and used as is.
    If it returns unknown, the system should provide a general answer.
    """
    inputs = {
        "query": {
            "type": "string",
            "description": "The domain-specific question or a sentence containing keywords that can be used to identify the domain expert."
        }
    }
    output_type = "string"

    def forward(self, query: str):
        q_lower = query.lower()
        if any(word in q_lower for word in ["medical", "health", "cancer", "disease", "immunotherapy", "medicine"]):
            return "medical_expert"
        elif any(word in q_lower for word in ["computer", "software", "programming", "algorithm", "hardware", "data"]):
            return "cs_expert"
        else:
            return "unknown"

class AskAgent(Tool):
    name = "ask_agent"
    description = """
    Given an expert_name and a query, asks the expert_agent for the answer to the query.
    This expert agent specializes in the domain and hence is better suited to answer the queries of the respective domains.
    This tool should be used to get more specialized and accurate answers for particular query domains of which a generic agent or an LLM may not have sufficient information.
    While this agent is supposedly domain expert, it still requires a detailed query to provide an accurate answer. So, do not hide stuff from the expert and create a very detailed query.
    It returns a string that is the answer to the query as given by a domain specialist.
    If the given expert_name is unavailable, the system should verify the expert_name. If the expert_name was incorrect, query again with the correct expert_name. Otherwise, give a general answer from the personal knowledge.
    """
    inputs = {
        "expert_name": {
            "type": "string",
            "description": 'The identifier of the expert (e.g., "medical_expert" or "cs_expert"). This should be the correct expert_identifier, either known in advance or exactly as returned by the agent_search tool.'
        },
        "query": {
            "type": "string",
            "description": 'The domain-specific question to ask the expert. The query should be as detailed as possible to get a good answer.'
        }
    }
    output_type = "string"

    def __init__(self, expert_dict, *args, **kwargs):
        self.expert_dict = expert_dict
        assert "medical_expert" in self.expert_dict, "medical_expert not found in expert_dict."
        assert "cs_expert" in self.expert_dict, "cs_expert not found in expert_dict."
        super().__init__(*args, **kwargs)

    def forward(self, expert_name: str, query: str):
        if expert_name in self.expert_dict:
            return self.expert_dict[expert_name].run(query)
        else:
            return "No suitable expert found for the query."
