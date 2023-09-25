from uagents import Agent, Context
from src.messages.currancy import *

user = Agent(name='user', seed='converter ')
dragonAddess = "agent1qg5ke2duhdv0d7nw9nj6p3f2c34p9f3mler3yw49ydkufzh3r8wrs0r2zks"


def SETUP(ctx: Context):
    Base = input('Enter Base Currancy:').upper()
    numConditions = int(input('Enter number of conditions:'))
    conditions = []
    for _ in range(numConditions):
        condition = {
            'type': input('Enter type of condition Upper[u] or Lower[l]:').upper()[0],
            'currancy': input('Enter Currancy (eg: INR):').upper(),
            'Threshold': float(input('Enter Threshold:'))
        }
        conditions.append(condition)
    ctx.storage.set('Conditions', conditions)
    ctx.storage.set('conditionsCount', numConditions)
    ctx.storage.set('Base', Base)


@user.on_interval(period=3.0, messages=ConvertRequest)
async def main(ctx: Context):
    setup = ctx.storage.get("setup") or 0
    if not setup:
        ctx.logger.info(f"Starting Setup....")
        SETUP(ctx)
        ctx.logger.info(f"Setup completed.")
        ctx.storage.set('setup', True)

    base = ctx.storage.get('Base')
    curs = [i['currancy'] for i in ctx.storage.get('Conditions')]
    await ctx.send(dragonAddess, ConvertRequest(base=base, curs=curs, address=user.address))


@user.on_message(ConvertResponse)
async def warn(ctx: Context, _sender: str, msg: ConvertResponse):
    base = ctx.storage.get('Base')
    for condition in ctx.storage.get('Conditions'):
        rate = msg.rates[condition['currancy']]
        if (condition['type'] == 'U' and rate > condition['Threshold']) or (condition['type'] == 'L' and rate < condition['Threshold']):
            ctx.logger.warning(
                f"{base} has crossed the threshold of {condition['Threshold']} {condition['currancy']}")

if __name__ == "__main__":
    user.run()
