#!/usr/bin/env python3
from aws_cdk import (
    aws_ec2 as ec2,
    aws_directoryservice as ldap,
    aws_eks as eks,
    core
)

class BaseNetworkingLayer(core.Construct):
  """
  Configure and deploy the network
  """
  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    self.__vpc = ec2.Vpc(self,'MyVpc', cidr='10.10.0.0/16')

    self.__eks = eks.Cluster(self, 'WinCtrEksCluster',
      version= eks.KubernetesVersion.V1_18,
      default_capacity=0,
      vpc= self.vpc,
      endpoint_access= eks.EndpointAccess.PUBLIC)

    self.__private_subnet_ids = []
    for net in self.eks_cluster.vpc.private_subnets:
      self.__private_subnet_ids.append(net.subnet_id)

  @property
  def vpc(self) -> ec2.Vpc:
    return self.__vpc

  @property
  def private_subnets_ids(self) -> list:
    return self.__private_subnet_ids

  @property
  def eks_cluster(self) -> eks.Cluster:
    return self.__eks
