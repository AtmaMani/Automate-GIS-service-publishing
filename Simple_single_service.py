# This is a simple ArcPy script to publish a single map document as a service.
import arcpy
print("Imported ArcPy")

# Initialize the variables
mxd = r'E:\UC_demo\Publishing\simple_publishing\TyphoonAlberta.mxd'
server_con = r'E:\UC_demo\Publishing\simple_publishing\local_server.ags'
service_name = "TyphoonAlberta_python"

# Set output path
sd_file = r'E:\UC_demo\Publishing\simple_publishing\TyphoonAlberta.sd'
sddraft_file = r'E:\UC_demo\Publishing\simple_publishing\TyphoonAlberta.sddraft'

# Create a service definition draft
analysis_result = arcpy.mapping.CreateMapSDDraft(mxd, sddraft_file, service_name)
print("SDdraft file created")

# Stage and create Service Definition file
arcpy.StageService_server(sddraft_file, sd_file)
print("Service Definition file created")


# Publish the SD file as a service
arcpy.UploadServiceDefinition_server(sd_file, server_con)
print("Service published successfully")