# Shapefile Extension Types

Shapefiles are a simple, nontopological format for storing the geometric location and attribute information of geographic features. A shapefile is one of the spatial data formats that you can work with and edit in ArcGIS.

The shapefile format defines the geometry and attributes of geographically referenced features in three or more files with specific file extensions that should be stored in the same project workspace. They are:

- shp: The main file that stores the feature geometry; required.

- shx: The index file that stores the index of the feature geometry; required.

- dbf: The dBASE table that stores the attribute information of features; required. There is a one-to-one relationship between geometry and attributes, which is based on record number. Attribute records in the dBASE file must be in the same order as records in the main file.

- sbn and .sbx: The files that store the spatial index of the features.

- fbn and .fbx: The files that store the spatial index of the features for shapefiles that are read-only.

- ain and .aih: The files that store the attribute index of the active fields in a table or a theme's attribute table.

- atx: An .atx file is created for each shapefile or dBASE attribute index created in ArcCatalog. ArcView GIS 3.x attribute indexes for shapefiles and dBASE files are not used by ArcGIS. A new attribute indexing model has been developed for shapefiles and dBASE files.

- ixs: Geocoding index for read/write shapefiles.

- mxs: Geocoding index for read/write shapefiles (ODB format).

- prj: The file that stores the coordinate system information; used by ArcGIS.

- xml: Metadata for ArcGIS—stores information about the shapefile.

- cpg: An optional file that can be used to specify the codepage for identifying the characterset to be used.

Each file must have the same prefix, for example, roads.shp, roads.shx, and roads.dbf.
