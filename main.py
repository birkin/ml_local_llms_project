import copy, logging, time
from llama_cpp import Llama

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger( '__name__' )

## load model -------------------------------------------------------
log.debug( 'Loading model...' )
model_pth = '../models/ggml-vicuna-13b-4bit-rev1.bin'
log.debug( f'model_path: {model_pth}' )
llm = Llama( model_path=model_pth )
log.debug( 'model loaded.' )

## ask user for input and store it to variable ----------------------
user_input = input( 'Your input (hit return when done): ' )
log.debug( f'user_input, ``{user_input}``' )

## run model --------------------------------------------------------
log.debug( 'Running model...' )

stream = llm( 
    f'Question: {user_input} Answer:',
    max_tokens=100,
    stop=["\n", "Question:", "Q:"],
    stream=True,
)

# stream = llm( 
#     'Question: Who is Ada Lovelace? Answer:',
#     max_tokens=100,
#     stop=["\n", "Question:", "Q:"],
#     stream=True,
# )

## print output -----------------------------------------------------
"""
I really wanted the output to appear word-by-word, but print() by default includes an ending newline.
Trying print( 'the_text', end='' ) doesn't work, because the output is internally-buffered until the newline is printed.
But this is ok; it shows that streaming the output is possible.
For the web, some front-end js could be used to print the output word-by-word in teletype fashion.
"""
buffer = ""
for output in stream:
    # log.debug( f'output, ``{output}``' )
    completion_fragment = copy.deepcopy( output )
    fragment = completion_fragment['choices'][0]['text']  # type: ignore
    buffer += fragment  # add fragment to buffer
    # log.debug( f'buffer before if, ``{buffer}``' )
    if ' ' in buffer:
        # log.debug( 'about to print segment' )
        # log.debug( f'buffer, ``{buffer}``' )
        # print( buffer, end='' )
        print( buffer)
        # print( 'foo' )
        # log.debug( 'segment printed' )
        buffer = ""
        # time.sleep( .25 )
if buffer:  # print any remaining text in buffer
    log.debug( f'remaining buffer, ``{buffer}``' )
    print(buffer)
    
log.debug( 'model run complete.' )

## tutorial ---
# for output in stream:
#     completion_fragment = copy.deepcopy( output )
#     # fragment = completion_fragment['choices'][0]['text']
#     fragment = completion_fragment.get('choices', [])[0]['text']
#     print( fragment )

## trying to print word-by-word ---
# buffer = ""
# for output in stream:
#     completion_fragment = copy.deepcopy( output )
#     fragment = completion_fragment.get('choices', [])[0]['text']
#     buffer += fragment  # add fragment to buffer
#     if buffer and (buffer[-1] in {' ', ',', '.', '!', '?', ';', ':', '-'} or buffer[-1].isdigit()):
#         # print buffer and clear it when a space, punctuation, or digit is detected
#         print(buffer, end='')
#         buffer = ""

## trying to print word-by-word ---
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

## trying to print word-by-word ---
# buffer = ""
# for output in stream:
#     completion_fragment = copy.deepcopy( output )
#     fragment = completion_fragment['choices'][0]['text']  # type: ignore
#     buffer += fragment  # add fragment to buffer
#     if not buffer[-1].isalnum():  # if the last character in buffer is not alphanumeric, print buffer
#         print(buffer, end='')
#         buffer = ""
# if buffer:  # print any remaining text in buffer
#     print(buffer)

## trying to print word-by-word ---
# buffer = ""
# for output in stream:
#     # log.debug( f'output, ``{output}``' )
#     completion_fragment = copy.deepcopy( output )
#     fragment = completion_fragment['choices'][0]['text']  # type: ignore
#     buffer += fragment  # add fragment to buffer
#     log.debug( f'buffer before if, ``{buffer}``' )
#     if len(buffer) > 0:
#         if buffer[0] == ' ':
#             log.debug( f'buffer, ``{buffer}``' )
#             print(buffer, end='')
#             buffer = ""
#             time.sleep( .5 )
# if buffer:  # print any remaining text in buffer
#     log.debug( f'remaining buffer, ``{buffer}``' )
#     print(buffer)
