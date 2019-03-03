import asyncio


class Storage:  # TODO necessary ?
    async def search(self, namespace, filename, version):
        raise NotImplementedError()

    async def versions(self, namespace, filename):
        raise NotImplementedError()

    async def store(self, stream, namespace, filename):
        raise NotImplementedError()

    async def delete(self, stream, namespace, filename):
        raise NotImplementedError()

    # Synced version of previous method
    def search_sync(self, namespace, filename, version):
        return asyncio.get_event_loop().run_until_complete(
            self.search(namespace, filename, version)
        )

    def versions_sync(self, namespace, filename):
        return asyncio.get_event_loop().run_until_complete(
            self.versions(namespace, filename)
        )

    def store_sync(self, stream, namespace, filename):
        return asyncio.get_event_loop().run_until_complete(
            self.store(stream, namespace, filename)
        )

    def delete_sync(self, namespace, filename, version):
        return asyncio.get_event_loop().run_until_complete(
            self.delete(namespace, filename, version)
        )
