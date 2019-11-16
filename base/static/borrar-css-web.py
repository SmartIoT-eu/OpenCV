import os
import sympy.sandbox
import glob
import sys

path= sys.path[0]+"\CACHE\css\*"

files = glob.glob(path)
for f in files:
    os.remove(f)
    print(f, "Eliminador del sistema")

print("Ya puedes trabajar y volver a correr el django ;)")

   