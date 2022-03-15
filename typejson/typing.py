from datetime import date, datetime
from decimal import Decimal


class TypeJsonTyper:
    '''
    TypeJson 类型化
    '''

    def __init__(self):
        '''
        初始化
        '''

        # 类型化处理
        self.type_processes = [
            (datetime, lambda v: f'dt:{v.strftime("%Y-%m-%d %H:%M:%S")}'),
            (date, lambda v: f'd:{v.strftime("%Y-%m-%d")}'),
            (str, lambda v: f's:{v}'),
            (Decimal, lambda v: f'n:{v}'),
            (bytes, lambda v: f'b:{v.hex()}'),
        ]

        # 去类型化处理
        self.detype_processes = [
            ('dt', lambda v: datetime.strptime(v, '%Y-%m-%d %H:%M:%S')),
            ('d', lambda v: date.strptime(v, '%Y-%m-%d')),
            ('s', lambda v: v),
            ('n', lambda v: Decimal(v)),
            ('b', lambda v: bytes.fromhex(v)),
        ]

    def set_type_process(self, t, p):
        '''
        设置类型化处理
        '''

        for i, v in enumerate(self.type_processes):
            if v[0] == t:
                self.type_processes[i] = (t, p)
                return v[1]
        self.type_processes.append((t, p))
        return None

    def set_detype_process(self, s, p):
        '''
        设置去类型化处理
        '''

        for i, v in enumerate(self.detype_processes):
            if v[0] == s:
                self.detype_processes[i] = (s, p)
                return v[1]
        self.detype_processes.append((s, p))
        return None

    def type(self, v):
        '''
        类型化数据
        '''

        #
        if isinstance(v, list):
            return [self.type(i) for i in v]
        if isinstance(v, dict):
            return {k: self.type(i) for k, i in v.items()}

        # 类型化类型处理
        for t, p in self.type_processes:
            if isinstance(v, t):
                return p(v)

        # bool int float null 默认原样返回
        return v

    def detype(self, raw):
        '''
        去类型化数据
        '''

        if isinstance(raw, list):
            return [self.detype(i) for i in raw]
        if isinstance(raw, dict):
            return {k: self.detype(i) for k, i in raw.items()}
        if isinstance(raw, str):
            t, v = raw.split(':', 1)
            for s, p in self.detype_processes:
                if t == s:
                    return p(v)

        # bool int float null 默认原样返回
        return raw
