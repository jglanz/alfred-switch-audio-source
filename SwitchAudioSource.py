from subprocess import check_output, call
from json import dumps
from sys import stdout
from os import environ

environ.setdefault("SWITCH_AUDIO_SOURCE_PATH", "/usr/local/bin/SwitchAudioSource")
PATH_TO_SWITCH_AUDIO_OUTPUT = environ['SWITCH_AUDIO_SOURCE_PATH']
LOOKUP_WARNING = "Error: Could not find SwitchAudioSource"


class AudioSource:
    def __init__(self, title, active):
        self.uid = title
        self.title = title
        self.arg = title
        self.autocomplete = title

        self.output = True  # output.find('output') > -1
        self.input = not self.output
        self.icon = {"path": "icons/active.png" if active ==
                                                   title else "icons/inactive.png"}

    def __str__(self):
        return str(self.__dict__)


def get_sources():
    active = get_current()

    command_output = check_output([
        PATH_TO_SWITCH_AUDIO_OUTPUT, '-a', '-t', 'output'
    ])
    #
    lines = filter(lambda line: line != active, map(lambda line: line.strip(), command_output.splitlines()))
    # return map(lambda line: AudioSource(line, active), lines)
    return lines


def get_current():
    command_output = check_output([
        PATH_TO_SWITCH_AUDIO_OUTPUT, '-c'
    ]).decode()
    return command_output.strip()


def set_output(device):
    check_output([
        PATH_TO_SWITCH_AUDIO_OUTPUT, '-s', device
    ])
    stdout.write(device)


def no_path_provided():
    stdout.write(dumps({
        "items": [{
            "title": LOOKUP_WARNING
        }]
    }))
    exit()
