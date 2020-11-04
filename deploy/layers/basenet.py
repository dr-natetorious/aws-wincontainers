#!/usr/bin/env python3
from aws_cdk import (
    aws_ec2 as ec2,
    aws_directoryservice as ldap,
    aws_eks as eks,
    core
)

class BaseNetworkingLayer(core.Stack):
  """
  Configure and deploy the network
  """
  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    self.eks = eks.Cluster(self, 'WinCtrEksCluster',
      version= eks.KubernetesVersion.V1_18,
      endpoint_access= eks.EndpointAccess.PUBLIC)

    self.subnet_ids = []
    for net in self.eks.vpc.private_subnets:
      self.subnet_ids.append(net.subnet_id)

    for net in self.eks.vpc.public_subnets:
      self.subnet_ids.append(net)

  