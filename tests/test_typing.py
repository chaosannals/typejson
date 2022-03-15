from decimal import Decimal
from typejson.typing import TypeJsonTyper


def test_typejsontyper_type():
    '''

    '''

    raw = {
        'one': 'title',
        'two': [1, 123.23, Decimal('123.567'), 5],
    }
    typing = TypeJsonTyper()
    r = typing.type(raw)
    assert r['two'][2] == 'n:123.567'

    e = typing.detype(r)
    assert e['two'][0] == 1
