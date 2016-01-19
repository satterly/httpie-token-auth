httpie-token-auth
=================

`Access Token <http://tools.ietf.org/html/rfc6750>`_ auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.

Provides generic support for presenting access tokens of any type as long as they can be added to the ``Authorization``
header in the below format:

.. code-block::

    Authorization: <token_type> <token>

Installation
------------

.. code-block:: bash

    $ pip install httpie-token-auth

You should now see ``token`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http --auth-type=token --auth='<token_type>:<token>' example.org

Examples
--------

To access a protected resource with a "bearer" token:

.. code-block:: bash

    $ http --auth-type=token --auth="Bearer:mF_9.B5f-4.1JqM" example.org

To access a protected resource with a "mac" token:

.. code-block:: bash

    $ http --auth-type=token --auth='MAC:token="h480djs93hd8"' example.org

License
-------

Copyright (c) 2016 Nick Satterly. Available under the MIT License.
