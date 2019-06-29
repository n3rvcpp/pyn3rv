import zmq
from n3rv.binding import binding

class servicecontroller:

    def __init__(self, binding_addr, binding_port, logger):

        self.directory = []

        self.binding_addr = binding_addr
        self.binding_port = binding_port
        self.logger = logger

        self.running = False
        self.context = zmq.Context()
        self.zmsock = self.context.socket(zmq.REP)
        self.zmsock_pub = self.context.socket(zmq.PUB)

        self.zmsock.bind("tcp://{}:{}".format(self.binding_addr, self.binding_port))
        self.zmsock.bind("tcp://{}:{}".format(self.binding_addr, self.binding_port + 1))


    def run(self):
        self.running = True
        while(self.running):
            msg = self.zmsock.recv_json()
            if (msg.action == "subscribe"):

                b = binding()
                




       
    def load_topology_file(self, topology_file):
        return

    def load_topology(self, topology):
        return