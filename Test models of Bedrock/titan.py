
import boto3
import json

bedrock_runtime = boto3.client(service_name="bedrock-runtime")

prompt = """
Act as a Shakespeare and write a poem on Genertaive AI
"""

body = json.dumps({
    "inputText": prompt, 
    "textGenerationConfig":{  
        "maxTokenCount":256,
        "stopSequences":[],
        "temperature":0,
        "topP":0.9
    }
})

response = bedrock_runtime.invoke_model(
    body=body,
	modelId="amazon.titan-text-premier-v1:0",
    accept="application/json", 
    contentType="application/json"
)

response_body = json.loads(response.get('body').read())
print(response_body.get('results')[0].get('outputText'))