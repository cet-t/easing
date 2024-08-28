from enum import Enum
import easing_function as f


class EASE(Enum, int):
    LINEAR = 0
    ZERO = 10
    ONE = 11

    IN_SINE = 100
    OUT_SINE = 101
    IN_OUT_SINE = 102

    IN_QUAD = 110
    OUT_QUAD = 111
    IN_OUT_QUAD = 112

    IN_CUBIC = 120
    OUT_CUBIC = 121
    IN_OUT_CUBIC = 122

    IN_QUART = 130
    OUT_QUART = 131
    IN_OUT_QUART = 132

    IN_QUINT = 140
    OUT_QUINT = 141
    IN_OUT_QUINT = 142

    IN_SEXT = 150
    OUT_SEXT = 151
    IN_OUT_SEXT = 152

    IN_EXPO = 0xf00051
    OUT_EXPO = 0xf00052
    IN_OUT_EXPO = 0xf00053

    IN_CIRC = 0xf00061
    OUT_CIRC = 0xf00062
    IN_OUT_CIRC = 0xf00063

    IN_BACK = 0xf00071
    OUT_BACK = 0xf00072
    IN_OUT_BACK = 0xf00073

    IN_ELASTIC = 0xf00081
    OUT_ELASTIC = 0xf00082
    IN_OUT_ELASTIC = 0xf00083

    IN_BOUNCE = 0xf00091
    OUT_BOUNCE = 0xf00092
    IN_OUT_BOUNCE = 0xf00093


def easing(x: float, ease: EASE) -> float | None:
    match ease:
        case EASE.LINEAR: return f.linear(x)
        case EASE.ZERO: return f.zero(x)
        case EASE.ONE: return f.one(x)

        case EASE.IN_SINE: return f.isine(x)
        case EASE.OUT_SINE: return f.osine(x)
        case EASE.IN_OUT_SINE: return f.iosine(x)

        case EASE.IN_QUAD: return f.iquad(x)
        case EASE.OUT_QUAD: return f.oquad(x)
        case EASE.IN_OUT_QUAD: return f.ioquad(x)

        case EASE.IN_CUBIC: return f.icubic(x)
        case EASE.OUT_CUBIC: return f.ocubic(x)
        case EASE.IN_OUT_CUBIC: return f.iocubic(x)

        case EASE.IN_QUART: return f.iquart(x)
        case EASE.OUT_QUART: return f.oquart(x)
        case EASE.IN_OUT_QUART: return f.ioquart(x)

        case EASE.IN_QUINT: return f.iquint(x)
        case EASE.OUT_QUINT: return f.oquint(x)
        case EASE.IN_OUT_QUINT: return f.ioquint(x)

        case EASE.IN_SEXT: return f.isext(x)
        case EASE.OUT_SEXT: return f.osext(x)
        case EASE.IN_OUT_SEXT: return f.iosext(x)

        case EASE.IN_EXPO: return f.iexpo(x)
        case EASE.OUT_EXPO: return f.oexpo(x)
        case EASE.IN_OUT_EXPO: return f.ioexpo(x)

        case EASE.IN_CIRC: return f.icirc(x)
        case EASE.OUT_CIRC: return f.ocirc(x)
        case EASE.IN_OUT_CIRC: return f.iocirc(x)

        case EASE.IN_BACK: return f.iback(x)
        case EASE.OUT_BACK: return f.oback(x)
        case EASE.IN_OUT_BACK: return f.ioback(x)

        case EASE.IN_ELASTIC: return f.ielastic(x)
        case EASE.OUT_ELASTIC: return f.oelastic(x)
        case EASE.IN_OUT_ELASTIC: return f.ioelastic(x)

        case EASE.OUT_BOUNCE: return f.obounce(x)
        case EASE.IN_BOUNCE: return f.ibounce(x)
        case EASE.IN_OUT_BOUNCE: return f.iobounce(x)

        case _: return None
