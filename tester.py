import llms

llm = llms.llm

def write_test_function(code):
    template = f"""
You are a Software Developer. Your task is to write a unit test for the below Code unit the unittest.

Code: 
{code}

"""
    result = llm.invoke(template)
    result = result.content
    return result
    
