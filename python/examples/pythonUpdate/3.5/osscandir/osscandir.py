# -*- coding=utf-8 -*-
import os


def scanDir(path):
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)


if __name__ == '__main__':
    scanDir('d:\\go\\bin')