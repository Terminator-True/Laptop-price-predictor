import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))

query = np.array(['Lenovo','Gaming',16,32,'Windows',2.50,1,0,141,'Intel Core i7',256,1000,'Nvidia'], dtype=object)
query = query.reshape(1,13)

print(int(np.exp(pipe.predict(query)[0])))