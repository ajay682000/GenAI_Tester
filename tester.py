

from langchain_google_genai import ChatGoogleGenerativeAI



def write_test_function(code, api_key):
    llm = ChatGoogleGenerativeAI(
    google_api_key=api_key,
    model="gemini-pro"
    )
    template = f"""
You are a Software Developer. Your task is to write a unit test for the below Code unit the unittest.

Code: 
{code}

"""
    result = llm.invoke(template)
    result = result.content
    return result
    
