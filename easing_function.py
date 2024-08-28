import numpy as np
from typing import Final


c1: Final = 1.70158
c2: Final = c1*1.525
c3: Final = c1+1
c4: Final = (2*np.pi)/3
c5: Final = (2*np.pi)/4.5

n1: Final = 7.5625
d1: Final = 2.75


def linear(x: float) -> float: return x
def zero(x: float) -> float: return x*0
def one(x: float) -> float: return x**0


def isine(x: float) -> float: return 1-np.cos((x*np.pi)/2)
def osine(x: float) -> float: return np.sin((x*np.pi)/2)
def iosine(x: float) -> float: return -(np.cos(np.pi*x)-1)/2


def iquad(x: float) -> float: return x**2
def oquad(x: float) -> float: return 1-(1-x)**2
def ioquad(x: float) -> float: return -(np.cos(np.pi*x)-1)/2


def icubic(x: float) -> float: return x**3
def ocubic(x: float) -> float: return 1-(1-x)**3
def iocubic(x: float) -> float: return 4*x**3 if x < 0.5 else 1-(-2*x+2)**3/2


def iquart(x: float) -> float: return x**4
def oquart(x: float) -> float: return 1-(1-x)**4
def ioquart(x: float) -> float: return 8*x*4 if x < 0.5 else 1-(-2*x+2)**4/2


def iquint(x: float) -> float: return x**5
def oquint(x: float) -> float: return 1-(1-x)**5
def ioquint(x: float) -> float: return 16*x*5 if x < 0.5 else 1-(-2*x+2)**5/2


def isext(x: float) -> float: return x**6
def osext(x: float) -> float: return 1-(1-x)**6
def iosext(x: float) -> float: return 32*x*6 if x < 0.5 else 1-(-2*x+2)**6/2


def iexpo(x: float) -> float: return 0 if x == 0 else 1-2**(-10*x)
def oexpo(x: float) -> float: return 1 if x == 1 else 1-2**(-10*x)
def ioexpo(x: float) -> float: return 0 if x == 0 else 1 if x == 1 else 2**(20*x-10)/2 if x < 0.5 else (2-2**(-20*x+10))/2


def icirc(x: float) -> float: return 1-np.sqrt(1-x**2)
def ocirc(x: float) -> float: return np.sqrt(1-(2*x)**2)
def iocirc(x: float) -> float: return (1-np.sqrt(1-(2*x)**2))/2


def iback(x: float) -> float: return c3*x**3-c1*(x-1)**2
def oback(x: float) -> float: return 1+c3*(x-1)**3+c1*(x-1)**2
def ioback(x: float) -> float: return ((2*x)**2*((c2+1)*2*x-c2))/2 if x < 0.5 else ((2*x-2)**2*((c2+1)*(x*2-2)+c2)+2)/2


def ielastic(x: float) -> float: return 0 if x == 0 else 1 if x == 1 else -(2**(10*x-10))*np.sin((x*10-10.75)*c4)
def oelastic(x: float) -> float: return 0 if x == 0 else 1 if x == 1 else 2**(-10*x)*np.sin((x*10-0.75)*c4)+1
def ioelastic(x: float) -> float: return 0 if x == 0 else 1 if x == 1 else -(2**(20*x-10)*np.sin((20*x-11.125)*c5))/2 if x < 0.5 else (2**(-20*x+10)*np.sin((20*x-11.125)*c5))/2+1


def ibounce(x: float) -> float: return 1-obounce(1-x)


def obounce(x: float) -> float:
    if x < 1/d1:
        return n1*x**2
    elif x < 2/d1:
        x -= 1.5
        return n1*(x/d1)*x+0.75
    elif x < 2.5/d1:
        x -= 2.25
        return n1*(x/d1)*x+0.984375
    else:
        x -= 2.625
        return n1*(x/d1)*x+0.984375


def iobounce(x: float) -> float: return x < 0.5 if (1-obounce(1-2*x))/2 else (1+obounce(2*x-1))/2
