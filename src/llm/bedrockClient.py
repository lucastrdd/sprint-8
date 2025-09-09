from langchain_aws import BedrockLLM

def getLlm():
    return BedrockLLM(
        model_id='amazon.titan-text-premier-v1:0',
        region_name='us-east-1',
        model_kwargs={'temperature': 0.3, 'maxTokenCount': 2048}
    )