
class Storage: # TODO necessary ?
    async def search(self, namespace, filename, version):
        raise NotImplementedError()
    async def versions(self, namespace, filename):
        raise NotImplementedError()
    async def store(self, stream, namespace, filename):
        raise NotImplementedError()
