# import statements
import os, glob
import arcpy

print("ArcPy imported")

# Set Path and Variables
map_path = r'E:\UC_demo\Publishing\batch_publishing\\'
svr_con = r'E:\UC_demo\Publishing\batch_publishing\local_server.ags'

# Find maps in folder
map_list = glob.glob(map_path + "*.mxd")
print("Total number of maps found: " + str(len(map_list)))

# Reference data using Data Store
arcpy.AddDataStoreItem(svr_con, "FOLDER", "datastore_registered_with_Python",
                       r"E:\UC_demo\Data")

# Loop through each map in list
for current_map in map_list:
    print("----------------------------------")

    # Set Variables
    mxd = arcpy.mapping.MapDocument(current_map)
    service_name = os.path.basename(current_map)[:-4]
    sddraft = map_path + service_name + ".sddraft"
    sd = map_path + service_name + ".sd"

    # Create Service Definition Draft
    analysis = arcpy.mapping.CreateMapSDDraft(mxd, sddraft, service_name,
                    "ARCGIS_SERVER", svr_con, folder_name="Store_locations",
                    summary="Southern California store locations", tags="location analysis")

    print("Publishing " + service_name)

    # Stage into a Service Definition file
    arcpy.StageService_server(sddraft, sd)
    print("Staged")

    # Upload and publish
    arcpy.UploadServiceDefinition_server(sd, svr_con)

    print("Published")
