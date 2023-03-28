import openai
openai.api_key ="your api key here"
def translate_to_chinese(text):
    prompt = f"Translate the following English text to Chinese:\n\n{text}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.8,
    )

    return response.choices[0].text.strip()
