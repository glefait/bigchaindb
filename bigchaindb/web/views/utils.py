# Copyright BigchainDB GmbH and BigchainDB contributors
# SPDX-License-Identifier: (Apache-2.0 AND CC-BY-4.0)
# Code is Apache-2.0 and docs are CC-BY-4.0

"""This module provides the blueprint for the blocks API endpoints.

For more information please refer to the documentation: http://bigchaindb.com/http-api
"""
from flask import jsonify
from flask_restful import Resource, reqparse
from bigchaindb.commands import bigchaindb
from argparse import Namespace
import logging


logger = logging.getLogger(__name__)


class CleanApi(Resource):
    def get(self):
        logger.warning("drop and recreate DB")
        args = Namespace(config=None, yes=True)
        bigchaindb.run_drop(args)
        bigchaindb.run_init(args)
        return jsonify({})
