#
# Copyright (c) 2013, Digium, Inc.
# Copyright (c) 2018, AVOXI, Inc.
#

"""ARI client library
"""

import aripy3.client
import swaggerpy3.http_client
import urllib.parse

from .client import ARIClient

async def connect(base_url, username, password):
    """Helper method for easily connecting to ARI.

    :param base_url: Base URL for Asterisk HTTP server (http://localhost:8088/)
    :param username: ARI username
    :param password: ARI password.
    :return:
    """
    split = urllib.parse.urlsplit(base_url)
    http_client = swaggerpy3.http_client.AsyncHttpClient()
    http_client.set_basic_auth(split.hostname, username, password)
    ari = ARIClient()
    await ari.connect(base_url, http_client)
    return ari
