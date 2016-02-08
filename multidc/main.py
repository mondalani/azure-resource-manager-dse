import json
import opsCenterNode
import dseNodes

# This python script generates an ARM template that deploys DSE across multiple datacenters.

with open('clusterParameters.json') as inputFile:
    clusterParameters = json.load(inputFile)

locations = clusterParameters['locations']
vmSize = clusterParameters['vmSize']
nodeCount = clusterParameters['nodeCount']
adminUsername = clusterParameters['adminUsername']
adminPassword = clusterParameters['adminPassword']
nodeType = clusterParameters['nodeType']

# This is the skeleton of the template that we're going to add resources to
generatedTemplate = {
    "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {},
    "variables": {},
    "resources": [],
    "outputs": {}
}

# Create DSE nodes in each location
for location in locations:
    datacenterIndex = locations.index(location) + 1
    resources = dseNodes.generate_template(location, datacenterIndex, vmSize, nodeCount, adminUsername, adminPassword)
    generatedTemplate['resources'] += resources

# Create the OpsCenter node
#resources = opsCenterNode.generate_template(clusterParameters)
#generatedTemplate['resources'] += resources


# Add the opsCenterURL
def opsCenterURL():
    return {
        "opsCenterURL": {
            "type": "string",
            "value": "[concat('http://opsc', variables('uniqueString'), '.', " + locations[0] + ", '.cloudapp.azure.com:8888')]"
        }
    }

generatedTemplate['outputs'] += opsCenterURL()

with open('generatedTemplate.json', 'w') as outputFile:
    json.dump(generatedTemplate, outputFile, sort_keys=True, indent=4, ensure_ascii=False)
