# gpt-retriever

GPT but with your own data

## Get started

1. Install necessary libraries

```python
pip install langchain
pip install python-dotenv
```

2. Edit .env and txt file

```bash
cp .env.template .env
cp data.txt.template data.txt
```

Make sure to put in your OpenAI API Key and content to data.txt.

> Note: you can put multiple .txt files

3. Run script

```bash
python retriever.py "Prompt"
```
