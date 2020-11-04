from aws_cdk.aws_ec2 import IVpc
from aws_cdk import (
    aws_ec2 as ec2,
    aws_directoryservice as ldap,
    core
)

class DirectoryServicesLayer(core.Stack):
  """
  Configure and deploy the network
  """
  def __init__(self, scope: core.Construct, id: str, vpc:IVpc, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    # Get the subnet_id for PUBLIC | PRIVATE networks
    self.subnet_ids = []
    for net in vpc.private_subnets:
      self.subnet_ids.append(net.subnet_id)

    #for net in vpc.public_subnets:
    #  self.subnet_ids.append(net.subnet_id)

    # Provision MS ADFS
    self.ldap = ldap.CfnMicrosoftAD(self,'WinLDAP',
        name='ad.virtual.world',
        short_name='virtualworld',
        password='P0Rsh911!',
        vpc_settings= ldap.CfnMicrosoftAD.VpcSettingsProperty(subnet_ids=self.subnet_ids, vpc_id= vpc.vpc_id),
        create_alias=True,
        enable_sso=True)