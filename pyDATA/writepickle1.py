import pickle

file=open("writedata.py", "rb")
l=pickle.load(file)
file.close()
print(l)
#output=[10, 20, 30, 40]