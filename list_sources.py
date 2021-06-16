#!/usr/bin/env python
import json
from sys import stdout
from json import dumps, JSONEncoder
from SwitchAudioSource import get_sources, AudioSource

sources = get_sources()
items = list(map(lambda source: AudioSource(source.decode(), False).__dict__, sources))

json_output = dumps({
    "items": items
})

stdout.write(json_output)
