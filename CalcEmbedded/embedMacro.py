#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
def embedMacro():
    import glob
    filenames = glob.glob("*.ods")
    if filenames:
        import zipfile
        with zipfile.ZipFile(filenames[0]) as zipf:
            with zipf.open("META-INF/manifest.xml") as manif:
                import xml.etree.ElementTree as ET
                tree = ET.parse(manif)
                root = tree.getroot()
                
                
                
                
                
#                 for child in root:
#                     print(child.tag, child.attrib)

    
    
    
    
    
#     odsfile = zipfile.ZipFile(ods_filenames[0])
#     
#     
#     
#     
#     listoffiles = odsfile.infolist()
#     for s in listoffiles:
#         if s.orig_filename == "META-INF/manifest.xml":
#             bh = odsfile.read(s.orig_filename)
#             print(bh)
    
    
    
    
#     print(myfile.infolist())
#     print(myfile.namelist())
    
    
    
    
#     with open(ods_filenames[0]) as f:
#         import gzip
#         zip = gzip.GzipFile(f)
#         manifest_content = zip.read("META-INF/manifest.xml")
#         print(manifest_content)
    
    
    
    
#     print(ods[0])
#     import gzip
#     with gzip.open(ods_filename[0],"rb") as f:
#         file_content = f.read()



#     with open(ods_filename[0]) as f:
#         import zipfile
#         zip = zipfile.ZipFile(f)
#         manifest_content = zip.read("META-INF/manifest.xml")
#         print(manifest_content)




#     import zipfile
#     with zipfile.ZipFile(ods, 'r') as myzip:
#         print(myzip.infolist())

    
    
    
    
if __name__ == "__main__":
    import sys
    sys.exit(embedMacro())