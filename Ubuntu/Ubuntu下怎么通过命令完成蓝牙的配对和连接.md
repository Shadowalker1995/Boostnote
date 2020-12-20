# Ubuntu下怎么通过命令完成蓝牙的配对和连接

1. 输入`hciconfig`命令, 确认你的蓝牙设备是否被系统识别, 避免你插入多个蓝牙设备

![image-20200708191531039](/home/zzhenry/Boostnote/Ubuntu/Ubuntu下怎么通过命令完成蓝牙的配对和连接.assets/image-20200708191531039.png)

2. 为你的蓝牙设备上电, 输入`hciconfig hci0 up`

    ![image-20200708191633454](/home/zzhenry/Boostnote/Ubuntu/Ubuntu下怎么通过命令完成蓝牙的配对和连接.assets/image-20200708191633454.png)

3. 输入`bluetoothctl`命令

    ![image-20200708191808821](/home/zzhenry/Boostnote/Ubuntu/Ubuntu下怎么通过命令完成蓝牙的配对和连接.assets/image-20200708191808821.png)

4. 启动搜索模式, 输入`scan on`

    ![image-20200708191851760](/home/zzhenry/Boostnote/Ubuntu/Ubuntu下怎么通过命令完成蓝牙的配对和连接.assets/image-20200708191851760.png)

5. 当找到你需要连接的蓝牙设备时, 输入`scan off`, 停止探索

6. 完成配对输入`pair ADDRESS`

    ![image-20200708191937312](/home/zzhenry/Boostnote/Ubuntu/Ubuntu下怎么通过命令完成蓝牙的配对和连接.assets/image-20200708191937312.png)

    ![image-20200708192020620](/home/zzhenry/Boostnote/Ubuntu/Ubuntu下怎么通过命令完成蓝牙的配对和连接.assets/image-20200708192020620.png)

7. 手机端需要确认配对请求, 之后ubuntu有如下打印说明配对成功

    ![20190507180902993.png](/home/zzhenry/Boostnote/Ubuntu/Ubuntu下怎么通过命令完成蓝牙的配对和连接.assets/20190507180902993.png)

8. Ubuntu输入`connect ADDRESS`

    ![20190507180909156.png](/home/zzhenry/Boostnote/Ubuntu/Ubuntu下怎么通过命令完成蓝牙的配对和连接.assets/20190507180909156.png)


如上说明你连接成功, finish