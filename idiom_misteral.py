from llama_cpp import Llama

from flask import Flask, render_template, request, redirect, url_for
import json

#flask app for aour misteral llm
app = Flask(__name__)

@app.route('/', methods=['GET'])
def idiom_simplifier():
    #for our purpose we read from a file
    with open('prompt.txt', 'r') as file:
        lines = file.readlines()
        file_contents = ''.join(lines)

    print(f"input.txt contents:\n{file_contents} \n ")

    # Set gpu_layers to the number of layers to offload to GPU.
    #Set to 0 if no GPU acceleration is available on your system.
    llm = Llama(
        model_path="./misteral/mistral-7b-instruct-v0.2.Q6_K.gguf",  # Download the model file first
        n_ctx=32768,  # The max sequence length to use -
                      #note that longer sequence lengths require much more resources
        n_threads=8,            # The number of CPU threads to use,
                                #tailor to your system and the resulting performance
        n_gpu_layers=35         # The number of layers to offload to GPU,
                                #if you have GPU acceleration available
)

    # Simple inference example
    output = llm(
        "<s>[INST] {prompt} [/INST]", # Prompt
        max_tokens=64,   # Generate up to 512 tokens
        stop=["</s>"],   # Example stop token -
                         #not necessarily correct for this specific model! Please check before using.
        echo=True          # Whether to echo the prompt
    )

    # Chat Completion API

    # Set chat_format according to the model you are using
    llm = Llama(model_path="./misteral/mistral-7b-instruct-v0.2.Q6_K.gguf", chat_format="llama-2")  
    
    result=llm.create_chat_completion(
        messages = [
                    {"role": "system", "content": "You are an English Language idiom and expression simplifier."},
                    {
                                    "role": "user",
                                    "content": f""" simplify the following text and
                                                    only give the equivelent text ready for translation: 
                                                    '{file_contents}' """
                                }
                ]
    )
    #for production it would be better to return the json
    return result["choices"][0]["message"]["content"]


if __name__=="__main__":
    app.run(port=5000,debug=True)

