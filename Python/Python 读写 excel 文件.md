# Python 读写 excel 文件

![image](assets/20170510185101899)

![image](assets/20170510185103615)

我们尝试添加总分列，并计算各个同学的总分成绩

`sheet.row_value` 函数直接获取某一行所有值，第二项是从第几个格子开始

![image](assets/20170510185105149)

```python
import xlrd

book = xlrd.open_workbook('demo.xlsx')

#sheets可以获取所有的表，返回一个sheet对象
book.sheets()
#另一种获取sheet的方法
sheet = book.sheet_by_index(0)
# 访问行数
sheet.nrows
# 访问列数
sheet.ncols
# 获取单元格内容
cell = sheet.cell(0, 0)
# 获取单元格类型,返回的是枚举值，1对应xlrd.XL_CELL_TEXT;2对应xlrd.XL_CELL_NUMBER
cell.ctype
# 获取单元格的内容（unicode）
cell.value
# 获取一行,返回一个列表，每一项都是一个sheet对象
sheet.row(1, 1)

# 同样，col类似
```

 

```python
# 添加单元格，这个添加操作需要引入xlwt
import xlwt
wbook = xlwt.Workbook()
wsheet =  wbook.add_sheet(‘sheet1’)
```

![image](assets/20170510185105693)

![image](assets/20170510185106665)



**代码实现**：

```python
#coding:utf8
import xlrd, xlwt

rbook = xlrd.open_workbook('demo.xlsx')

rsheet = rbook.sheet_by_index(0)
nc = rsheet.ncols
rsheet.put_cell(0, nc , xlrd.XL_CELL_TEXT, u'总分', None)

for row in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align:vertical center,horizontal center')

for r in range(rsheet.nrows):
    for c in range(rsheet.nols):
        wsheet.writes(r, c, rsheet.cell_value(r,c), style)
        
wbook.save('output.xlsx')
```