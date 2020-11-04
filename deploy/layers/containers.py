#!/usr/bin/env python3
import os.path
from aws_cdk import (
    aws_ecr as ecr,
    aws_ecr_assets as assets,
    core
)

src_root_dir = os.path.join(os.path.dirname(__file__),"../..")

class ContainerLayer(core.Stack):
  """
  Configure the containers
  """

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    self.repo = ecr.Repository(self,'WinApp', repository_name='mywin-webapp')
    
    #self.webapp = assets.DockerImageAsset(self,'WinApp',
    #  directory= os.path.join(src_root_dir, "WebApplication1"), target=)