#!/usr/bin/env python3
import os.path
from aws_cdk.core import App, Stack, Environment
from layers.basenet import BaseNetworkingLayer
from layers.containers  import ContainerLayer
from layers.adfs import DirectoryServicesLayer

src_root_dir = os.path.join(os.path.dirname(__file__),"..")

default_env= Environment(region="us-west-2")

app = App()
networking  = BaseNetworkingLayer(app, "WinContainers", env=default_env)
containers = ContainerLayer(app,'ContainerLayer', env=default_env)
ldap = DirectoryServicesLayer(app,'AuthLayer', vpc= networking.eks.vpc, env= default_env)

app.synth()
