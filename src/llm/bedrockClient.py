from langchain_aws import BedrockLLM

def getLlm():
    return BedrockLLM(
        model_id='amazon.titan-embed-text-v2:0',
        region_name='us-east-2',
        model_kwargs={'temperature': 0.3, 'maxTokenCount': 2048}
    )