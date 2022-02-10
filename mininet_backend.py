import sys
sys.path.insert(0, '/home/mininet')   

import time, os
import numpy as np

from os import system
from mininet.net import Mininet
from mininet.net import Mininet,CLI
from mininet.node import OVSSwitch, Host, RemoteController
from mininet.link import TCLink,Link
from mininet.log import setLogLevel, info
from typing import List

TOPOLOGY_FILE_NAME = 'topology_arpanet.txt'

bw_capacity = {}

class MininetBackend():
    global number_hosts

    def __init__(self):
        self.net, self.bw_capacity = self.start_network()
        #add arps

    def add_host(self, net, host):
        if host not in net.keys():
            net.addHost(host)

    def add_switch(self, net, switch):
        if switch not in net.keys():
            net.addSwitch(switch, cls=OVSSwitch) 

    def add_link(self, net, src, dst, link_bw):
        if len(net.linksBetween(net.getNodeByName(src), net.getNodeByName(dst))) == 0:
            net.addLink(net.getNodeByName(src), net.getNodeByName(dst), **dict(bw=link_bw, delay='1ms', loss=0))

    def build_topology_from_txt(self, net):
        global bw_capacity
    
        with open(TOPOLOGY_FILE_NAME, 'r') as topo:
            for row in topo.readlines():
                row_data : List[str] = row.split()
                for node in row_data:
                    if 'H' in node:
                        self.add_host(net, node)
                    elif 'S' in node:
                        self.add_switch(net, node)
                link_bw : int = int(row_data[2])
                self.add_link(net, row_data[0], row_data[1], link_bw)
                bw_capacity[(row_data[0], row_data[1])] = link_bw
                bw_capacity[(row_data[1], row_data[0])] = link_bw

    def start_network(self):
        system('clear')
        system('sudo mn -c')
        setLogLevel('info')
        net = Mininet(controller=RemoteController, switch=OVSSwitch, link=TCLink, autoSetMacs=True, ipBase='10.0.0.0/24')
    
        self.build_topology_from_txt(net)
        net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
        net.start()
    
        return bw_capacity, net
