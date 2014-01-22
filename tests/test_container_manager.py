import sys
import libvirt

from unittest import TestCase

from fabstick.domain_manager import DomainManager

domains = ['keystone','nova','ceilometer','swift']

class SimpleDomainTestCase(TestCase):
    def setUp(self):
        self.domains = domains
        self.domain_manager = DomainManager(self.domains)
        self.conn = self.domain_manager.connect()

    def tearDown(self):
        if(self.conn.isAlive()):
            self.domain_manager.close()

class DomainManagerTestCase(SimpleDomainTestCase):
    def test_isalive(self):
        self.assertEqual(self.conn.isAlive(),True)
        self.domain_manager.close()

    def test_start_domain(self):
        with self.assertRaises(libvirt.libvirtError):
            for domain_name in self.domains:
                domain = self.conn.lookupByName(domain_name)


    def test_stop_domain(self):
        pass

    def test_domain_attr(self):
        pass

    def test_add_device(self):
        pass

    def test_del_device(self):
        pass

    def test_set_network(self):
        pass

    def test_clear_network(self):
        pass

    