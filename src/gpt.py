from openai import OpenAI

client = OpenAI(api_key='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')

def qeaGPT(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7)
    obj = {"id": completion.id,
           "response": completion.choices[0].message.content }
    # print(obj)
    return obj

def translateGPT(prompt, from_lang, to_lang):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Traduza {prompt} de {from_lang} para {to_lang}"}],
    temperature=0.7)
    obj = {"id": completion.id,
           "response": completion.choices[0].message.content }
    return obj

def summarizeGPT(prompt, amount):
    quant = "o mínimo possível" if amount == 1 else ("medianamente" if amount == 2 else "ao máximo possível")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Seu objetivo é resumir textos de acordo com 3 níveis: 1(O mínimo possível), 2 (Medianamente) ou 3 (O máximo possível). É importante não retirar o sentido do texto. Resuma este texto:\n {prompt}\n No nível {quant}"}],
        temperature=0.7
    )

    obj = {"id": completion.id, "response": completion.choices[0].message.content}
    return obj

def get_keywordsGPT(prompt, keyNum):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Identifique {keyNum} palavras-chave deste texto: {prompt}"}],
    temperature=0.7)
    obj = {id: completion.id,
           "response": completion.choices[0].message.content }
    return obj

def summarize_inGPT(prompt, words):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Resuma este texto em {words} palavras:\n {prompt}"}],
    temperature=0.7)
    obj = {id: completion.id,
           "response": completion.choices[0].message.content }
    return obj
