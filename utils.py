from llm import ask_llm

def self_check(document):
    prompt = f"""
 Review the following document.

 Correct grammar.

 Improve formatting.

 Return improved version.

 {document}

 """
    return ask_llm(prompt)
