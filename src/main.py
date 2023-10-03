from uagents import Bureau
from agents.user import user
from agents.dragon import dragon

if __name__=='__main__':
    bureau = Bureau()
    bureau.add(user)
    bureau.add(dragon)
    bureau.run()