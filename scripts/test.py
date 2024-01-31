import pickle
import numpy as np

pipe = pickle.load(open('models\\pipe_main.pkl','rb'))
# pipe = pickle.load(open('pipe.pkl','rb')) #test Model

query = np.array(['Apple',15.6,'intel core i7',32,'Nvidia High gamma','MacOs',2000], dtype=object)
# query = np.array(['Lenovo','Gaming',16,32,'Windows',2.50,1,0,141,'Intel Core i7',256,1000,'Nvidia'], dtype=object) # Test Model
query = query.reshape(1,7)

print(int(np.exp(pipe.predict(query)[0])))