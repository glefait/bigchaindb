# Copyright BigchainDB GmbH and BigchainDB contributors
# SPDX-License-Identifier: (Apache-2.0 AND CC-BY-4.0)
# Code is Apache-2.0 and docs are CC-BY-4.0

"""This module provides the blueprint for the blocks API endpoints.

For more information please refer to the documentation: http://bigchaindb.com/http-api
"""
from flask import current_app
from flask_restful import Resource, reqparse
import logging
from bigchaindb.web.views.base import make_error


logger = logging.getLogger(__name__)


class LatestBlockApi(Resource):
    def get(self):
        logger.info("Retrieving latest block")
        pool = current_app.config['bigchain_pool']

        with pool() as bigchain:
            block = bigchain.get_latest_block()

        if not block:
            return make_error(404)

        return block
