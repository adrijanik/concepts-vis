#!/usr/bin/env python
import numpy as np
import glob
import os.path
import json
from PIL import Image

data = None
with open("data/points.js") as f:
    data = f.read()[18:]

points = json.loads(data)

pc0 = [x['coords'][0] for x in points]
pc1 = [x['coords'][1] for x in points]

g0 = [x['gradient'][0] for x in points]
g1 = [x['gradient'][1] for x in points]
print("var min_g0 = {};".format(min(g0)))
print("var min_g1 = {};".format(min(g1)))
print("var max_g0 = {};".format(max(g0)))
print("var max_g1 = {};".format(max(g1)))



print("var min_x = {};".format(min(pc0)))
print("var max_x = {};".format(max(pc0)))
print("var min_y = {};".format(min(pc1)))
print("var max_y = {};".format(max(pc1)))




# simulate data for the background heatmap
error_heatmap = []
for x in np.linspace(min(pc0), max(pc0), 100):
    for y in np.linspace(min(pc0), max(pc1), 100):
        error_heatmap.append({
            "coords": [x, y],
            "iou": 0.7
        })

with open("data/heatmap.js", "w") as f:
    f.write("var hm_data = {}".format(json.dumps(error_heatmap)))
