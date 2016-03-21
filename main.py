import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

cscan = np.zeros([30,60]);
for i in range(0,30):
    data = np.genfromtxt("bscan-"+str(i)+".csv", delimiter = ",");
    for j in range(0,60):
        cscan[i,j]=np.amax(data[i,:]);
        
np.savetxt("cscan.csv",cscan,delimiter = ",");