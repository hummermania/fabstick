import sys
import unittest

from fabstick.container_manager import ContainerManager

containers = ['keystone','nova','ceilometer','swift']

class SimpleContainerTestCase(unittest.TestCase):
    def setUp(self):
        self.cntr_mgr = ContainerManager(containers)

    def tearDown(self):
        self.cntr_mgr.stop(self.name)

class ContainerManagerTestCase(SimpleContainerTestCase):
    def test_container_attr(self):
        self.assertEqual(self.cntr_mgr.name,'keystone')
        self.assertEqual(self.cntr_mgr.template,'Ubuntu')

    def test_start_container(self):
        self.cntr_mgr.start(self.name)
        self.cntr_mgr.is_active(self.name)