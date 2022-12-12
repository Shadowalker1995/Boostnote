To get the parameter count of each layer like Keras, PyTorch has [model.named_paramters()](https://pytorch.org/docs/master/generated/torch.nn.Module.html#torch.nn.Module.named_parameters) that returns an iterator of both the parameter name and the parameter itself.

Here is an example:

```python
from prettytable import PrettyTable

def count_parameters(model):
    table = PrettyTable(["Modules", "Parameters"])
    total_params = 0
    for name, parameter in model.named_parameters():
        if not parameter.requires_grad: continue
        param = parameter.numel()
        table.add_row([name, param])
        total_params+=param
    print(table)
    print(f"Total Trainable Params: {total_params}")
    return total_params
    
count_parameters(net)
```

The output would look something like this:

```
+-------------------+------------+
|      Modules      | Parameters |
+-------------------+------------+
| embeddings.weight |   922866   |
|    conv1.weight   |  1048576   |
|     conv1.bias    |    1024    |
|     bn1.weight    |    1024    |
|      bn1.bias     |    1024    |
|    conv2.weight   |  2097152   |
|     conv2.bias    |    1024    |
|     bn2.weight    |    1024    |
|      bn2.bias     |    1024    |
|    conv3.weight   |  2097152   |
|     conv3.bias    |    1024    |
|     bn3.weight    |    1024    |
|      bn3.bias     |    1024    |
|    lin1.weight    |  50331648  |
|     lin1.bias     |    512     |
|    lin2.weight    |   265728   |
|     lin2.bias     |    519     |
+-------------------+------------+
Total Trainable Params: 56773369
```