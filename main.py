#!/usr/bin/python
import json

# import os
from azure.common.client_factory import get_client_from_json_dict
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import SubscriptionClient
from cred_wrapper import CredentialWrapper


# class AuthException(ValueError):
#     """Auth process failed for some reason."""

#     def __str__(self):
#         return "Failed to authenticate to Azure. Have you set the AZURE_AUTH environment variable?"


# def get_management_client(azure_auth, client_class):
#     """Returns SDK Client for the given client_class."""
#     client = None
#     if azure_auth is not None:
#         print(f"Getting SDK Client for {client_class}")
#         auth_config_dict = json.loads(azure_auth)
#         client = get_client_from_json_dict(client_class, auth_config_dict)
#     else:
#         raise AuthException()
#     return client


def main():
    """Main function to get metrics"""
    # azure_auth = os.environ.get("AZURE_AUTH")
    # compute_client = get_management_client(azure_auth, ComputeManagementClient)

    # credential = DefaultAzureCredential()
    credential = CredentialWrapper()

    subscription_client = SubscriptionClient(credential)
    subscription = next(subscription_client.subscriptions.list())
    print(subscription.subscription_id)

    compute_client = ComputeManagementClient(
        credentials=credential, subscription_id=subscription.subscription_id
    )

    for virtual_machine in compute_client.virtual_machines.list_all():
        print(f"{virtual_machine.name} {virtual_machine.id}")


if __name__ == "__main__":

    print("hello world brig")
    main()
