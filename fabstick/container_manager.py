import libvirt

class DomainManager:
    def __init__(self, names):
        self.names = names

    def connect(self, URI = None):
        try
            self.conn = libvirt.open(URI)
        except libvirt.libvirtError:
            print "Failed to open connection to hyphervisor"
        

    def create(self, name):
        self.containers[name].create(self.default_template)

    def start(self, name):
        self.containers[name].start()
        
    def stop(self):
        for container in self.containers.values():
            container.stop()

    def stop(self, name):
        self.containers[name].stop()