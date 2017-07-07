import pytest
import uuid
from uuid import uuid1, uuid4
from notsouid.wrapper import freeze_uuid


class TestWrapper:

    def test_wrapping(self):
        assert not str(uuid.uuid1()).startswith('00000001')
        assert not str(uuid.uuid4()).startswith('00000000')

        with freeze_uuid():
            assert uuid.uuid1() == uuid.UUID('00000001-0000-0000-0000-000000000000')
            assert uuid.uuid4() == uuid.UUID('00000000-0000-0000-0000-000000000001')

        assert not str(uuid.uuid1()).startswith('00000001')
        assert not str(uuid.uuid4()).startswith('00000000')

    def test_manual(self):
        assert not str(uuid.uuid1()).startswith('00000001')
        assert not str(uuid.uuid4()).startswith('00000000')

        freezer = freeze_uuid()
        freezer.start()
        assert uuid.uuid1() == uuid.UUID('00000001-0000-0000-0000-000000000000')
        assert uuid.uuid4() == uuid.UUID('00000000-0000-0000-0000-000000000001')
        freezer.stop()

        assert not str(uuid.uuid1()).startswith('00000001')
        assert not str(uuid.uuid4()).startswith('00000000')

    def test_with_string(self):
        with freeze_uuid('abcd1234-1234-abcd-a1b2-a1b2c3d4e5f6'):
            assert uuid.uuid1() == uuid.UUID('abcd1234-1234-abcd-a1b2-a1b2c3d4e5f6')
            assert uuid.uuid4() == uuid.UUID('abcd1234-1234-abcd-a1b2-a1b2c3d4e5f6')

    def test_with_auto_increment(self):
        with freeze_uuid(auto_increment=True):
            assert uuid.uuid1() == uuid.UUID('00000001-0000-0000-0000-000000000000')
            assert uuid.uuid1() == uuid.UUID('00000002-0000-0000-0000-000000000000')
            assert uuid.uuid1() == uuid.UUID('00000003-0000-0000-0000-000000000000')

            assert uuid.uuid4() == uuid.UUID('00000000-0000-0000-0000-000000000001')
            assert uuid.uuid4() == uuid.UUID('00000000-0000-0000-0000-000000000002')
            assert uuid.uuid4() == uuid.UUID('00000000-0000-0000-0000-000000000003')

    @pytest.mark.xfail
    def test_direct_import(self):
        with freeze_uuid():
            assert uuid1() == uuid.UUID('00000001-0000-0000-0000-000000000000')
            assert uuid4() == uuid.UUID('00000000-0000-0000-0000-000000000001')

    def test_decorator(self):

        @freeze_uuid()
        def my_func():
            return uuid.uuid4()

        assert my_func() == uuid.UUID('00000000-0000-0000-0000-000000000001')
        assert my_func() == uuid.UUID('00000000-0000-0000-0000-000000000001')
        assert my_func() == uuid.UUID('00000000-0000-0000-0000-000000000001')
        assert not str(uuid.uuid4()).startswith('00000000')

    def test_decorator_params(self):

        @freeze_uuid('abcd1234-0000-0000-0000-000000000001', auto_increment=True)
        def my_func():
            return uuid.uuid4()

        assert my_func() == uuid.UUID('abcd1234-0000-0000-0000-000000000001')
        assert my_func() == uuid.UUID('abcd1234-0000-0000-0000-000000000002')
        assert my_func() == uuid.UUID('abcd1234-0000-0000-0000-000000000003')
