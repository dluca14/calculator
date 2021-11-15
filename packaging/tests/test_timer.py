import time

from packaging.src.business_logic.timer import Timer


def test_timer():
    with Timer('test') as timer:
        time.sleep(1)

    assert timer.elapsed.__round__(1) == 1