# source
Chris Hay on "Python with Stanford Alpaca and Vicuna 13B AI models - A llama-cpp-python Tutorial!"
<https://www.youtube.com/watch?v=-BidzsQYZM4>


# get model
<https://huggingface.co/eachadea/legacy-ggml-vicuna-13b-4bit>

Note: already things have changed. The file above suggests using other files. For now I'm sticking with this file specified in the video.


# install stuff

Note: a simple `pip install llama-cpp-python` installed successfully, but running main.py after the model-load yielded an error.

Googling, I ended up pip-installing an older version -- see `requirements.txt`. Now running `python ./main.py` works (at 5:45 in video).

---

- at 5:45