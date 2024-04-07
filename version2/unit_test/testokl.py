import pickle
import torch
import numpy as np
import os
from version2.model_gen.TorchModelGenerator import TorchModel
file_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(file_path)
# with open(r'E:\GraphFuzz\version2\model_graph\model2_WS.pkl','rb') as f:
#     model=pickle.load(f)

print(model.__class__.__name__)
torch_model = TorchModel(model)
res=torch_model.compute_dag(d)
print(res[0].shape)