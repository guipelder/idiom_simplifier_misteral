# Idiom Simplification Web API Using Mistral LLM Model

This web app demonstrates how to utilize the Mistral LLM model for idiom simplification tasks through a simple Flask server. It reads content from a text file (prompt.txt) and generates a simplified version suitable for translation.

## Getting Started
To get started with this project locally, follow these steps:

### Prerequisites
Make sure you meet the following prerequisites prior to attempting installation:

1. Ensure Python (version >= 3.6) is installed in your system. You may download it from https://www.python.org/downloads/.
2. Check if C++ compiler toolchain is present on your system for compiling the native parts of the Mistral LLM package. On Linux systems, commonly found tools include `gcc`, `clang`, etc., while Windows users might consider using Visual Studio Build Tools. For macOS, XCode Command Line Tools should suffice.
3. Verify that the [`llama_cpp`](https://pypi.org/project/llama-cpp-python/) Python package has been correctly built and installed after cloning the repo. Refer to the official documentation for detailed build instructions depending upon your platform.
4. download your `.gguf` model from [hugginface](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF) 

Once those dependencies are met, proceed with setting up the environment:

### Environment Setup
Install the required packages mentioned in the `requirements.txt` file:
```
pip install -r requirements.txt
```
Download the Mistral LLM model archive (~5GB) from the link specified in the source code comments (`.mistral-7b-instruct-v0.2.Q6_K.gguf`) and extract it into a directory named `misteral` inside the same folder where the source code resides.

### Running Locally
Execute the following command to start the Flask server locally:
```
python3 idiom_misterla.py
```
Access the web application at `http://localhost:5000/`.

## Usage Instructions
The user needs to provide a path to a text file containing idioms and expressions when navigating to the root route ('/'). Upon submission, the server loads the content from the given text file, processes it utilizing the Mistral LLM model for simplifying idioms, and returns the equivalent text back to the client side.

## Technical Details
This project employs the following technologies:

- [Flask](https://flask.palletsprojects.com/en/2.1.x/) – Lightweight web framework for creating APIs in Python
- [Llama](https://pypi.org/project/llama-cpp-python/) – Highly capable autoregressive language models implemented in pure C++, providing superior performance over purely Python implementations. but we use the python binding of it.


## Author
- Mehdi Hosseini  - [GitHub](https://github.com/guipelder)


