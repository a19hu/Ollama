import requests
import json


url ="http://localhost:11434/api/generate"

data = {
    "model": "test:01",
    "prompt": "what is your name?",
}

response = requests.post(url, json=data,stream=True)


if response.status_code == 200:

    print('generated')

    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            result = json.loads(decoded_line)
            generated_text = result.get('response', '')
            print(generated_text)

else:
    print('error')