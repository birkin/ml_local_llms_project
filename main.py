import json
from llama_cpp import Llama

## load model -------------------------------------------------------
print( 'Loading model...' )
model_pth = '../models/ggml-vicuna-13b-4bit-rev1.bin'
print( f'model_path: {model_pth}' )
llm = Llama( model_path=model_pth )
print( 'model loaded.' )

## run model --------------------------------------------------------
print( 'Running model...' )
output = llm( 
    'Question: Who is Ada Lovelace? Answer:',
    max_tokens=100,
    stop=["\n", "Question:", "Q:"],
    echo=True,
)

## print output -----------------------------------------------------
output_jsn = json.dumps( output, sort_keys=True, indent=2 )
print( f'output_jsn, ``{output_jsn}``' )