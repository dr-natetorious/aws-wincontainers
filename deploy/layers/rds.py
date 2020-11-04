from aws_cdk.aws_ec2 import IVpc
from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_directoryservice as ldap,
    aws_rds as rds,
    core
)

class DatabaseLayer(core.Construct):
  """
  Configure and deploy the network
  """
  def __init__(self, scope: core.Construct, id: str, vpc:IVpc, subnet_ids:list, adfs:ldap.CfnMicrosoftAD, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    sql2ad_role = iam.Role(self,'RDSDirectoryServicesRole',
      assumed_by= iam.ServicePrincipal("rds.amazonaws.com"),
      managed_policies=[
        iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonRDSDirectoryServiceAccess")
    ])

    rds.DatabaseInstance(self,'WebDatabase',
      engine= rds.DatabaseInstanceEngine.sql_server_web(version= rds.SqlServerEngineVersion.VER_15),
      storage_encrypted=True,
      instance_type= ec2.InstanceType.of(ec2.InstanceClass.STANDARD5, ec2.InstanceSize.LARGE),
      auto_minor_version_upgrade=True,
      vpc= vpc,
      credentials= rds.Credentials.from_username(username='sqladmin'), # passwd = admin
      enable_performance_insights=True,
      multi_az=False,
      domain=adfs.ref,
      domain_role=sql2ad_role
    )
