import torch
#加载的z就是tensor类型变量，可以直接给下游任务使用
z= torch.load("z.pt")
#这边写自己的下游任务
print(z)
