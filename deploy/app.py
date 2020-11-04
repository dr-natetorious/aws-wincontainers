#!/usr/bin/env python3
import os.path
from aws_cdk.core import App, Stack, Environment
from layers.basenet import BaseNetworkingLayer
from layers.containers  import ContainerLayer
from layers.adfs import DirectoryServicesLayer
from layers.rds import DatabaseLayer

src_root_dir = os.path.join(os.path.dirname(__file__),"..")

default_env= Environment(region="us-west-2")

def create_infra_stack(infra_stack):
    networking  = BaseNetworkingLayer(infra_stack, "BaseNetworkingLayer")
    containers = ContainerLayer(infra_stack,'ContainerLayer')
    ds = DirectoryServicesLayer(infra_stack,'AuthLayer', vpc= networking.vpc, subnet_ids= networking.private_subnets_ids)
    rds = DatabaseLayer(infra_stack,'DatabaseLayer', vpc= networking.vpc, subnet_ids= networking.private_subnets_ids, adfs=ds.adfs)

app = App()
infra_stack = Stack(app,'VirtualWorld', env=default_env)
create_infra_stack(infra_stack)

app.synth()
