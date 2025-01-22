# -*- coding: utf-8 -*-
import json
import redis

from collective.ocrmypdf.datamanager import queue_callback
from collective.ocrmypdf.config import REDIS_HOST, REDIS_PORT, REDIS_CHANNEL


def handler(obj, event):
    """Publish UID of PDF files to the Redis channel."""
    redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    if obj.content_type() == "application/pdf":
        uid = obj.UID()
        message = {"uid": uid}
        data = json.dumps(message)

        def callback():
            redis_client.publish(REDIS_CHANNEL, data)

        queue_callback(callback)
