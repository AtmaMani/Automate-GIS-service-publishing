#Script to demonstrate overwriting a service.
import arcpy
from sddraft_modifiers import HostedFeatureServiceProperties
print("Imported ArcPy")

# Initialize the variables
mxd = r'E:\UC_demo\Publishing\advanced_publishing\Good_cartography.mxd'
server_con = r'MY_HOSTED_SERVICES'
service_name = "Fortune_500_companies"

# Set output path
sd_file = r'E:\UC_demo\Publishing\advanced_publishing\overwrite.sd'
sddraft_file = r'E:\UC_demo\Publishing\advanced_publishing\overwrite.sddraft'

# Create a service definition draft
analysis_result = arcpy.mapping.CreateMapSDDraft(mxd, sddraft_file, service_name, server_con)
print("Initial SDdraft file created")

# Convert service type to Feature Service
service_properties = HostedFeatureServiceProperties(sddraft_file)
service_properties.change_to_feature_service()
print("Service type changed to Hosted Feature Service")

# Enable editing capability
service_properties.modify_web_capabilities("Editing")
print("Edit capability enabled")

# Convert publishing operation as overwrite
service_properties.modify_for_overwriting()
print("Updated publishing operation as overwrite")

# Stage and create Service Definition file
arcpy.StageService_server(sddraft_file, sd_file)
print("Service Definition file created")

 # Publish the SD file as a service
arcpy.UploadServiceDefinition_server(sd_file, "My Hosted Services")
print("Service published successfully")