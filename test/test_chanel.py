import pytest

from srs.channel import Channel


@pytest.fixture
def Channel1():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')

def test_channel_print_info(Channel1):
    assert isinstance(youtube.channels().list(id=Channel1, part='snippet,statistics').execute(), list)

