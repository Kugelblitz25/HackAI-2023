from uagents import Bureau
from src.agents.user import user
from src.agents.dragon import dragon

if __name__=='__main__':
    bureau=Bureau()
    bureau.add(user)
    bureau.add(dragon)
    bureau.run()