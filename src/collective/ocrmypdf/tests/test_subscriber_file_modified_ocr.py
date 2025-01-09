# -*- coding: utf-8 -*-
from collective.ocrmypdf.testing import COLLECTIVE_OCRMYPDF_FUNCTIONAL_TESTING
from collective.ocrmypdf.testing import COLLECTIVE_OCRMYPDF_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class SubscriberIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_OCRMYPDF_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])


class SubscriberFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_OCRMYPDF_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
