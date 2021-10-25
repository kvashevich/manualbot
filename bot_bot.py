import requests
import config

url = 'https://api.telegram.org/bot'
# updates = requests.get(url + config.TOKEN + '/getUpdates?offset=-1').json()
# last_update_id = updates['result'][0]['update_id'] if updates else None
# print(updates)
# message = updates['result'][0]['message']
# print(message)

last_update_id = None
while True:
    updates = requests.get(url + config.TOKEN + '/getUpdates?offset=-1').json()
    message = updates['result'][0].get('message', None)
    if not message:
        message = updates['result'][0].get('edited_message', None)
    if last_update_id != updates['result'][0]['update_id'] and message['from']['id'] == 509585214:
            chat_id = message['chat']['id']
            send_message = requests.get(
                url + config.TOKEN + f'/sendMessage?chat_id={chat_id}&text= Последнее сообщение было отправлено ')
            last_update_id = updates['result'][0]['update_id']
    #     if 'sticker' in message:
    #         chat_id = message['chat']['id']
    #         sticker = message['sticker']['emoji']
    #         send_message = requests.get(
    #             url + config.TOKEN + f'/sendMessage?chat_id={chat_id}&text= {sticker}')
    #     else:
    #         message = updates['result'][0].get('message', None)
    #         if not message:
    #             message = updates['result'][0].get('edited_message', None)
    #         chat_id = message['chat']['id']
    #         if message['text'] == '/weather':
    #             response = requests.get('https://www.nbrb.by/api/exrates/rates')
    #             send_message = requests.get(
    #                 url + config.TOKEN + f'/sendMessage?chat_id={chat_id}&text= {message["text"]}')
    #         text = message['text']
    #         send_message = requests.get(
    #             url + config.TOKEN + f'/sendMessage?chat_id={chat_id}&text= {text}')
    #
    # last_update_id = updates['result'][0]['update_id']
