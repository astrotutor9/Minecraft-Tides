from mcpi import minecraft
from mcpi import block
import requests

# Get the unix epoch time from https://www.epochconverter.com/
# Place it in the time = XXXX below.

time = 1566572574

# Find the latitude and longitude of a location.
# Default values are for Newquay.

lat = 50.4
lon = -5.0

# Get the latest tide height from closest location near yours
# response = requests.get("https://www.worldtides.info/api?heights&lat&lon=&start=time&length=1&key=c51a887d-2c77-4437-8fcc-b189da284a7d")
response = requests.get("https://www.worldtides.info/api?heights&lat&lon&start=1566579774&length=1&key=c51a887d-2c77-4437-8fcc-b189da284a7d")
data = response.json()

print(response)
print(data)

tide_height = (data["heights"][0]['height'])

# The +3 brings tide levels equal to minecraft level
# Minecraft level is treated as Lowest Low Water so a High Tide
# will be about 6 blocks deep of water.

minecraftTide = (int(round((tide_height*10), 0))) + 3 

print(minecraftTide)
"""
# Make link into Minecraft
mc=minecraft.Minecraft.create()

mc.postToChat("Tide was out.")
mc.postToChat("Let's see how far in it is")

# Find player position and alter water levels 60 blocks around them

x,y,z = mc.player.getTilePos()

for goingOut in range(1, minecraftTide+1, 1):
    for xEdge in range(x-30, x+30):
        for zEdge in range(z-30, z+30):
            airOrNot = mc.getBlock(xEdge, goingOut, zEdge) # is there air? 
            print(xEdge, goingOut, zEdge, airOrNot) # Just to show something happening
            if airOrNot == 0:
                mc.setBlock(xEdge, goingOut, zEdge, 8) # if air place water
"""