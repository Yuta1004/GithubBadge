from enum import Enum


class ShieldsColor(Enum):
    BRIGHTGREEN = "brightgreen"
    GREEN = "green"
    YELLOWGREEN = "yellowgreen"
    YELLOW = "yellow"
    ORANGE = "orange"
    RED = "red"
    BLUE = "blue"
    LIGHTGRAY = "lightgray"
    SUCCESS = "success"
    IMPORTANT = "important"
    CRITICAL = "critical"
    INFORMATIONAL = "informational"
    INACTIVE = "inactive"
    BLUEVIOLET = "blutviolet"
    _FF69B4 = "ff69b4"
    _C9CF = "9cF"


def shields(label, message, color):
    shields_url = "https://img.shields.io/static/v1.svg?label=<LABEL>&message=<MESSAGE>&color=<COLOR>"
    shields_url = shields_url.replace("<LABEL>", label)
    shields_url = shields_url.replace("<MESSAGE>", message)
    shields_url = shields_url.replace("<COLOR>", color.value)
    return shields_url


if __name__ == "__main__":
    print(shields("build", "succcess", ShieldsColor.SUCCESS))
    print(shields("version", "v1.0.0", ShieldsColor.INFORMATIONAL))
