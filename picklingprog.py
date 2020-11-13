import pickle

# tarun={"Name":"Tarun","Age":19,"Address":"Bhongir"}
# file=open("tarun.pxl","ab")
# pickle.dump(tarun,file)
# file.close()

# file2=open("tarun.pxl","rb")
# files=pickle.load(file2)
# print(files)

prabhas={"Name":"Prabhas","Address":"CVRCOE"}
with open("prabhas.pxl","ab") as f:
    pickle.dump(prabhas,f)

with open("prabhas.pxl","rb") as f2:
    file=pickle.load(f2)
    print(file["Name"])