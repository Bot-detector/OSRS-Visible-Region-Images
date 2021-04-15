import os

# Download the files from explv's github here: https://github.com/Explv/osrs_map_tiles/tree/master/0/8
# This script works with zoom 8 which correlates 1:1 with Region ID. It has been linked above.
# Change png and regionRename to the location of the downloaded file.
# Run the script. 

def region_generate():
    start = 4627
    i = 0
    for x in range(0,49):
        start = 4627 + (x*256)
        for i in range(0,178):
            regionid = i+start
            png = "C:/Users/8/{0}/{1}.png".format(x,i)
            regionRename = "C:/Users/8/{0}/{1}.png".format(x,regionid)
            os.rename(png,regionRename)
    return
  
region_generate()
