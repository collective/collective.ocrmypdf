# -*- coding: utf-8 -*-


def handler(obj, event):
    """Event handler"""
    print("{0} on object {1}".format(event.__class__, obj.absolute_url()))
