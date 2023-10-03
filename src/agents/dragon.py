from uagents import Agent,Context
from messages.currancy import *
import requests

dragon=Agent(name='dragon',seed='ball Z')

API_KEY='TTvZgnnbMzoVny5ecrHcYwEaCpLgO8xK'
BASE_URL = 'https://api.apilayer.com/fixer'
CONV = lambda c1,c2: f"/latest?apikey={API_KEY}&base={c1}&symbols={','.join(c2)}"

@dragon.on_message(ConvertRequest,ConvertResponse)
async def conv(ctx: Context, _sender: str, msg: ConvertRequest):
    response=requests.get(BASE_URL+CONV(msg.base,msg.curs)).json()
    await ctx.send(msg.address,ConvertResponse(rates=response['rates']))

if __name__=="__main__":
    dragon.run()
