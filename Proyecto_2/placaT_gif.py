import glob
from PIL import Image

frames=[]

for image in glob.glob(f"*.png"):
    frames.append(Image.open(image))
    
frame_one = frames[0]
frame_one.save("placa.gif", format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)
    

