import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """
what is the smallest bird in the world
"""},
    {"role": "user", "content": "answer the question"}
  ],    
  temperature=0.5,
  max_tokens=100
)

response_lst = response.choices[0].message['content'].strip()
print(response_lst)
