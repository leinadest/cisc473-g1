import torch

# Make this model compatible with CPU too
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
