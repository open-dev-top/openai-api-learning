import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"你是一个富有诗意的助手，善于用创意来解释复杂的编程概念。"},
        {"role":"user","content":"创作一首诗，解释编程中递归的概念。"}
    ]
)

print(completion.choices[0].message)
