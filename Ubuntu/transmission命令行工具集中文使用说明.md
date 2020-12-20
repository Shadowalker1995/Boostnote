# transmission命令行工具集中文使用说明

> 转载: [transmission命令行工具集中文使用说明]([http://xdsnet.github.io/index.html?name=%E6%9D%82%E8%B0%88:transmission%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7%E9%9B%86%E4%B8%AD%E6%96%87%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E](http://xdsnet.github.io/index.html?name=杂谈:transmission命令行工具集中文使用说明))

[transmission](http://www.transmissionbt.com/)作为一个优秀的BT下载工具, 支持普通BT和PT广受用户喜爱。近日根据需要调整PT种子的属性, 所以稍微研究了下transmission的命令行工具, 并根据man文档简要翻译出了本份说明。

transmission的命令行工具主要有:

- `transmission-create`: 创建种子文件(`.torrent`格式文件)的工具
- `transmission-show`: 显示种子metadata信息的工具
- `transmission-edit`: 编辑种子信息的工具
- `transmission-cli`: 一个命令行的bt客户端工具
- `transmission-daemon`: bt下载客户端服务工具
- `transmission-remote`: 远程控制transmission-daemon的工具

## transmission-create——创建种子的工具

### 命令行语法

```shell
transmission-create [-h]
transmission-create -V
transmission-create [-p] [-o file] [-c comment] [-t tracker] <source file or directory>
```

### 选项参数说明

- `-h, --help`: 显示一个帮助后退出
- `-p, --private`: 包含私人追踪信息(private trackers)的bt种子标志, 即pt种子
- `-c, --comment`: 为种子文件添加一个说明
    - `comment`: 一段字符串, 是需要添加的说明内容
- `-t, --tracker`: 为种子添加追踪用的网址, 大多数种子至少需要一个追踪用的网址（通常是发布地址）。要添加不止一个, 可以多次使用这个选项
    - `tracker`: 一段URI字符串, 是需要添加的追踪用网址
- `source file or directory`: 要提供下载的源文件或者目录
- `-o`: 种子输出到文件,如果没有 `-o` 选项, 将输出到标准输出设备, 可以用来测试
    - `file`: 种子文件路径
- `-V, --version`: 显示版本信息后退出

### 例子

```shell
transmission-create -p -o /tmp/test.torrent -c "a test BitToorent seed file" -t http://www.test1.me/ -t http://www.testbt.me/ test.txt
```

## transmission-show——显示种子元数据

### 命令行语法

```shell
transmission-show [-h] 
transmission-show -V
transmission-show [-m] [-s] <torrent-file(s)>
```

### 选项参数说明

- `-h, --help`: 显示一个帮助后退出
- `-m, --magnet`: 指定的`magnet`链接格式显示种子信息
- `-s, --scrape`: 向种子的信息追踪网址请求当前有多少连接(显示做种和下载数)
- `torrent-file(s)`: bt种子文件路径(可以是相对或者绝对路径, 支持通配符)
- `-V, --version`: 显示版本信息后退出

### 例子

显示`test.torrent`的`magnet`链接

```shell
transmission-show  -m test.torrent
```

一个`magnet`链接形如:

```shell
magnet:?xt=urn:btih:<种子文件HASH值>&dn=<种子种的文件名>&tr=<追踪地址信息>
```

```shell
transmission-show -c test.torrent
```

将显示如下类型的信息：

```shell
Name: <文件名>
File: test.torrent

<追踪地址> ... <XXs> seeders, <XXl> leechers
```

其中`<XXs>`和`<XXl>`是数字值, 分别表示做种数和下载数。

## transmission-edit——编辑种子信息的工具

### 命令行语法

```shell
transmission-edit [-h] 
transmission-edit -V 
transmission-edit [选项和参数] torrent-file(s)
```

### 选项参数说明

- `-h, --help`: 显示一个帮助后退出
- `-a, --add <url>`: 添加`<url>`作为追踪地址
- `-d, --delete <url>`: 删除`<url>`追踪地址
- `-r, --replace <oldurl> <newurl>`: 在追踪地址（列表）中用`<newurl>`替换`<oldurl>`
- `torrent-file(s)`: bt种子文件路径(可以是相对或者绝对路径, 支持通配符)
- `-V, --version`: 显示版本信息后退出

### 例子

```shell
transmission-edit -a http://www.test.me/ abc.torrent
transmission-edit -a http://www.testbt.me/ abc.torrent
transmission-edit -d http://www.test.me/ abc.torrent
transmission-edit -r http://www.testbt.me/ http://www.test.me/ abc.torrent
```

通过上面的处理, `abc.torrent`中至少有一个追踪地址是`http://www.test.me/`

## transmission-cli——命令行的bt客户端工具

### 命令行语法

```shell
transmission-cli [-h] 
transmission-cli -V
transmission-cli [选项和参数]  <file|url|magnet>
```

### 选项参数说明

- `-h, --help`: 显示一个帮助后退出
- `-b, --blocklist`: 允许黑名单
- `-B, --no-blocklist`: 禁止黑名单
- `-d, --downlimit <speed>`: 指定最大下载速度为`<speed>`, 单位 kb/s
- `-D, --no-downlimit`: 不限速
- `-er, --encryption-required`: 加密所有peer连接
- `-ep, --encryption-preferred`: 倾向加密对等连接
- `-et, --encryption-tolerated`: 倾向非加密对等连接
- `-f, --finish <script>`: 在下载完成后运行脚本, 脚本由`<script>`指定
- `-g, --config-dir <path>`: 在`<path>`指定的目录下加载配置文件
- `-m, --portmap`: 允许通过NAT-PMP 或者 UPnP的端口映射
- `-M, --no-portmap`: 禁止端口映射
- `-p, --port <port>`: 指定`<port>`作为对等连接的端口(默认: 51413)
- `-t, --tos <tos>`: 对等`socket`的`TOS` (0 to 255,default=default)
- `-u, --uplimit <speed>`: 设置 `<speed>`为最大上传速度, 单位kB/s
- `-U, --no-uplimit`: 不限制上传速度
- `-v, --verify`: 校验指定的种子（检查当前已经下载的情况）
- `-V, --version`: 显示版本信息后退出
- `-w, --download-dir <path>`: 下载数据保存目录（可能是临时保存）
- `<file|url|magnet>`: 
    - `file`: 种子文件路径
    - `url`: 种子URL链接
    - `magnet`: magnet格式链接

### 例子

将以当前目录为保存路径下载 `abc.torrent`

```shell
transmission-cli abc.torrent
```

将以当前目录为保存路径检验下载`abc.torrent`的情况

```shell
transmission-cli -v abc.torrent
```

将从`/home/me/.config/transmission`加载配置文件后下载`abc.torrent`。 配置文件的介绍见https://github.com/transmission/transmission/wiki/Configuration-Files

```shell
transmission-cli -g /home/me/.config/transmission abc.torrent
```

## transmission-daemon——bt下载客户端服务工具

### 命令行语法

```shell
transmission-daemon [-h] 
transmission-daemon -V 
transmission-daemon [选项和参数]
```

### 选项参数说明

- `-h, --help`: 显示一个帮助后退出
- `-a, --allowed <list>`: 允许连接（来控制）的IP地址为`<list>`指定的列表地址(默认:127.0.0.1, 即只允许本地连接来控制)
- `-b, --blocklist`: 允许黑名单
- `-B, --no-blocklist`: 禁止黑名单
- `-c, --watch-dir <directory>`: 设置目录监控路径为`<directory>`, 其中的`.torrent`文件将自动下载
- `-C, --no-watch-dir`: 禁止目录监控
- `--incomplete-dir <directory>`: 用于存储未完成的种子, 直到完成
- `--no-incomplete-dir`: 不保存未完成的种子到不同的位置
- `-d, --dump-settings`: 显示设置后退出
- `-e, --logfile <filename>`: 输出日志消息到文件`<filename>`
- `-f, --foreground`: 设置为在前台运行（一般用于调试测试）
- `-g, --config-dir <path>`: 设置配置文件搜索路径为 `<path>`
- `-p, --port <port>`: 设置RPC端口地址为 `<port>` (默认: 9091)
- `-t, --auth`: 要求认证
- `-T, --no-auth`: 不要求认证
- `-u, --username <username>`: 设置认证用户名为`<username>`
- `-v, --password <password>`: 设置认证用户密码为`<password>`
- `-V, --version`: 显示版本信息后退出
- `--log-error`: 显示错误消息
- `--log-info`: 显示错误和信息消息
- `--log-debug`: 显示错误, 信息和调试消息
- `-w, --download-dir <path>`: 设置 `<path>`指定的目录为数据下载目录
- `--paused`: 在启动时暂停所有的下载
- `-o, --dht`: 允许分布式hash表(distributed hash tables——DHT)
- `-O, --no-dht`: 禁止分布式hash表
- `-y, --lpd`: 允许本地对等发现(local peer discovery-LPD)
- `-Y, --no-lpd`: 禁止本地对等发现
- `--utp`: 允许 uTP的对等连接
- `--no-utp`: 禁止uTP的对等连接
- `-P, --peerport <port>`: 设置对等连接入口端口为`<port>` (默认: 51413)
- `-m, --portmap`: 允许通过NAT-PMP 或者 UPnP的端口映射
- `-M, --no-portmap`: 禁止端口映射
- `-L, --peerlimit-global <limit>`: 设置最大的对等连接数为`<limit>` (默认: 200)
- `-l, --peerlimit-torre <limit>`: 设置每个种子中最大的对等连接数为`<limit>` (默认: 50)
- `-er, --encryption-required`: 加密所有的对等连接
- `-ep, --encryption-preferred`: 倾向加密对等连接
- `-et, --encryption-tolerated`: 倾向非加密对等连接
- `-i, --bind-address-ipv4 <ipv4 addr>`: 对等连接绑定IPV4地址为`<ipv4 addr>`
- `-I, --bind-address-ipv6 <ipv6 addr>`: 对等连接绑定IPV6地址为`<ipv6 addr>`
- `-r, --rpc-bind-address <ipv4 addr>`: RPC连接监听IPV4地址为`<ipv4 addr>`
- `-gsr, --global-seedratio ratio`: 所有的种子, 除非预先设置了, 否则持续做种到完成`ratio`指定的全局分享率
- `-GSR, --no-global-seedratio`: 所有的种子, 除非预先设置, 否则不分配全局分享率
- `-x, --pid-file <pid-file>`: 允许PID文件, 并设置PID文件路径为`<pid-file>`

### 例子

从`/etc/transmission`来启动服务, 配置文件的介绍见https://github.com/transmission/transmission/wiki/Configuration-Files

```shell
transmission-daemon -g /etc/transmission
```

将pid信息保存到`/var/run/transmission-daemon.pid`来启动服务, 切启动时暂停所有下载

```shell
transmission-daemon -x /var/run/transmission-daemon.pid --paused
```

## transmission-remote——远程控制transmission-daemon的工具

### 命令行语法

```shell
transmission-remote [-h]
transmission-remote -V
transmission-remote [host] [options]
transmission-remote [port] [options]
transmission-remote [host:port] [options]
transmission-remote [http(s?)://host:port/transmission/] [options]
```

### 选项参数说明

- `host`: transmission-daemon主机地址, 默认为`localhost`

- `port`: transmission-daemon的rpc监听端口, 默认为9091, 如果不专门指定, 则默认通过http来访问。
- `-h, --help`: 显示一个帮助后退出
- `-a , --add <filepath|URL>`: 通过文件路径或者URL添加一个种子来下载
- `-as, --alt-speed`: 使用替代的限制
- `-AS, --no-alt-speed`: 不使用替代的限制
- `-asd --alt-speed-downlimit <speed>`: 设置替代的最大下载速度为 `<speed>`, 单位kB/s
- `-asu --alt-speed-uplimit <speed>`: 设置替代的最大上传速度为 `<speed>`, 单位kB/s
- `-asc --alt-speed-scheduler`: 使用预定开关时间
- `-ASC --no-alt-speed-scheduler`: 不使用预定开关时间
- `--alt-speed-time-begin <time>`: 设置使用替代限速的开始时间为`<time>` , 时间格式为hhmm
- `--alt-speed-time-end <time>`: 设置使用替代限速的结束时间为`<time>` , 时间格式为hhmm
- `--alt-speed-days <days>`: 设置采用替代限速的每周日期, 例如 "1-7"表示每天
- `--blocklist-update`: 更新黑名单
- `-c , --incomplete-dir <dir>`: 设置新种子存储目录为`<dir>`, 直到下载完成
- `-C , --no-incomplete-dir`: 不把未完成的种子存放到不同目录
- `-b , --debug`: 打印调试信息
- `-d , --downlimit <speed>`: 设置当前种子或者全局的最大下载速度为 `<speed>`, 单位kb/s
- `-D , --no-downlimit`: 禁止最大下载速度
- `-e , --cache <size>`: 设置每个session的最大内存缓冲为`<size>`, 单位kb/s
- `-er, --encryption-required`: 加密所有对等连接
- `-ep, --encryption-preferred`: 倾向加密的对等连接
- `-et, --encryption-tolerated`: 倾向非加密的对等连接
- `--exit`: 通知 transmission session 要下线
- `-f , --files`: 列出当前的种子
- `-g , --get <files>`: 标记`<files>`文件来下载
- `-G , --no-get <files>`: 标记`<files>`文件不下载
- `-i , --info`: 显示当前种子的详细信息（指定的种子）
- `-if, --info-files`: 列出当前种子文件
- `-ip, --info-peers`: 列出当前种子的对等连接信息
- `-ic, --info-pieces`: 列出当前种子的内容
- `-it, --info-trackers`: 列出当前种子的追踪信息
- `-si, --session-info`: 显示session的详细信息
- `-st, --session-stats`: 显示session的统计信息
- `-l , --list`: 列出所有的种子
- `--move <path>`: 把当前种子的数据移动到新目录`<path>`下
- `--find <path>`: 通知Transmission在`<path>`查找种子的数据
- `-m , --portmap`: 允许通过NAT-PMP或者UPnP的端口映射
- `-M , --no-portmap`: 禁止端口映射
- `-n , --auth <user:pw>`: 设置认证的用户名和密码, 需要`user:pw`格式
- `-ne, --authenv`: 设置从环境变量`TR_AUTH`中获取认证信息值的格式为`user:pw`
- `-N , --netrc <file>`: 设置从`.netrc`格式文件 `<file>` 中读取认证信息
- `--ssl`: 使用SSL来访问daemon
- `-o , --dht`: 允许分布式hash表(distributed hash tables——DHT)
- `-O , --no-dht`: 禁止分布式hash表
- `-p , --port <port>`: 设置对等连接入口端口为`<port>` (默认: 51413)
- `-pt, --port-test`: 端口测试
- `-P , --random-port`: 随机端口作为对等入口端口
- `-ph, --priority-high <files>`: 尝试先下载 `<files>`等文件
- `-pn, --priority-normal <files>`: 尝试按一般优先级下载`<files>`
- `-pl, --priority-low <files>`: 尝试最后下载`<files>`
- `-Bh, --bandwidth-high`: 为这个流(种子的下载)设置最可用的带宽（最大带宽）
- `-Bn, --bandwidth-normal`: 让高优先级下载保留带宽（继续下载）
- `-Bl, --bandwidth-low`: 让高优先级或者普通优先级的下载保留带宽（继续下载）
- `--reannounce`: 恢复当前下载（可能是多个）
- `-r , --remove`: 移除当前下载（可能是多个）（仅仅删除种子等下载信息, 已下载的数据不删除）
- `-pr, --peers <max>`: 设置当前下载的最大对等连接数为`<max>`
- `--remove-and-delete`: 移除当前下载, 并且删除本地数据
- `--torrent-done-script <file>`: 指定在完成下载后执行 `<file>`脚本
- `--no-torrent-done-script`: 设置在下载完成后不执行脚本
- `-sr, --seedratio ratio`: 设置当前下载种子的最低分享率为`ratio` （即一直做种直到分享率达到要求）
- `-srd --seedratio-default`: 让当前下载采用全局分享率要求
- `-SR, --no-seedratio`: 设置当前下载不采用全局分享率要求
- `-gsr --global-seedratio ratio`: 除非预设, 否则做种到满足全局分享率要求`ratio`
- `-GSR --no-global-seedratio`: 除非预设, 否则禁用全局分享率要求
- `-td, --tracker-add <tracker>`: 为一个下载添加追踪地址`<tracker>`
- `-tr, --tracker-remove <trackerId>`: 从bt下载中移除`<trackerId>`号的追踪
- `-s , --start`: 开始当前选中的下载
- `-S , --stop`: 停止当前选中的下载
- `-t , --torrent <torrent>`: 设置当前的下载任务。
- `--start-paused`: 添加的下载默认先暂停
- `--no-start-paused`: 添加的种子后先暂停
- `--trash-torrent`: 在添加种子后删除(在种子位置删除)
- `--no-trash-torrent`: 添加种子后不删除文件
- `-hl, --honor-session`: 设置当前下载回话准守限制属性
- `-HL, --no-honor-session`: 设置当前下载回话不准守限制属性
- `-u , --uplimit <speed>`: 设置当前或者全局的最大上传速度为`<speed>` , 单位KB/s
- `-U , --no-uplimit`: 显示当前或者全局的最大上传速度, 单位KB/s
- `--utp`: 允许uTP的对等连接
- `--no-utp`: 禁止uTP的对等连接
- `-v , --verify`: 验证当前下载
- `-V, --version`: 显示版本信息后退出
- `-w , --download-dir <path>`: 与`--add`一起使用时为设置新下载的数据保存路径为`<path>`, 否则为设置默认下载路径
- `-x , --pex`: 允许对等扩展(Enable peer exchange——PEX)
- `-X , --no-pex`: 禁止对等扩展
- `-y , --lpd`: 允许本地对等发现(local peer discovery——LPD)
- `-Y , --no-lpd`: 禁止本地对等发现
- `-pi, --peer-info`: 列出当前下载的对等连接信息

### 例子

```shell
transmission-remote http://localhost:9091/transmission -n user:password  -u 1000
```

设置本地的transmission-daemon上传限速为1000KB/s

