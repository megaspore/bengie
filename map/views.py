from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import json 
from django.http import JsonResponse
from .models import User, Jsons
import os
import math
from shapely.geometry import shape, Point, Polygon
from pyproj import Proj, transform


## Redirects you to the url with the map
def index(request):
    return render(request, "map/weathermap.html" )

def geofile(request):
    ## input variable, can be a local path or eventually populated by the backend
    input = "/home/chris/visual/bengie/weather/map/data/api_endpoint_OWM_temperature_20221010.json"
    ## Output variable, what populates the map currently
    output = "/home/chris/visual/bengie/weather/map/geodata/test.geojson"
    ## Hex variable is the output ran through pyEAC tesillation, currently not working dynamicly
    hex = "/home/chris/visual/bengie/weather/map/pyeac/hexmaps/testhex.geojson"
    
    ## if output already exists populate with output
    if os.path.exists(output) == True: 
        newgeojson=json.load(open(output, "r", encoding="utf-8")) 
         ## Pass variable geojson to url hoasting     
        return JsonResponse(newgeojson,safe=False)

    else:
        ## Load input
        input_file=json.load(open(input, "r", encoding="utf-8"))
        ## Geojson layout
        geojs={
            "type": "FeatureCollection",
            "features":[
                {
                        
                        "type":"Feature",
                        "geometry": {
                        "type":"Polygon",
                        ## Creat polygon from point
                        "coordinates":[[[d["lon"]+1, d["lat"]], [d["lon"], d["lat"]+1], [d["lon"]-1, d["lat"]], [d["lon"], d["lat"]-1]]],
                    },
                        "properties":d,
                ## Populate with inputfile data
                } for d in input_file 
            ]  
        }

        ## Create new geojson file 
        newgeojson=open(output, "w", encoding="utf-8")
        ## Load file with geo data 
        json.dump(geojs, newgeojson)
        # Save
        newgeojson.close()
        
        ## open
        newgeojson=json.load(open(output, "r", encoding="utf-8"))
        ## Pass variable geojson to url hoasting
        return JsonResponse(newgeojson,safe=False)


