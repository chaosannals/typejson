from decimal import Decimal
from datetime import datetime, date
from typejson.typing import TypeJsonTyper


def test_typejsontyper_type():
    '''

    '''


    raw = {
        'one': 'title',
        'two': [1, 123.23, Decimal('123.567'), 5],
        'dt': datetime.strptime('2022-01-01 01:02:03', '%Y-%m-%d %H:%M:%S'),
        'd': datetime.strptime('2022-01-01', '%Y-%m-%d').date(),
    }
    assert isinstance(raw['d'], date)
    typing = TypeJsonTyper()
    r = typing.type(raw)
    assert r['two'][2] == 'n:123.567'

    e = typing.detype(r)
    assert e['two'][0] == 1
