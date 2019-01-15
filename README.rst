=======
pyfiles
=======


.. image:: https://img.shields.io/pypi/v/pyfiles.svg
        :target: https://pypi.python.org/pypi/pyfiles

.. image:: https://img.shields.io/travis/jrmi/pyfiles.svg
        :target: https://travis-ci.org/jrmi/pyfiles

.. image:: https://readthedocs.org/projects/pyfiles/badge/?version=latest
        :target: https://pyfiles.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/jrmi/pyfiles/shield.svg
     :target: https://pyup.io/repos/github/jrmi/pyfiles/
     :alt: Updates



A Big file collection manager.

Usage
-----

Start inside the served data directory.


API
----

**GET** on `/file/<namespace>/<filename>[?version=<version>]`

To download a file. Namespace is a namespace to organise data and filename is the filename.
You can optionnaly add a version like `latest` or `<year>` or `<year.month>`, ...
You get the latest for the specified version.

**GET** on `/versions/<namespace>/<filename>`

To show all avaible file versions.

Features
--------

* An API to download files with rich version selection
* List all version of a file
* Can be used for CSV or Geojson files
* File can have version like 2018.01.10-01
* Find file by a part of the version. `2018` or `2018.01`

Roadmap
-------

* Handle file diff between versions
* Allow authentification with private data
* Be storage agnostic
* Get the update date of a file to ease caching
* Add a client library and CLI

License
------

* Free software: MIT license
* Documentation: https://pyfiles.readthedocs.io.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
