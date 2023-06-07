import copy
from llama_cpp import Llama

## load model -------------------------------------------------------
print( 'Loading model...' )
model_pth = '../models/ggml-vicuna-13b-4bit-rev1.bin'
print( f'model_path: {model_pth}' )
llm = Llama( model_path=model_pth )
print( 'model loaded.' )

## run model --------------------------------------------------------
print( 'Running model...' )
stream = llm( 
    'Question: Who is Ada Lovelace? Answer:',
    max_tokens=100,
    stop=["\n", "Question:", "Q:"],
    stream=True,
)

## print output -----------------------------------------------------

# for output in stream:
#     completion_fragment = copy.deepcopy( output )
#     # fragment = completion_fragment['choices'][0]['text']
#     fragment = completion_fragment.get('choices', [])[0]['text']
#     print( fragment )

# buffer = ""
# for output in stream:
#     completion_fragment = copy.deepcopy( output )
#     fragment = completion_fragment.get('choices', [])[0]['text']
#     buffer += fragment  # add fragment to buffer
#     if buffer and (buffer[-1] in {' ', ',', '.', '!', '?', ';', ':', '-'} or buffer[-1].isdigit()):
#         # print buffer and clear it when a space, punctuation, or digit is detected
#         print(buffer, end='')
#         buffer = ""

# buffer = ""
# for output in stream:
#     completion_fragment = copy.deepcopy( output )
#     fragment = completion_fragment.get('choices', [])[0]['text']
#     buffer += fragment  # add fragment to buffer
#     # print( f'buffer is now: {buffer}, and ends with, ``{buffer[-1]}' )
#     if buffer.endswith(' '): # if buffer ends with a space, print it and clear it
#         print(buffer, end='')
#         buffer = ""
# if buffer:  # print any remaining text in buffer
#     print( buffer )

buffer = ""
for output in stream:
    completion_fragment = copy.deepcopy( output )
    fragment = completion_fragment['choices'][0]['text']  # type: ignore
    buffer += fragment  # add fragment to buffer
    if not buffer[-1].isalnum():  # if the last character in buffer is not alphanumeric, print buffer
        print(buffer, end='')
        buffer = ""
if buffer:  # print any remaining text in buffer
    print(buffer)
