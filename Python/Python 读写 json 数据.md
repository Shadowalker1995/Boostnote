# Python 读写 json 数据

JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式，简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

使用 JSON 函数需要导入 json 库：`import json`。

```python
json.dumps  # 将 Python 对象编码成 JSON 字符串
json.loads  # 将已编码的 JSON 字符串解码为 Python 对象
```

## json.dumps

json.dumps 用于将 Python 对象编码成 JSON 字符串。

### 语法

```python
json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
```

### 实例

以下实例将数组编码为 JSON 格式数据：

```python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print(json)
```

以上代码执行结果为：

```python
[{"e": 5, "d": 4, "a": 1, "c": 3, "b": 2}]
```

### 使用参数让 JSON 数据格式化输出：

```python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

# 打开键值排序、缩进为4、以',', ': '为分隔
json = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print(json)
```

以上代码执行结果为：

```python
[
    {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5
    }
]
```

## json.loads

json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

### 语法

```python
json.loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```

### 实例

以下实例展示了Python 如何解码 JSON 对象：

```python
import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print(text)
```

以上代码执行结果为：

```python
{'a': 1, 'e': 5, 'd': 4, 'b': 2, 'c': 3}
```