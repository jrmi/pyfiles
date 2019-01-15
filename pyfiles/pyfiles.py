import os

from sanic import Sanic

from sanic.response import json
from sanic.response import stream
from sanic import response
from sanic.exceptions import NotFound

app = Sanic()

cwd = os.getcwd()

@app.get('/file/<namespace>/<filename>')
async def download(request, namespace, filename):

    version = request.args.get('version') or 'latest'
    basename = os.path.join(cwd, *namespace.split('.'))

    filelist = [f for f in sorted(os.listdir(basename)) if f.endswith(filename)]

    if version != 'latest':
        filelist = [f for f in filelist if f.startswith(version)]
    
    if not filelist:
        raise NotFound(f"File <{filename}> not found with version <{version}>")

    selected_file = filelist[-1]

    print('selected', selected_file)
    
    filepath = os.path.join(basename, selected_file)

    return await response.file(filepath)

@app.get('/versions/<namespace>/<filename>')
async def show_versions(request, namespace, filename):

    basename = os.path.join(cwd, *namespace.split('.'))

    filelist = [f.split('__')[0] for f in sorted(os.listdir(basename)) if f.endswith(filename)]

    return response.json(filelist)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)