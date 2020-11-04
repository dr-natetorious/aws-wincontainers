#!/usr/bin/env python3
import os.path
from aws_cdk import (
    aws_ecr as ecr,
    aws_ecr_assets as assets,
    core
)

src_root_dir = os.path.join(os.path.dirname(__file__),"../..")

class ContainerLayer(core.Construct):
  """
  Configure the containers
  """

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    self.repo = ecr.Repository(self,'WinApp', repository_name='helloworld-windows-webapp')
