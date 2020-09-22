Create Service Principal
------------------------

```bash
az ad sp create-for-rbac --name localtest-sp-rbac --skip-assignment --sdk-auth > local-sp.json
```

Upload Docker
-------------

Upload your docker image to a remote repository by building, tagging, and pushing

```code bash
docker build --pull --rm -f "dockerfile" -t training:latest "."
```

```code bash
docker tag training:latest <repository_name>.azurecr.io/training:latest
```

```code bash
docker push blxcontainerregistry.azurecr.io/training:latest
```

Update Container Instance
-------------------------

```code bash
az container create --resource-group <resource_group> --name <container_name) --image <registryname>.azurecr.io/<image_name>:<version> --registry-username <username> --registry-password <password> --restart-policy Never

# Get details of container
az container export -g <resource_group> --name <container_name> -f output.yaml

# Use a managed identity
az container create --resource-group <rg-name> --name <name-of-contianer-instance>  --image <imagename> --assign-identity "/subscriptions/<subscription_id>/resourcegroups/<rg_name>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<identity_id>"  --registry-username <replace> --registry-password <replace> --restart-policy Never

```

```code bash
az container delete --resource-group training --name training 
```


Create Role Assignment
-----------------------

```bash
az role assignment list --assignee <identity_id>
az role assignment create --assignee <service principal id> --role "Reader" --scope /subscriptions/<subscription_id>
```