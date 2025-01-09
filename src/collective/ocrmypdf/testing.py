# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.ocrmypdf


class CollectiveOcrmypdfLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.ocrmypdf)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.ocrmypdf:default')


COLLECTIVE_OCRMYPDF_FIXTURE = CollectiveOcrmypdfLayer()


COLLECTIVE_OCRMYPDF_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_OCRMYPDF_FIXTURE,),
    name='CollectiveOcrmypdfLayer:IntegrationTesting',
)


COLLECTIVE_OCRMYPDF_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_OCRMYPDF_FIXTURE,),
    name='CollectiveOcrmypdfLayer:FunctionalTesting',
)


COLLECTIVE_OCRMYPDF_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_OCRMYPDF_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveOcrmypdfLayer:AcceptanceTesting',
)
