[![PyPI version](https://badge.fury.io/py/notsouid.svg)](https://badge.fury.io/py/notsouid)
[![Build Status](https://travis-ci.org/nicwest/notsouid.svg?branch=master)](https://travis-ci.org/nicwest/notsouid)
[![codecov](https://codecov.io/gh/nicwest/notsouid/branch/master/graph/badge.svg)](https://codecov.io/gh/nicwest/notsouid)

notsouid
========

Quickly patch the dynamic/random uuid methods for testing.

Inspired by [freezegun](https://github.com/spulec/freezegun)

Installation
------------

```bash
pip install notsouid
```

Usage
-----

```python
>>> import uuid
>>> from notsouid import freeze_uuid

# uuid v1
>>> with freeze_uuid():
...     uuid.uuid1()
... 
UUID('00000001-0000-0000-0000-000000000000')
>>> uuid.uuid1()
UUID('d358c79a-62b7-11e7-b95d-001500e9d987')
>>> uuid.uuid1()
UUID('d417ca3c-62b7-11e7-b95d-001500e9d987')

# uuid v4
>>> with freeze_uuid():
...     uuid.uuid4()
... 
UUID('00000000-0000-0000-0000-000000000001')
>>> uuid.uuid4()
UUID('e8b65efd-d8d3-4048-9619-036d9ea16887')
>>> uuid.uuid4()
UUID('c7b6d222-3149-4ac5-9673-61f913b40393')

# auto increment
>>> with freeze_uuid(auto_increment=True):
...     uuid.uuid1()
...     uuid.uuid4()
...     uuid.uuid1()
...     uuid.uuid4()
...     uuid.uuid1()
...     uuid.uuid4()
... 
UUID('00000001-0000-0000-0000-000000000000')
UUID('00000000-0000-0000-0000-000000000001')
UUID('00000002-0000-0000-0000-000000000000')
UUID('00000000-0000-0000-0000-000000000002')
UUID('00000003-0000-0000-0000-000000000000')
UUID('00000000-0000-0000-0000-000000000003')

# custom result
>>> with freeze_uuid('abcd1234-acbd-1234-a1b2-a1b2c3d4e5f6'):
...     uuid.uuid4()
...     uuid.uuid1()
... 
UUID('abcd1234-acbd-1234-a1b2-a1b2c3d4e5f6')
UUID('abcd1234-acbd-1234-a1b2-a1b2c3d4e5f6')

# wrap auto increment
>>> with freeze_uuid('ffffffff-ffff-ffff-ffff-fffffffffffe', auto_increment=True):
...     uuid.uuid4()
...     uuid.uuid4()
...     uuid.uuid4()
...     uuid.uuid4()
... 
UUID('ffffffff-ffff-ffff-ffff-fffffffffffe')
UUID('ffffffff-ffff-ffff-ffff-ffffffffffff')
UUID('ffffffff-ffff-ffff-ffff-000000000000')
UUID('ffffffff-ffff-ffff-ffff-000000000001')

# decorator
>>> @freeze_uuid(auto_increment=True)
... def my_func():
...     return uuid.uuid4()
... 
>>> my_func()
UUID('00000000-0000-0000-0000-000000000001')
>>> my_func()
UUID('00000000-0000-0000-0000-000000000002')
>>> my_func()
UUID('00000000-0000-0000-0000-000000000003')

```
