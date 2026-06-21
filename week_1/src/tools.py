from typing import Dict, List

from langchain_core.tools import tool
from sqlitesearch import TextSearchIndex


@tool
def search(query: str) -> List[Dict]:
    """Search the FAQ database for entries matching the given query.
    Args:
        query: Search query text to look up in the course FAQ.
    Returns:
        List[Dict]: List of documents that are relevant to the query
    """
    boost_dict = {"question": 3.0, "section": 0.5}
    filter_dict = {"course": "llm-zoomcamp"}

    index = TextSearchIndex(
        text_fields=["question", "section", "answer"],
        keyword_fields=["course"],
        db_path="faq.db",
    )
    try:
        results = index.search(
            query, num_results=5, boost_dict=boost_dict, filter_dict=filter_dict
        )
    finally:
        index.close()

    return results
