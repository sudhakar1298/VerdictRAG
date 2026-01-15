from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

def argue(claim, docs_for, docs_against):
    llm = ChatOllama(model="llama3:latest")

    def join(docs):
        return "\n\n".join(d.page_content for d in docs)

    prompt = f"""
You are a legal reasoning assistant.

User claim:
"{claim}"

Evidence supporting the claim:
{join(docs_for)}

Evidence opposing the claim:
{join(docs_against)}

Rules:
- Use only the provided evidence.
- Do not invent facts.
- If evidence is weak or conflicting, say so.
- Present both sides fairly.
- End with a balanced conclusion.

Structure:
1. Arguments Supporting the Claim
2. Arguments Against the Claim
3. Conclusion
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
