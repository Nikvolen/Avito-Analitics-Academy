import pytest
from morse import decode


@pytest.mark.parametrize('s, exp', [
    ('... --- ...', 'SOS'),
    ('.---- ...-- ...-- --...', '1337'),
    ('. ...- . -....- --- -. .-.. .. -. .', 'EVE-ONLINE'),
    ('..--..', '?')
])
def test_decode(s, exp):
    assert decode(s) == exp
