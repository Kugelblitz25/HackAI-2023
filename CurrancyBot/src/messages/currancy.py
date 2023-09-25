from uagents import Model


class ConvertRequest(Model):
    base: str
    curs: list[str]
    address: str


class ConvertResponse(Model):
    rates: dict
