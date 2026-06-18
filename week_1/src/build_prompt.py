from typing import Dict, List

INSTRUCTIONS = """
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
"""

USER_PROMPT_TEMPLATE = """
Question:
{question}

Context:
{context}
"""


def build_context(search_results: List[Dict]) -> str:
    """Build an string context from the search results.

    Arguments:
        search_results: A list of dictionaries containing the search results.

    Returns:
        An string context built from the search results. It has the following format:
        Section 1
        Q: Question 1
        A: Answer 1
    """
    lines = []

    for doc in search_results:
        lines.append(doc["section"])
        lines.append("Q: " + doc["question"])
        lines.append("A: " + doc["answer"])
        lines.append("")

    return "\n".join(lines).strip()


def build_prompt(question: str, search_results: List[Dict]) -> str:
    context = build_context(search_results)
    prompt = USER_PROMPT_TEMPLATE.format(question=question, context=context)
    return prompt.strip()
