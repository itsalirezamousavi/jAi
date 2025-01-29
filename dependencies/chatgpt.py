import openai                                                                                                           # importing libs
import json

def suggestion(weather, biom, budget):                                                                                  # suggestion func
    try:
        openai.api_key = '' # Put Your API Key

        query = ['I want to travel somewhere. I need a list of top 6 suggestion for it.',                                   # query for ChatGPT
                f'I like {weather}. I have {budget} budget. I like the location to have {biom}.',
                'I just want the name of the country and city in english and farsi in a json output, like:\n',
                '{"1": ["Iran/Tehran", "ایران/تهران"],"2": ["France/Paris", "فرانسه/پاریس"]}\n',
                'don\'t send anything else, only the name of the country and city in the given format.']

        messages = [ {"role": "user", "content": ' '.join(query)} ]                                                         # creat and send data to Ai
        chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages )
        reply = chat.choices[0].message.content
        jsonfile = json.loads(reply)
        return jsonfile
    except:
        return None

#print(suggestion('cold','jungel','low'))