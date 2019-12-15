# -*- coding: utf-8 -*-
from movimentos import *

vire_a_direita()
ande()
ande()
ande()
proximo_movimento = "luz"
if proximo_movimento == "luz":
    ande()
    acenda()
    ande()
elif proximo_movimento == "buraco":
    pule()
ande()
ande()
acenda()
vire_a_direita()
proximo_movimento = "luz"
if proximo_movimento == "luz":
    ande()
    acenda()
    ande()
elif proximo_movimento == "buraco":
    pule()
vire_a_direita()
ande()
proximo_movimento = "buraco"
if proximo_movimento == "luz":
    ande()
    acenda()
    ande()
elif proximo_movimento == "buraco":
    pule()


