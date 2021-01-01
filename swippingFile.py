import os
import shutil

source="/users/v0788/Desktop/Python/Functions/data1.txt"
destination="/users/v0788/Desktop/Python/Functions/data2.txt"
dest=shutil.copy(source,destination)
source1="/users/v0788/Desktop/Python/Functions/data2.txt"
destination1="/users/v0788/Desktop/Python/Functions/data1.txt"
dest1=shutil.copy(source1,destination1)
