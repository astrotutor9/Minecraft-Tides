from mcpi import minecraft
from time import time
import requests

# Calculate the unix epoch time from Jan 1st 1070

time_now = str(time())

# Find the latitude and longitude location from Google.
# These values are for Newquay, Cornwall, UK.

latitude = str(50.4155)
longitude = str(-5.0737)

# Get the latest tide height from closest location near yours
# Next two lines of code are one line.
# Replace myKey with your long API key from worldtides.info

address = "https://www.worldtides.info/api?heights&lat=" + latitude + "&lon=" + longitude + "&" + "start=" + time_now + "&length=1&key=" + "myKey"

print(address)

# Get the latest tide height from closest location near yours

response = requests.get(address)
data = response.json()

print(data)

tide_height = (data["heights"][0]['height'])

# The +4 brings sets medium tide levels to Minecraft level
# Normal Minecraft level is treated as Lowest Low Water 
# So a High Tide will be about 8 blocks deep of water.

minecraftTide = (int(round((tide_height+4), 0))) 

print(minecraftTide)

# Make link into Minecraft

mc=minecraft.Minecraft.create()

mc.postToChat("Let's see how far in the tide is")

# Find player position and alter water levels 60 blocks around them

x,y,z = mc.player.getTilePos()

for goingOut in range(1, minecraftTide):
    for xEdge in range(x-30, x+30):
        for zEdge in range(z-30, z+30):
            airOrNot = mc.getBlock(xEdge, goingOut, zEdge) # is there air? 
            print(xEdge, goingOut, zEdge, airOrNot) # show check being made
            if airOrNot == 0:
                mc.setBlock(xEdge, goingOut, zEdge, 8) # if air place water
