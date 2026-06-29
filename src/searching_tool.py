from minsearch import Index


def fit_docs(
    docs, text_fields=["question", "section", "answer"], keyword_fields=["course"]
):
    index = Index(text_fields=text_fields, keyword_fields=keyword_fields)

    index.fit(docs)

    return index


def search(question, index, course="llm-zoomcamp"):
    boost_dict = {"question": 2.0, "section": 0.5}
    filter_dict = {"course": course}

    return index.search(
        question, boost_dict=boost_dict, filter_dict=filter_dict, num_results=5
    )
