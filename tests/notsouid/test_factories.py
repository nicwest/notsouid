import uuid
from notsouid import factories


class TestBaseFactory:

    def test_call(self):
        factory = factories.BaseFactory()
        result = factory()
        assert result == uuid.UUID('00000000-0000-0000-0000-000000000000')

    def test_from_string(self):
        factory = factories.BaseFactory.from_string('abcd1234-1234-abcd-a1b2-a1b2c3d4e5f6')
        assert factory.time_low == 0xabcd1234
        assert factory.time_mid == 0x1234
        assert factory.time_hi_version == 0xabcd
        assert factory.clock_seq_hi_varient == 0xa1
        assert factory.clock_seq_low == 0xb2
        assert factory.node == 0xa1b2c3d4e5f6


class TestUUID1Factory:

    def test_call(self):
        factory = factories.UUID1Factory()
        result = factory()
        assert result == uuid.UUID('00000001-0000-0000-0000-000000000000')

    def test_auto_inc(self):
        factory = factories.UUID1Factory(auto_increment=True)

        result = factory()
        assert result == uuid.UUID('00000001-0000-0000-0000-000000000000')

        result = factory()
        assert result == uuid.UUID('00000002-0000-0000-0000-000000000000')

        result = factory()
        assert result == uuid.UUID('00000003-0000-0000-0000-000000000000')

    def test_auto_inc_overflow(self):
        factory = factories.UUID1Factory(time_low=0xffffffff, auto_increment=True)
        assert factory() == uuid.UUID('ffffffff-0000-0000-0000-000000000000')
        assert factory() == uuid.UUID('00000000-0000-0000-0000-000000000000')
        assert factory() == uuid.UUID('00000001-0000-0000-0000-000000000000')


class TestUUID4Factory:

    def test_call(self):
        factory = factories.UUID4Factory()
        result = factory()
        assert result == uuid.UUID('00000000-0000-0000-0000-000000000001')

    def test_auto_inc(self):
        factory = factories.UUID4Factory(auto_increment=True)

        result = factory()
        assert result == uuid.UUID('00000000-0000-0000-0000-000000000001')

        result = factory()
        assert result == uuid.UUID('00000000-0000-0000-0000-000000000002')

        result = factory()
        assert result == uuid.UUID('00000000-0000-0000-0000-000000000003')

    def test_auto_inc_overflow(self):
        factory = factories.UUID4Factory(node=0xffffffffffff, auto_increment=True)
        assert factory() == uuid.UUID('00000000-0000-0000-0000-ffffffffffff')
        assert factory() == uuid.UUID('00000000-0000-0000-0000-000000000000')
        assert factory() == uuid.UUID('00000000-0000-0000-0000-000000000001')
