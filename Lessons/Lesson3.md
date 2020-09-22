# Lesson 3

This lesson covers the following:
- Section 1.1 – Setup Development Environment (Azure CLI)
- Section 1.3 – Create Service Principal on Azure (Pull Images)
- Section 1.5 – Deploy job as part of a CI/CD pipeline
 

## Section 1.1 – Setup Development Environment
Install Azure CLI by following instructions here https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest

## Section 1.3 – Create Service Principal on Azure (Pull Images)

This step is needed for the Azure Container instance to pull an image from the Private Docker Repository we created. There are two steps:
- Create the service account
- Create a role-assignment

Create the service principal and save the secrets
```bash
az ad sp create-for-rbac --name sp_corp_test_training --skip-assignment --sdk-auth > local-sp.json
```

> Notice the username and password are saved to the file `local-sp.json`

Next we have to assign the `Azure Container Registry Pull` role-assignment to the new service principal

```bash
$SERVICE_PRINCIPAL_ID = "service_principal_clientId>"
$ACR_REGISTRY_NAME = "<registry_name>"
$ACR_REGISTRY_ID = az acr show --name $ACR_REGISTRY_NAME  --query id --output tsv

# Create the role assignment
az role assignment create --assignee $SERVICE_PRINCIPAL_ID --scope $ACR_REGISTRY_ID --role acrpull

# Show the role assignment
az role assignment list --assignee $SERVICE_PRINCIPAL_ID
```

## Section 1.5 – Deploy job as part of a CI/CD pipeline

These steps outline how to deploy your code to a container instance. These steps would be automated in a build pipeline.

When you make a change to you code, follow these steps:
1. Modify code
2. Test locally
3. Rebuild docker image 
    ```code bash
    docker build --pull --rm -f "dockerfile" -t training:latest "."
    ```
4. Run Docker Image locally 
    ```bash
    docker run --rm -d  training:latest

    #If you want to see STDOUT use 
    docker run --rm -a STDOUT training:latest
    ```
5. Tag for remote registry 
    ```bash
    docker tag training:latest $ACR_REGISTRY_NAME.azurecr.io/training:v4
    ```
6. Login to Azure Container Resigtry 
    ```bash
    az acr login --name $ACR_REGISTRY_NAME
    ```
7. Push image to the registry 
    ```bash 
    docker push $ACR_REGISTRY_NAME.azurecr.io/training:v4
    ```
8. Run the new image on ACI
    ```bash
    az container create --resource-group $RG_NAME --name $CONTAINER_INSTANCE_NAME --image $ACR_REGISTRY_NAME.azurecr.io/training:v3 --registry-username $SERVICE_PRINCIPAL_ID --registry-password $SERVICE_PRINCIPAL_PASSWORD --restart-policy Never
    
    # Or use a managed identity
    
    az container create --resource-group $RG_NAME --name $CONTAINER_INSTANCE_NAME --image $ACR_REGISTRY_NAME.azurecr.io/training:v3 --assign-identity "/subscriptions/<subscription_id>/resourcegroups/<rg_name>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<identity_id>"  --registry-username $SERVICE_PRINCIPAL_ID --registry-password $SERVICE_PRINCIPAL_PASSWORD --restart-policy Never
    ```

## Additional Info

If you need to get the details of your container use

```bash
az container export -g <resource_group> --name <container_name> -f output.yaml
```

Delete a container
```code bash
az container delete --resource-group training --name training 
```

Create a Role Assignment for Reader
```bash
az role assignment list --assignee <identity_id>
az role assignment create --assignee <service principal id> --role "Reader" --scope /subscriptions/<subscription_id>
```