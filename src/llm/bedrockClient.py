from langchain_community.llms import FakeListLLM

def getLlm():
    print("🤖 Usando LLM fake para testes")
    responses = [
        "Baseado na documentação jurídica, isso é válido.",
        "Conforme a legislação brasileira, isso está correto.",
        "Os documentos indicam que isso é permitido por lei."
    ]
    return FakeListLLM(responses=responses)