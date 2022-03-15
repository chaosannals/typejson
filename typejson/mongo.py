from bson import Decimal128
from .typing import TypeJsonTyper


class TypeJsonMongoTyper(TypeJsonTyper):
    '''
    MongoDB 类型化
    '''

    def __init__(self):
        super().__init__()
        self.set_type_process(Decimal128, lambda v: f'n:{v}')
        self.set_detype_process('n', lambda v: Decimal128(v))
