# source
Chris Hay on "Python with Stanford Alpaca and Vicuna 13B AI models - A llama-cpp-python Tutorial!"
<https://www.youtube.com/watch?v=-BidzsQYZM4>


# get model
<https://huggingface.co/eachadea/legacy-ggml-vicuna-13b-4bit>

Note: already things have changed. The file above suggests using other files. For now I'm sticking with this file specified in the video.


# install stuff

Note: a simple `pip install llama-cpp-python` installed successfully, but running main.py after the model-load yielded an error.


# notes

- I spent some time trying to get the ouput to print in teletype fashion. I had initially wanted to print word-by-word, but not all fragments are full words. I settled for looking for the presence of a space. Not perfect, but fine for now.

- The other thing I wanted to do was to have the word-by-word output appear on the same line. "print()" doesn't seem to allow this. I tried using it's "end" parameter, but that buffers the data until a newline. Probably some sort of stdout call would work. But I was really just trying to demonstrate that, for a web-context, accessing streamed output is possible.

---