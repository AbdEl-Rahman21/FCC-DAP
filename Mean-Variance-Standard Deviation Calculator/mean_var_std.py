import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    data = np.array(list).reshape(3, 3)
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    calculations['mean'].append(data.mean(axis=0).tolist())
    calculations['mean'].append(data.mean(axis=1).tolist())
    calculations['mean'].append(data.mean().tolist())

    calculations['variance'].append(data.var(axis=0).tolist())
    calculations['variance'].append(data.var(axis=1).tolist())
    calculations['variance'].append(data.var().tolist())

    calculations['standard deviation'].append(data.std(axis=0).tolist())
    calculations['standard deviation'].append(data.std(axis=1).tolist())
    calculations['standard deviation'].append(data.std().tolist())

    calculations['max'].append(data.max(axis=0).tolist())
    calculations['max'].append(data.max(axis=1).tolist())
    calculations['max'].append(data.max().tolist())

    calculations['min'].append(data.min(axis=0).tolist())
    calculations['min'].append(data.min(axis=1).tolist())
    calculations['min'].append(data.min().tolist())

    calculations['sum'].append(data.sum(axis=0).tolist())
    calculations['sum'].append(data.sum(axis=1).tolist())
    calculations['sum'].append(data.sum().tolist())

    return calculations
