import lxc

class ContainerManager:
    def __init__(self, names, default_template = 'ubuntu'):
        self.names = names
        self.default_template = default_template
        self.containers = {}

    def create(self):
        for container_name in self.names:
            try:
                container = lxc.Container(container_name)
            except Exception, e:
                raise e
            
            self.containers[container_name] = container

    def create(self, name):
        self.containers[name].create(self.default_template)

    def start(self, name):
        self.containers[name].start()
        
    def stop(self):
        for container in self.containers.values():
            container.stop()

    def stop(self, name):
        self.containers[name].stop()