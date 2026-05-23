import sys
from unittest.mock import patch
from app.utils.logger import _ensure_utf8_stdout

def test_ensure_utf8_stdout_non_windows():
    """
    Test that _ensure_utf8_stdout does not throw exceptions on non-Windows platforms.
    """
    with patch.object(sys, 'platform', 'linux'):
        # On non-Windows, it should just return without doing anything,
        # so no exceptions should be raised.
        _ensure_utf8_stdout()
