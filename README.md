### This file has ROUGH NOTES , steps i followed , errors logs etc .( REFER with a pinch of salt)  


<p align="center">
    <img src="https://github.com/DigitalCognition-GIS/sentinel_scihub_copernicus_eu/blob/master/Screen_captures/Sentinel_Screenshot%20from%202020-07-12%2011-56-48.png" width= "850px">
</p>

<h1 align="center">SENTINEL Experiments - </h1>

> This repository will contain both code and additional reading material refrences for analytics and pseudo-projects done with the Sentinel Data **- Sentinel 2020**
 
> If you are a GIS developer or a GeoSpatial Scientist - kindly feel free to contribute. 


<br/>


### Table of Contents of this repository

- [X] `A-- Intro to Sentinel...` 
- [X] `B-- Download and Preprocess Sentinel Data` 
- [X] `C-- Further explorations with Sentinel Data` 
- [X] `D-- Work in Progress` 
- [X] `Work in Progress` 
- [X] `Work in Progress` 
- [X] `Work in Progress` 


<br/>

### References - Always an ongoing effort - Work in Progress

### sentinel_scihub_copernicus_eu
Intial experiments with data from - sentinel_scihub_copernicus_eu

<br/>


- Source URL - the ```manifest.safe``` file 

> The Sentinel Data has ZIP file , once the ZIP files is uncompressed the TREE structure is as seen below --   

<br/>


