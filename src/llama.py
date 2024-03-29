import replicate

LLAMA_API_KEY = "r8_Kc2aEwXy6tjYa8Bxq2WOCoBSBo3sg7R1jfah0"

client = replicate.Client(api_token=LLAMA_API_KEY)

def qeaLlama(prompt):
    response = client.run("meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
                 input={
    "debug": False,
    "top_k": 50,
    "top_p": 1,
    "prompt": prompt,
    "temperature": 0.5,
    "max_new_tokens": 10,
    "min_new_tokens": -1
  })
    arr = []
    for output in response:
        arr.append(output)
    return ''.join(arr)
    

def translateLlama(prompt, from_lang, to_lang):
    response = client.run( "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
                 input={
                     "prompt": f"return only translation of: {prompt} from {from_lang} to {to_lang} without note"
                 })
    arr = []
    for output in response:
        arr.append(output)
        
    return ''.join(arr)

def summarizeLlama(prompt, amount):
    response = client.run( "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
                 input={
                     "prompt": f"Seu objetivo é resumir textos de acordo com 3 níveis: 1(O mínimo possível, mantendo o máximo possível do texto intacto), 2 (Medianamente, sem resumir muito mas ainda retirando o que for necessário) ou 3 (O máximo possível, fazendo com que o texto fique o mais reduzido possível enquanto ainda fazendo sentido). É importante não retirar o sentido do texto. Mande uma resposta completa e somente em pt-br. Resuma este texto:\n {prompt}\n No nível {amount}",
                     "max_new_tokens": 4096,
                 })
    arr = []
    for output in response:
        arr.append(output)
    
    return ''.join(arr)

def summarize_inLlama(prompt, words):
    response = client.run( "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
                 input={
                     "prompt": f"Resuma um texto em apenas {words} palavras e absolutamente nada mais que isso, captando a essência do texto de modo tão resumido quanto necessário para dar a definição do assunto abordado. Mesmo que perca detalhes, lembre-se de nunca ultrapassar {words} palavra(s) na sua resposta. Ex (4 palavras): 'Maçã é uma fruta.'\n Segue o texto:\n {prompt}",
                     "temperature": 0.2
                 })
    arr = []
    for output in response:
        arr.append(output)
    
    return ''.join(arr)

def get_keywordsLlama(prompt, keyNum):
    response = client.run( "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
                 input={
                     "prompt": f"Não responda nada além de apenas o que for pedido. Identifique e retorne {keyNum} palavra(s)-chave e absolutamente nada mais que isso, apenas em português e sem comentários, neste texto:\n {prompt}",
                     "temperature": 0.3
                 })
    arr = []
    for output in response:
        arr.append(output)
    
    return ''.join(arr)