import os
import sys
import pyfiles
import importlib

from pyfiles.conf import settings
from pyfiles.storages import get_storage

# TODO: remove below if statement asap. This is a workaround for a bug in begins
# TODO: which provokes an exception when calling pypeman without parameters.
# TODO: more info at https://github.com/aliles/begins/issues/48

if len(sys.argv) == 1:
    sys.argv.append('-h')

CURRENT_DIR = os.getcwd()

# Keep this import
sys.path.insert(0, CURRENT_DIR)

import asyncio  # noqa
import begin # noqa

@begin.subcommand
def search(namespace, filename, version='latest'):
    loop = asyncio.get_event_loop()
    settings.init_settings()

    storage = get_storage(settings.BACKEND, settings.BACKEND_OPTIONS)

    result = loop.run_until_complete(storage.search(namespace=namespace, filename=filename, version=version))

    print(result)

@begin.subcommand
def versions(namespace: "namespace store", filename: "Filename"):
    loop = asyncio.get_event_loop()
    settings.init_settings()

    storage = get_storage(settings.BACKEND, settings.BACKEND_OPTIONS)

    result = loop.run_until_complete(storage.versions(namespace=namespace, filename=filename))

    print(result)

@begin.subcommand
def store(path: "file path to upload", namespace: "Namespace to store", filename: "File name to store", version: "File version"):
    loop = asyncio.get_event_loop()
    settings.init_settings()

    storage = get_storage(settings.BACKEND, settings.BACKEND_OPTIONS)

    with open('path', 'rb') as fin:
        loop.run_until_complete(storage.store(stream=fin, namespace=namespace, filename=filename, version=version))

    print("Ok!")

#@begin.subcommand
def serve():
    pass

@begin.start
def run(version=False):
    """ Pyfiles allow you to easilly store and share data files """

    if version:
        print(pyfiles.__version__)
        sys.exit(0)