```
/Sentinel_data/S2A_MSIL1C_20160129T054102_N0201_R005_T43RFM_20160129T054903.SAFE$ tree

.
├── AUX_DATA
├── DATASTRIP
│   └── DS_MTI__20160129T092949_S20160129T054903
│       ├── MTD_DS.xml
│       └── QI_DATA
├── GRANULE
│   └── L1C_T43RFM_A003148_20160129T054903
│       ├── AUX_DATA
│       │   └── AUX_ECMWFT
│       ├── IMG_DATA
│       │   ├── T43RFM_20160129T054102_B01.jp2
│       │   ├── T43RFM_20160129T054102_B02.jp2
│       │   ├── T43RFM_20160129T054102_B03.jp2
│       │   ├── T43RFM_20160129T054102_B04.jp2
│       │   ├── T43RFM_20160129T054102_B05.jp2
│       │   ├── T43RFM_20160129T054102_B06.jp2
│       │   ├── T43RFM_20160129T054102_B07.jp2
│       │   ├── T43RFM_20160129T054102_B08.jp2
│       │   ├── T43RFM_20160129T054102_B09.jp2
│       │   ├── T43RFM_20160129T054102_B10.jp2
│       │   ├── T43RFM_20160129T054102_B11.jp2
│       │   ├── T43RFM_20160129T054102_B12.jp2
│       │   ├── T43RFM_20160129T054102_B8A.jp2
│       │   └── T43RFM_20160129T054102_TCI.jp2
│       ├── MTD_TL.xml
│       └── QI_DATA
│           ├── MSK_CLOUDS_B00.gml
│           ├── MSK_DEFECT_B01.gml
│           ├── MSK_DEFECT_B02.gml
│           ├── MSK_DEFECT_B03.gml
│           ├── MSK_DEFECT_B04.gml
│           ├── MSK_DEFECT_B05.gml
│           ├── MSK_DEFECT_B06.gml
│           ├── MSK_DEFECT_B07.gml
│           ├── MSK_DEFECT_B08.gml
│           ├── MSK_DEFECT_B09.gml
│           ├── MSK_DEFECT_B10.gml
│           ├── MSK_DEFECT_B11.gml
│           ├── MSK_DEFECT_B12.gml
│           ├── MSK_DEFECT_B8A.gml
│           ├── MSK_DETFOO_B01.gml
│           ├── MSK_DETFOO_B02.gml
│           ├── MSK_DETFOO_B03.gml
│           ├── MSK_DETFOO_B04.gml
│           ├── MSK_DETFOO_B05.gml
│           ├── MSK_DETFOO_B06.gml
│           ├── MSK_DETFOO_B07.gml
│           ├── MSK_DETFOO_B08.gml
│           ├── MSK_DETFOO_B09.gml
│           ├── MSK_DETFOO_B10.gml
│           ├── MSK_DETFOO_B11.gml
│           ├── MSK_DETFOO_B12.gml
│           ├── MSK_DETFOO_B8A.gml
│           ├── MSK_NODATA_B01.gml
│           ├── MSK_NODATA_B02.gml
│           ├── MSK_NODATA_B03.gml
│           ├── MSK_NODATA_B04.gml
│           ├── MSK_NODATA_B05.gml
│           ├── MSK_NODATA_B06.gml
│           ├── MSK_NODATA_B07.gml
│           ├── MSK_NODATA_B08.gml
│           ├── MSK_NODATA_B09.gml
│           ├── MSK_NODATA_B10.gml
│           ├── MSK_NODATA_B11.gml
│           ├── MSK_NODATA_B12.gml
│           ├── MSK_NODATA_B8A.gml
│           ├── MSK_SATURA_B01.gml
│           ├── MSK_SATURA_B02.gml
│           ├── MSK_SATURA_B03.gml
│           ├── MSK_SATURA_B04.gml
│           ├── MSK_SATURA_B05.gml
│           ├── MSK_SATURA_B06.gml
│           ├── MSK_SATURA_B07.gml
│           ├── MSK_SATURA_B08.gml
│           ├── MSK_SATURA_B09.gml
│           ├── MSK_SATURA_B10.gml
│           ├── MSK_SATURA_B11.gml
│           ├── MSK_SATURA_B12.gml
│           ├── MSK_SATURA_B8A.gml
│           ├── MSK_TECQUA_B01.gml
│           ├── MSK_TECQUA_B02.gml
│           ├── MSK_TECQUA_B03.gml
│           ├── MSK_TECQUA_B04.gml
│           ├── MSK_TECQUA_B05.gml
│           ├── MSK_TECQUA_B06.gml
│           ├── MSK_TECQUA_B07.gml
│           ├── MSK_TECQUA_B08.gml
│           ├── MSK_TECQUA_B09.gml
│           ├── MSK_TECQUA_B10.gml
│           ├── MSK_TECQUA_B11.gml
│           ├── MSK_TECQUA_B12.gml
│           ├── MSK_TECQUA_B8A.gml
│           └── T43RFM_20160129T054102_PVI.jp2
├── HTML
│   ├── banner_1.png
│   ├── banner_2.png
│   ├── banner_3.png
│   ├── star_bg.jpg
│   ├── UserProduct_index.html
│   └── UserProduct_index.xsl
├── INSPIRE.xml
├── manifest.safe
├── MTD_MSIL1C.xml
└── rep_info
    └── S2_User_Product_Level-1C_Metadata.xsd

11 directories, 94 files
```



<br/>

- Source URL - https://gdal.org/drivers/vector/gml.html
- Source URL - Sentinel-2-msi Data-Formats  - https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/data-formats 

> The Sentinel Data has vector GML Files , these ```Geography Markup Language``` files are as listed within TREE structure of DIR = GRANULE > L1C_T43RFM_A003148_20160129T054903 > QI_DATA .    
The 'tagset' for this GML has Elements as listed below -    
- Within the outer Tagset - <eop:maskMembers><eop:maskMembers>
- Within Tagset <eop:MaskFeature></eop:MaskFeature> we have ``` <eop:MaskFeature gml:id="OPAQUE.3">```
- Also within the Tagset <eop></eop> we have -  <eop:maskType codeSpace="urn:gs2:S2PDGS:maskType">CIRRUS</eop:maskType>

<br/>

- Source - Further specifics read -- https://sentinel.esa.int/documents/247904/685211/Sentinel-2-Products-Specification-Document

<br/>


- Source URL - ..

> The Sentinel 



<br/>

Rohit Dhankar - https://www.linkedin.com/in/rohitdhankar/




