"""Shkruani nje funksion qe merr gjatesite e dy kateve te nje trekendeshi kenddrejte dhe kthen gjatesine e
hipotenuzes se trekendeshit."""

import math

def llogarit_hipotenuzen(kati1, kati2):
    hipotenuza = math.sqrt(kati1**2 + kati2**2)
    return hipotenuza


print(llogarit_hipotenuzen(3, 4))  # Kthen 5.0
