# MATLAB exist判断文件夹是否存在并建立文件夹 isfield判断struct isempty判断矩阵

### 1. exist判断当前目录是否存在指定文件夹

- **example 1**

    ```matlab
    if ~exist('Directtory', 'dir')
        mkdir('Directory')			% if not exist, make dir 'Directory' in current directory
    end
    ```

- **example2**

    判断并建立多层目录

    ```matlab
    if ~exist('./fig/Figure', 'dir')
    	mkdir('./fig/Figure')		% if not exist, make a series dirs in current directory
    end
    ```

### 2. exist 还可以用于判断目录、内置函数（buildin）、文件、class和变量(var)是否存在

**Syntax**

`exist name`

`exist name kind`

`A = exist('name','kind')`

kind包括：

1. **builtin**	Checks only for built-in functions.
2. **class**	Checks only for classes.
3. **dir**		Checks only for directories.
4. **file**		Checks only for files or directories.
5. **var**		Checks only for variables.

注意这里的var不能用于struct内的子field判定，field可参考下一段

### 3. isfield判断struct是否有指定子filed

```matlab
% 定义一个struct
>> patient.name = 'John Doe';
>> patient.billing = 127.00;
>> patient.test = [79 75 73; 180 178 177.5; 220 210 205];
% 检测该struct是否存在指定filed
>> isfield(patient,'billing')

ans = 1
```

### 4. isempty用于判断矩阵是否为空

```matlab
>> B = rand(2,2,2);
>> B(:,:,:) = [];         % B此时为零矩阵
>> isempty(B)

ans = 1
```