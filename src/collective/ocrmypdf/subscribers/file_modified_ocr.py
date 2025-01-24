# -*- coding: utf-8 -*-
import json
import redis
from zope.globalrequest import getRequest
from collective.ocrmypdf.datamanager import queue_callback
from collective.ocrmypdf.config import REDIS_HOST, REDIS_PORT, REDIS_CHANNEL

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)


def handler(obj, event):
    """Publish UID of PDF files to the Redis channel."""

    if obj.content_type() == "application/pdf":
        request = getRequest()
        # Check the 'ocr' flag to prevent re-triggering the handler
        # when the processed file is uploaded by the consumer.
        ocr_flag = request.form.get("ocr")

        if ocr_flag == "1":
            return

        uid = obj.UID()
        message = {"uid": uid}
        data = json.dumps(message)

        def callback():
            redis_client.publish(REDIS_CHANNEL, data)

        queue_callback(callback)
