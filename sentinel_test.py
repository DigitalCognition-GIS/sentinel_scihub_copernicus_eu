import sentinelsat

from sentinelsat.sentinel import SentinelAPI

s2_api = SentinelAPI(
    user="rohitdhankar",
    password="rohitdhankar",
    api_url="https://scihub.copernicus.eu/apihub/"
)

print(s2_api)

from sentinelsat import read_geojson, geojson_to_wkt
products = s2_api.query(
    area = geojson_to_wkt(read_geojson('map.geojson')),
    date = ("20151001", "20160201"),
    platformname = "Sentinel-2",
    cloudcoverpercentage="(0,10)"
)

print(type(products))