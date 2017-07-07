import uuid


class BaseFactory(object):

    def __init__(self, time_low=0x0, time_mid=0x0, time_hi_version=0x0,
                 clock_seq_hi_varient=0x0, clock_seq_low=0x0, node=0x0,
                 auto_increment=False):
        self.time_low = time_low
        self.time_mid = time_mid
        self.time_hi_version = time_hi_version
        self.clock_seq_hi_varient = clock_seq_hi_varient
        self.clock_seq_low = clock_seq_low
        self.node = node
        self.auto_increment = auto_increment

    def __call__(self, *args, **kwargs):

        return uuid.UUID(fields=(
            self.time_low,
            self.time_mid,
            self.time_hi_version,
            self.clock_seq_hi_varient,
            self.clock_seq_low,
            self.node
        ))

    @classmethod
    def from_string(cls, raw, *args, **kwargs):
        u = uuid.UUID(raw)
        time_low = u.fields[0]
        time_mid = u.fields[1]
        time_hi_version = u.fields[2]
        clock_seq_hi_varient = u.fields[3]
        clock_seq_low = u.fields[4]
        node = u.fields[5]

        return cls(time_low=time_low, time_mid=time_mid,
                   time_hi_version=time_hi_version,
                   clock_seq_hi_varient=clock_seq_hi_varient,
                   clock_seq_low=clock_seq_low, node=node, *args, **kwargs)


class UUID1Factory(BaseFactory):

    def __init__(self, time_low=0x1, *args, **kwargs):
        super(UUID1Factory, self).__init__(time_low=time_low, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        ret = super(UUID1Factory, self).__call__(*args, **kwargs)
        if self.auto_increment:
            self.time_low +=1
            if self.time_low > 0xffffffff:
                self.time_low = 0x0
        return ret


class UUID4Factory(BaseFactory):

    def __init__(self, node=0x1, *args, **kwargs):
        super(UUID4Factory, self).__init__(node=node, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        ret = super(UUID4Factory, self).__call__(*args, **kwargs)
        if self.auto_increment:
            self.node +=1
            if self.node > 0xffffffffffff:
                self.node = 0x0
        return ret
