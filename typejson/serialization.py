from json import dump, dumps, load, loads
from .typing import TypeJsonTyper


class TypeJsonSerializer:
    '''
    TypeJson 序列化
    '''

    def __init__(self, typer=None):
        self.typer = typer if typer is not None else TypeJsonTyper()

    def dumps(self, raw, **args) -> str:
        r = self.typer.type(raw)
        if 'ensure_ascii' not in args:
            args['ensure_ascii'] = False
        return dumps(r, **args)

    def dump(self, raw, fp, **args):
        r = self.typer.type(raw)
        if 'ensure_ascii' not in args:
            args['ensure_ascii'] = False
        return dump(r, fp, **args)

    def loads(self, raw: str, **args):
        r = loads(raw, **args)
        return self.typer.detype(r)

    def load(self, fp, **args):
        r = load(fp, **args)
        return self.typer.detype(r)
