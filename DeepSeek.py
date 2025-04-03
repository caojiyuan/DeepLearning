
from openai import OpenAI

client = OpenAI(api_key="sk-6f8a3dd17777483cac209df838c04aa9", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "作一首诗，描写美女"},
    ],
    stream=False
)

print(response.choices[0].message.content)