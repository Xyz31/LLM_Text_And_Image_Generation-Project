# Getting Response from API in this file
import replicate
import os
import requests

# key = "Paste your Api Key here"
key = "r8_WEfoC4wjmOWO09WTedGMfCdPXWaB6GN0BQqdb"
os.environ["REPLICATE_API_TOKEN"] = key

temperature = 0.4
prob = 0.5
maxlength = 200

# generate text from api
def generateTextFromApi(user_prompt: str) ->str:
    # Prompts
    pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    prompt_input = "How I can Learn LLms. Give Roadmap?"

    # Generate LLM response
    # LLM model
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
            input={"prompt": f"{pre_prompt} {user_prompt} Assistant: ", # Prompts
                    "temperature":temperature, "top_p":prob, "max_length":maxlength, "repetition_penalty":1})  # Model par

    full_response = ""
    for item in output:
        full_response += item

    return full_response


#generate image from Api
def generateImageFromApi(user_prompt: str) ->str:
    # For Image Generation

    ai_image_link = replicate.run(
        "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
        input={"text": "a beautifull nature Image"}
    )
    
    return ai_image_link
