# Numpy vs Python
This repo contains a test to demonstrate the speed advantage Numpy has over regular Python.

## Reasons
The reasons for Numpy's superior performance are listed below:
* Numpy is written in C which is why it is faster than Python.
* Python lists are pointers to Python Objects, these pointers eat up alot more memory than Numpy arrays.
* Numpy lists are statically stored in memory unlike Python lists which are dynamic. This causes less memory usage and thus the program runs faster
