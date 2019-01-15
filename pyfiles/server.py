import os

from sanic import Sanic

from sanic.response import json
from sanic.response import stream
from sanic import response
from sanic.exceptions import NotFound
from pyfiles.storages import DiskStorage

app = Sanic()

cwd = os.getcwd()

storage = DiskStorage(basepath=cwd, base_url="dld")

@app.get('/file/<namespace>/<filename>')
async def download(request, namespace, filename):

    version = request.args.get('version') or 'latest'

    fileinfo = await storage.search(namespace, filename, version)
    fileinfo = await storage.search(namespace, filename, version)

    return response.json(fileinfo)

@app.get('/versions/<namespace>/<filename>')
async def show_versions(request, namespace, filename):

    versions = await storage.versions(namespace, filename)

    return response.json(versions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
