# A small python library to modify SDdraft files created during publishing.
""" SDdraft files contain the service configuration. Modifying this allows customizing
 the service being published. This library is not complete and is just a sample to
 showcase the possibility"""

import xml.dom.minidom as DOM
import os
import codecs


class HostedFeatureServiceProperties(object):
    sddraft_path = ""

    def __init__(self, sddraft_path):
        self.sddraft_path = sddraft_path
        if not os.path.exists(self.sddraft_path):
            print("File not found. Check the path")

    def change_to_feature_service(self):
        """Change service type from one to another. Valid values include
        soe: FeatureServer"""

        xml = self.sddraft_path
        doc = DOM.parse(xml)
        featureServiceExt = doc.getElementsByTagName('TypeName')[0]
        if featureServiceExt.parentNode.tagName == 'SVCConfiguration':
            if featureServiceExt.hasChildNodes():
                featureServiceExt.firstChild.data = "FeatureServer"
        configProps = doc.getElementsByTagName('ConfigurationProperties')[0]
        propArray = configProps.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "isCached":
                        keyValue.nextSibling.firstChild.data = "false"
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def modify_web_capabilities(self, newCapabilities):
        """
        Method to update service capabilities
        :param newCapabilities: 'Create,Delete,Query,Update,Uploads,Editing'
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        stagingSettings = doc.getElementsByTagName('Info')[0]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "WebCapabilities":
                        keyValue.nextSibling.firstChild.data = newCapabilities
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def modify_for_overwriting(self):
        """
        Method to create a SD file to overwrite an existing service
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        descriptions = doc.getElementsByTagName('Type')
        for desc in descriptions:
            if desc.parentNode.tagName == 'SVCManifest':
                if desc.hasChildNodes():
                    desc.firstChild.data = 'esriServiceDefinitionType_Replacement'
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def modify_max_record_count(self, maxRecords):
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        stagingSettings = doc.getElementsByTagName('ConfigurationProperties')[0]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "maxRecordCount":
                        keyValue.nextSibling.firstChild.data = maxRecords
        stagingSettings = doc.getElementsByTagName('Props')[1]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "maxRecordCount":
                        keyValue.nextSibling.firstChild.data = maxRecords
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def modify_allow_geometry_updates(self, allowGeometryUpdates):
        """
        Turn on geometry updates during service editing.
        :param allowGeometryUpdates: true, false
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        stagingSettings = doc.getElementsByTagName('ConfigurationProperties')[0]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "allowGeometryUpdates":
                        keyValue.nextSibling.firstChild.data = allowGeometryUpdates
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()


class HostedTileServiceProperties(object):
    sddraft_path = ""

    def __init__(self, sddraft_path):
        self.sddraft_path = sddraft_path
        if not os.path.exists(self.sddraft_path):
            print("File not found. Check the path")

    def modify_initial_cache_LOD(self, level, levelID):
        xml = self.sddraft_path
        doc = DOM.parse(xml)

        configProps = doc.getElementsByTagName('InitialCacheInfos')[0]
        propArray = configProps.childNodes[level]
        propSets = propArray.childNodes
        for propSet in propSets:
            if propSet.tagName == 'LevelID':
                if propSet.hasChildNodes():
                    propSet.firstChild.data = levelID
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def modify_tile_image_type(self, imageType):
        """
        Modify the tile image format in cache
        :imageType: 'JPEG' , 'PNG8'
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        descriptions = doc.getElementsByTagName('CacheTileFormat')
        for desc in descriptions:
            if desc.parentNode.tagName == 'TileImageInfo':
                if desc.hasChildNodes():
                    desc.firstChild.data = imageType
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def modify_tile_image_compression(self, imageComp):
        """
        Modify the compression factor of tiles in cache
        :param imageComp: 100, 75 etc
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        descriptions = doc.getElementsByTagName('CompressionQuality')
        for desc in descriptions:
            if desc.parentNode.tagName == 'TileImageInfo':
                if desc.hasChildNodes():
                    desc.firstChild.data = imageComp
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def modify_DPI(self, dpi):
        """
        Modify the DPI factor of tiles in cache
        :param dpi: 96, 72 etc
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        descriptions = doc.getElementsByTagName('DPI')
        for desc in descriptions:
            if desc.parentNode.tagName == 'TileCacheInfo':
                if desc.hasChildNodes():
                    desc.firstChild.data = dpi
        descriptions = doc.getElementsByTagName('PreciseDPI')
        for desc in descriptions:
            if desc.parentNode.tagName == 'TileCacheInfo':
                if desc.hasChildNodes():
                    desc.firstChild.data = dpi
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def enable_caching(self):
        """
        Enable caching when publishing a map service to arcgis server
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        stagingSettings = doc.getElementsByTagName('ConfigurationProperties')[0]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "isCached":
                        keyValue.nextSibling.firstChild.data = "true"
        outXml = xml
        f = codecs.open(outXml, 'w', 'utf-8')
        doc.writexml(f)
        f.close()

    def modify_for_overwriting(self):
        """
        Method to create a SD file to overwrite an existing service
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        descriptions = doc.getElementsByTagName('Type')
        for desc in descriptions:
            if desc.parentNode.tagName == 'SVCManifest':
                if desc.hasChildNodes():
                    desc.firstChild.data = 'esriServiceDefinitionType_Replacement'
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()


