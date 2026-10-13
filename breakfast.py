from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Reads OPENAI_API_KEY from the .env file. The key is not written in this code.
load_dotenv(override=True)

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

prompt = (
    "Give me exactly 5 healthy breakfast ideas. "
    "Healthy means: high in protein or fibre, low in added sugar, "
    "and not deep-fried. "
    "Format rules: a numbered list from 1 to 5, one idea per line, "
    "each idea on a single line, "
    "and no introduction, no closing sentence, no extra text."
)

reply = llm.invoke(prompt)

print(reply.content)