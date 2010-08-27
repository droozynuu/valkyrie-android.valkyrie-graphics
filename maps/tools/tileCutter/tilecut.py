import popen2 
import sys,Image
import os
import tempfile
from random import random

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

imdir= "" #Linux
nice= ["nice"]

name = sys.argv[1]

tile_width=int(sys.argv[2])
tile_height=int(sys.argv[3])


print name+".png", 

tileYmax= Image.open(name+".png").size[1]/tile_height
tileXmax= Image.open(name+".png").size[0]/tile_width

mkdir("dest")
 

f = open("dest/"+name+".png.json","w");
f.write("{width:"+str(Image.open(name+".png").size[0])+",height:"+str(Image.open(name+".png").size[1])+"}")
f.close()

for y in range(tileYmax):
    for x in range(tileXmax):
        todo=["-crop",str(tile_width)+"x"+str(tile_height)+"+"+str(x*tile_width)+"+"+str(y*tile_height)+"!"]
        todo+=["-colors","63"]		
        popen2.popen2(nice+[r"convert"]+todo+[name+".png", "dest/"+name+","+str(x)+","+str(y)+".png"])
        os.wait()


