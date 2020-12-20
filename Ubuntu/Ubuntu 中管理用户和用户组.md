# Ubuntu 中管理用户和用户组

## 1. 添加一个用户组并指定id为1002

```sh

```

## 2. 添加一个用户到www组并指定id为1003

```sh
sudo useradd zz -g 1002 -u 1003 -m
```

**参数说明**

`-g`: `--gid` `GROUP` 用户初始登陆组的组名或号码。组名必须已经存在。组号码必须指代已经存在的组。

`-u`: `--uid` `UID` 用户 ID 的数字值。此值必须为唯一的，除非使用了 -o 选项。此值必须非负，默认使用大于等于 UID_MIN，且大于任何其他用户 ID 最小值。

`-m`: `--creat-home` 如果不存在，则创建用户主目录。

## 3. 修改用户的密码

```sh

```

## 4. 删除一个用户

```sh

```

## 5. 为该用户添加 sudo 权限

```sh

```

## 6. 查看用户所属的组

`groups`：查看当前用户所属的组

`groups <user1> <user2> <user3>`：查看 `<user1>`, `<user2>` 和 `<user3>` 所属的组

## 7.  查看所有用户和用户组

```sh
cat /etc/passwd

root:x:0:0:root:/root:/usr/bin/zsh
zzhenry:x:1000:1000:ZHU ZHAN,,,:/home/zzhenry:/bin/zsh
# 登录名:有无口令:用户ID:组ID:账户备注信息:用户Home目录:登录时用户shell的名称(超级用户有权限修改)

cat /etc/group

root:x:0:
zzhenry:x:1000:
# 组名:组加密口令:GID:组成员列表(用，隔开的每个组用户名)
```