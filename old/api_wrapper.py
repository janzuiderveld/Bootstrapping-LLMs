import requests
import json

class APIWrapper:
    def __init__(self, base_url = 'http://localhost:11434'):
        self.base_url = base_url

    def generate_completion(self, model, prompt, options=None, system=None, template=None, context=None):
        url = self.base_url + '/api/generate'
        data = {
            "model": model,
            "prompt": prompt,
        }
        if options:
            data['options'] = options
        if system:
            data['system'] = system
        if template:
            data['template'] = template
        if context:
            data['context'] = context

        response = requests.post(url, data=json.dumps(data), stream=True)
        # Streamed responses are not immediately decoded,
        # to decode them, we need to iterate through the response
        for line in response.iter_lines():
            if line:  # filter out keep-alive new lines
                yield json.loads(line)

# Example of usage:
# api = APIWrapper()
# for response in api.generate_completion('llama2:7b', 'Why is the sky blue?'):
#     print(response)