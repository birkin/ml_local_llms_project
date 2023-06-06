from llama_cpp import Llama

## load model -------------------------------------------------------
print( 'Loading model...' )
model_pth = '../models/ggml-vicuna-13b-4bit-rev1.bin'
print( f'model_path: {model_pth}' )
llm = Llama( model_path=model_pth )
print( 'model loaded.' )


