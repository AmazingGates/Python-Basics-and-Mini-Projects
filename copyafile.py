# Copy A File - In this section we will be going over the process of writing a file
import shutil

# In the shutil module, these are the 3 copy funtions we can use and will choose which one we pick according to need
# All 3 work exactly the same, the difference is that they copy different things
# copyfile() - Copies contentof a file
# copy() - copyfile() + permission node + destination can be a directory
# copy2() - copy() + copies metadata (file's creation and modification times)

# In this section we will be focussing on the copyfile()
shutil.copyfile("test.txt","copy.txt") # This is the function you use to copy a file. It takes 2 parameters, (src,dst)
