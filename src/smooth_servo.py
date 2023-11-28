from math import sin, pi as PI, cos, sqrt 


class ServoSmoothBase:
    """ Base class for servo smooth actions """
    def __init__(self, value: int, time_ms: int, start_value: int = 0):
        self._value = self.__normalize_value(value)
        self._time_ms = self.__normalize_time(time_ms)
        self._start_value = self.__normalize_start_value(value, start_value)

    def generate(self, tick_t_ms: int):
        yield 0

    @staticmethod
    def __normalize_start_value(value, s_v):
        return 0 if s_v < 0 or s_v > value else s_v
    
    @staticmethod
    def __normalize_value(value):
        if value <= 0:
            raise TypeError('Value must be greater than 0')
        return int(value)
    
    @staticmethod
    def __normalize_time(value):
        if value <= 0:
            raise TypeError('Time must be greater than 0')
        return int(value)


class SmoothLinear(ServoSmoothBase):
    """Simple linear smoother"""

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value

        _ss = (_t_ms // tick_t_ms)
        _s = _v / _ss

        for i in range(1, _ss):
            yield int(_s_v + _s * i)
        yield _e_v


class SmoothEaseIn(ServoSmoothBase):
    """ link https://easings.net/#easeInSine """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            yield int(_s_v + (1 - cos((i / _ss) * PI / 2)) * _v)
        yield _e_v


class SmoothEaseOut(ServoSmoothBase):
    """ link: https://easings.net/#easeOutSine """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            yield int(_s_v + sin(((i / _ss) * PI) / 2) * _v)
        yield _e_v


class SmoothEaseInOut(ServoSmoothBase):
    """ link: https://easings.net/#easeInOutSine """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            yield int(_s_v + (-(cos(PI * (i / _ss)) - 1) / 2) * _v)
        yield _e_v


class SmoothEaseInQuad(ServoSmoothBase):
    """ link: https://easings.net/#easeInQuad """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = i / _ss
            yield int(_s_v + (_x * _x) * _v)
        yield _e_v


class SmoothEaseOutQuad(ServoSmoothBase):
    """ link: https://easings.net/en#easeOutQuad """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (1 - i / _ss)
            yield int(_s_v + (1 - _x * _x) * _v)
        yield _e_v


class SmoothEaseInOutQuad(ServoSmoothBase):
    """ link: https://easings.net/en#easeInOutQuad """

    def generate(self, tick_t_ms: int):
        _t_ms = self._time_ms
        _s_v = self._start_value
        _v = self._value - _s_v
        _e_v = self._value
        _ss = (_t_ms // tick_t_ms)

        for i in range(1, _ss):
            _x = (i / _ss)
            yield int(_s_v + (2 * _x * _x if _x < 0.5 else 1 - pow(-2 * _x + 2, 2) / 2) * _v)
        yield _e_v