class MapServiceProperties(object):
    sddraft_path = ""

    def __init__(self, sddraft_path):
        self.sddraft_path = sddraft_path
        if not os.path.exists(self.sddraft_path):
            print("File not found. Check the path")

    def modify_for_overwriting(self):
        """
        Method to create a SD file to overwrite an existing service
        :return:
        """
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        descriptions = doc.getElementsByTagName('Type')
        for desc in descriptions:
            if desc.parentNode.tagName == 'SVCManifest':
                if desc.hasChildNodes():
                    desc.firstChild.data = 'esriServiceDefinitionType_Replacement'
        outXml = xml
        f = open(outXml, 'w')
        doc.writexml(f)
        f.close()

    def enable_SOE(self, soe):

        xml = self.sddraft_path
        doc = DOM.parse(xml)
        typeNames = doc.getElementsByTagName('TypeName')
        for typeName in typeNames:
            if typeName.firstChild.data == soe:
                extention = typeName.parentNode
                for extElement in extention.childNodes:
                    # enable soe
                    if extElement.tagName == 'Enabled':
                        extElement.firstChild.data = 'true'
        outXml = xml
        f = codecs.open(outXml, 'w', 'utf-8')
        doc.writexml(f)
        f.close()

    def modify_SOE(self, soe, soeProperty, soePropertyValue):
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        typeNames = doc.getElementsByTagName('TypeName')
        for typeName in typeNames:
            # Get the TypeName whose properties we want to modify.
            if typeName.firstChild.data == soe:
                extention = typeName.parentNode
                for extElement in extention.childNodes:
                    if extElement.tagName == 'Props':
                        for propArray in extElement.childNodes:
                            for propSet in propArray.childNodes:
                                for prop in propSet.childNodes:
                                    if prop.tagName == "Key":
                                        if prop.firstChild.data == soeProperty:
                                            if prop.nextSibling.hasChildNodes():
                                                prop.nextSibling.firstChild.data = soePropertyValue
                                            else:
                                                txt = doc.createTextNode(soePropertyValue)
                                                prop.nextSibling.appendChild(txt)

        outXml = xml
        f = codecs.open(outXml, 'w', 'utf-8')
        doc.writexml(f)
        f.close()

    def enable_caching(self):
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        stagingSettings = doc.getElementsByTagName('ConfigurationProperties')[0]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "isCached":
                        keyValue.nextSibling.firstChild.data = "true"
        outXml = xml
        f = codecs.open(outXml, 'w', 'utf-8')
        doc.writexml(f)
        f.close()

    def modify_cache_properties(self, xOrigin, yOrigin, cols, rows, dpi, imageType, compression, storageFormat):
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        descriptions = doc.getElementsByTagName('X')
        for desc in descriptions:
            if desc.hasChildNodes():
                desc.firstChild.data = xOrigin
        descriptions = doc.getElementsByTagName('Y')
        for desc in descriptions:
            if desc.hasChildNodes():
                desc.firstChild.data = yOrigin
        descriptions = doc.getElementsByTagName('TileCols')
        for desc in descriptions:
            if desc.hasChildNodes():
                desc.firstChild.data = cols
        descriptions = doc.getElementsByTagName('TileRows')
        for desc in descriptions:
            if desc.hasChildNodes():
                desc.firstChild.data = rows
        descriptions = doc.getElementsByTagName('DPI')
        for desc in descriptions:
            if desc.hasChildNodes():
                desc.firstChild.data = dpi
        descriptions = doc.getElementsByTagName('CacheTileFormat')
        for desc in descriptions:
            if desc.hasChildNodes():
                desc.firstChild.data = imageType
        descriptions = doc.getElementsByTagName('CompressionQuality')
        for desc in descriptions:
            if desc.hasChildNodes():
                desc.firstChild.data = compression
        descriptions = doc.getElementsByTagName('StorageFormat')
        for desc in descriptions:
            if desc.hasChildNodes():
                desc.firstChild.data = storageFormat
        outXml = xml
        f = codecs.open(outXml, 'w', 'utf-8')
        doc.writexml(f)
        f.close()

    def modify_antialias(self, newTextAntialiasingMode, newAntiAliasingMode):
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        stagingSettings = doc.getElementsByTagName('ConfigurationProperties')[0]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "antialiasingMode":
                        keyValue.nextSibling.firstChild.data = newAntiAliasingMode
                    elif keyValue.firstChild.data == "textAntialiasingMode":
                        keyValue.nextSibling.firstChild.data = newTextAntialiasingMode
        outXml = xml
        f = codecs.open(outXml, 'w', 'utf-8')
        doc.writexml(f)
        f.close()

    def modify_service_properties(self, maxRecords, minInstances, maxInstances, maxClientUse, maxClientWait, maxIdle, isolation,
                                instancesPerProcess, recycleInterval, recycleStart, configState, cleanTime):
        xml = self.sddraft_path
        doc = DOM.parse(xml)
        stagingSettings = doc.getElementsByTagName('ConfigurationProperties')[0]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "maxRecordCount":
                        keyValue.nextSibling.firstChild.data = maxRecords
        stagingSettings = doc.getElementsByTagName('Props')[0]
        propArray = stagingSettings.firstChild
        propSets = propArray.childNodes
        for propSet in propSets:
            keyValues = propSet.childNodes
            for keyValue in keyValues:
                if keyValue.tagName == 'Key':
                    if keyValue.firstChild.data == "MinInstances":
                        keyValue.nextSibling.firstChild.data = minInstances
                    elif keyValue.firstChild.data == "MaxInstances":
                        keyValue.nextSibling.firstChild.data = maxInstances
                    elif keyValue.firstChild.data == "UsageTimeout":
                        keyValue.nextSibling.firstChild.data = maxClientUse
                    elif keyValue.firstChild.data == "WaitTimeout":
                        keyValue.nextSibling.firstChild.data = maxClientWait
                    elif keyValue.firstChild.data == "IdleTimeout":
                        keyValue.nextSibling.firstChild.data = maxIdle
                    elif keyValue.firstChild.data == "Isolation":
                        keyValue.nextSibling.firstChild.data = isolation
                    elif keyValue.firstChild.data == "InstancesPerContainer":
                        keyValue.nextSibling.firstChild.data = instancesPerProcess
                    elif keyValue.firstChild.data == "configuredState":
                        keyValue.nextSibling.firstChild.data = configState
                    elif keyValue.firstChild.data == "CleanupTimeout":
                        keyValue.nextSibling.firstChild.data = cleanTime
                    elif keyValue.firstChild.data == "recycleInterval":
                        if keyValue.nextSibling.hasChildNodes():
                            keyValue.nextSibling.firstChild.data = recycleInterval
                        else:
                            txt = doc.createTextNode(recycleInterval)
                            keyValue.nextSibling.appendChild(txt)
                    elif keyValue.firstChild.data == "recycleStartTime":
                        if keyValue.nextSibling.hasChildNodes():
                            keyValue.nextSibling.firstChild.data = recycleStart
                        else:
                            txt = doc.createTextNode(recycleStart)
                            keyValue.nextSibling.appendChild(txt)
        outXml = xml
        f = codecs.open(outXml, 'w', 'utf-8')
        doc.writexml(f)
        f.close()
