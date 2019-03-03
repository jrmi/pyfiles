import os

from pyfiles.storages.core import Storage


class DiskStorage(Storage):
    def __init__(self, basepath, base_url):
        self.base = os.path.realpath(basepath)
        self.base_url = base_url

    async def search(self, namespace, filename, version="latest"):
        basename = os.path.join(self.base, *namespace.split("."))

        # TODO Should we awaitable
        all_files = sorted(os.listdir(basename))

        # TODO add regex match for YYYY_MM_DD-VV__<filename>
        filelist = [f for f in all_files if f.endswith(filename)]

        if version != "latest":
            filelist = [f for f in filelist if f.startswith(version)]

        if not filelist:
            return None

        selected_file = filelist[-1]

        # TODO Add url prefix here
        filepath = os.path.join(basename, selected_file)

        return {
            "version": selected_file.split("__")[0],
            "url": f"{self.base_url}{filepath}",
        }

    async def versions(self, namespace, filename):
        basename = os.path.join(self.base, *namespace.split("."))

        # TODO Should we awaitable
        all_files = sorted(os.listdir(basename))

        versionlist = [f.split("__")[0] for f in all_files if f.endswith(filename)]

        return versionlist

    async def store(self, stream, namespace, filename, version):
        basename = os.path.join(self.base, *namespace.split("."))

        try:
            os.makedirs(basename)
        except OSError:
            pass

        filepath = os.path.join(basename, f"{version}__{filename}")

        # TODO make it async
        with open(filepath, "wb") as fout:
            fout.write(stream.read())

    async def delete(self, namespace, filename, version):
        basename = os.path.join(self.base, *namespace.split("."))
        filepath = os.path.join(basename, f"{version}__{filename}")

        # TODO make it async
        os.remove(filepath)
