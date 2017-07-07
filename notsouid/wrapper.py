from mock import patch
from notsouid.factories import UUID1Factory, UUID4Factory


class freeze_uuid(object):

    def __init__(self, str_in=None, auto_increment=False):
        self.str_in = str_in
        self.auto_increment = auto_increment
        self._patches = []

    def start(self):
        if self._patches:
            for patcher in self._patches:
                patcher.start()
            return
        if self.str_in:
            v1 = UUID1Factory.from_string(
                self.str_in,
                auto_increment=self.auto_increment
            )
            v4 = UUID4Factory.from_string(
                self.str_in,
                auto_increment=self.auto_increment
            )
        else:
            v1 = UUID1Factory(auto_increment=self.auto_increment)
            v4 = UUID4Factory(auto_increment=self.auto_increment)

        v1patcher = patch('uuid.uuid1', v1)
        v1patcher.start()
        self._patches.append(v1patcher)

        v4patcher = patch('uuid.uuid4', v4)
        v4patcher.start()
        self._patches.append(v4patcher)

    def stop(self):
        for patcher in self._patches:
            patcher.stop()

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            with self:
                return f(*args, **kwargs)
        return wrapper

    def __enter__(self):
        self.start()

    def __exit__(self, type, value, tb):
        self.stop()
