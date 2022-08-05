from flask import Flask, request
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import json

app = Flask(__name__)
bot = Bot(config("BOT_TOKEN", default=None))
chat = config('UPDATE', default=None, cast=int)

@app.route('/', methods=["POST"]) 
def main():
    data = json.loads(request.form.to_dict()['data']) 
    message=f'''
A *{data['type']}* Received From *{data["from_name"]}* of *{data['amount']}* _{data['currency']}_ .

`Transaction Id` : *{data['kofi_transaction_id']}*
`Subscription Payment` : *{data['is_subscription_payment']}*
`From` : *{data['from_name']}*
`Sender E-Mail` : *{data['email']}*
`Currency` : *{data['currency']}*
`Amount` : *{data['amount']}*

Powerd by @Teamsemmy
Devolop by @ImRishmika
Support By @ImChathush

'''
    bot.send_message(
            chat_id=chat, 
            text=message, 
            parse_mode='MarkDown', 
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
		[InlineKeyboardButton(text="👀 View Transaction 👀", url=data['url'])]
			])
                )

    return {}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config('PORT', default=6969))
