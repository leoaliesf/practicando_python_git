#from fastapi import FastAPI
import numpy as np

#app = FastAPI()

#@app.get('/')
def get_list():
    return [1,2,3,4,5]

#@app.get('/contact')
def get_list():
    return 'leonardo alies fuentes'

arr=np.array(['hola',3,4,7,1], dtype='float64')
print(np.sort(arr))



