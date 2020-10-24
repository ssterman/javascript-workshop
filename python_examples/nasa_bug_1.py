import json 
import matplotlib.pyplot as pyplot
  
# Opening JSON file 
with open('asteroids.json') as json_file: 
    data = json.load(json_file) 
    # print("Type:", type(data))  # Print the type of data variable 
    # print(data['near_earth_objects']['2020-10-25'][0]) # Print the data format to see what it looks like

    # extract the data we want  
    miss_distances = []
    diameters = []
    for i in range(0, 20):
        asteroid = data['near_earth_objects']['2020-10-25'][i]
        asteroid_approach_data = asteroid['close_approach_data']
        asteroid_approach_data_element = asteroid_approach_data['0']
        miss_distance = asteroid_approach_data_element['miss_distance']['kilometers']
        miss_distances.append(miss_distance)
        diameter = asteroid['estimated_diameter']['kilometers']['estimated_diameter_max']
        diameters.append(diameter)


    # Use Matplotlib to visualize the data
    plot = pyplot.subplot(111)
    scatter = plot.scatter(miss_distances, diameters)
            # , s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=<deprecated parameter>, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)[
    
    plot.set_ylabel('diameter (km)')
    plot.set_xlabel('earth miss distance (km)')
    pyplot.show()