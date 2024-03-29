# Makefile 详解

[toc]

## 变量定义

1. `$^`

    所有的依赖目标的集合。以空格分隔。如果在依赖目标中有多个重复的，那个这个变量会去除重复的依赖目标，只保留一份。

2. `$@`

    规则中的目标文件集。在模式规则中，如果有多个目标，那么，`"$@"`就是匹配于目标中模式定义的集合 

3. `$?`

    所有比目标新的依赖目标的集合。以空格分隔。

4. `$<`

    依赖目标中的第一个目标名字。如果依赖目标是以模式 (即`"%"`) 定义的，那么`"$<"`将是符合模式的一系列的文件集。注意，其是一个一个取出来的。

5. `$(@D)`

    表示`"$@"`的目录部分(不以斜杠作为结尾)，如果`"$@"`值是`"dir/foo.o"`，那么`"$(@D)"`就是`"dir"`，而如果`"$@"`中没有包含斜杠的话，其值就是`"."`(当前目录) 。

6. `$(@F)`

    表示`"$@"`的文件部分，如果`"$@"`值是`"dir/foo.o"`，那么`"$(@F)"`就是`"foo.o"`，`"$(@F)"`相当于函数`"$(notdir $@)"`

## 举例详解

有`main.c`, `test.c`, `test1.c`, `test2.c`四个源文件

- 例子1:

    ```makefile
    %.o: %.c
    	gcc -c $< -o $@
    ```

    把所以的c文件编译生成对应的o文件，`$<`代表每次取的c文件，`$@`代表每次c文件对应的目标文件

- 例子2:

    ```makefile
    main: main.o test.o test1.o test2.o
    	gcc -o $@ $^
    ```

    把所有的o文件编译生成可执行的main文件，`$^`代表所以的依赖文件集合 (main.o test.o test1.o test2.o)，`$@`代表目标文件 (main)

- 例子3:

    ```makefile
    lib: test.o test1.o test2.o
    	ar r lib $?
    ```

    把有更新的依赖文件重新打包到库lib中， 如果只有test1.o更新，则`$?`代表test1.o，如果test.o test1.o都有更新，则`$?`代表test.o test1.o的集合。

## 总结

- `$^`: 所有依赖目标的集合

- `$?`: 所有有更新的依赖目标集合

- `$<`: 依赖目标中的第一个目标，如果依赖以`%`模式定义，则是一个一个取出来的

- `$@`: 目标文件

- `$(@D)`: `$@`的目录部分

- `$(@F)`: `$@`的文件部分

## 记忆方法

```makefile
dst: source1.o source2.o source3.o source4.o  
	xx ......
```

- `$^`: 其中^表示水平的范围限定，包含所有的依赖文件集合 (source1.o source2.o source3.o source4.o)

- `$?`: 其中?表示哪些依赖文件有更新是未知的，有更新的依赖文件集合 (?)

- `$<`: 其中<表示从集合中取值，第一个依赖的文件 (source1.o)

- `$@`: 目标文件 (dst)