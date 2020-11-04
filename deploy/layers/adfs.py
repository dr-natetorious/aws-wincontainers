from aws_cdk.aws_ec2 import IVpc
from aws_cdk import (
    aws_ec2 as ec2,
    aws_directoryservice as ldap,
    core
)

class DirectoryServicesLayer(core.Construct):
  """
  Configure and deploy the network
  """
  def __init__(self, scope: core.Construct, id: str, vpc:IVpc, subnet_ids:list, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)
    
    # Provision MS ADFS
    self.__msftadfs = ldap.CfnMicrosoftAD(self,'WinLDAP',
      name='adfs.virtual.world',
      short_name='virtualworld',
      password='P0Rsh911!',
      vpc_settings= ldap.CfnMicrosoftAD.VpcSettingsProperty(subnet_ids=subnet_ids, vpc_id= vpc.vpc_id),
      create_alias=True,
      enable_sso=True)

  @property
  def adfs(self) -> ldap.CfnMicrosoftAD:
    return self.__msftadfs