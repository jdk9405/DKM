import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def kde(x, std = 0.1):
    # use a gaussian kernel to estimate density
    x = torch.from_numpy(x).to(device)
    scores = (-torch.cdist(x,x)**2/(2*std**2)).exp()
    density = scores.sum(dim=-1)
    return density
