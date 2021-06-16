#!/usr/bin/env python
from sys import stdout

from SwitchAudioSource import get_current

stdout.write(get_current())
