# Installing and configuring NFS Server on Ubuntu

### 1. Install NFS Kernel Server in Ubuntu

```sh
sudo apt update
sudo apt install nfs-kernel-server
```

### 2. Create an NFS Export Directory

Creating a directory that will be shared among client systems.

```sh
sudo mkdir -p /mnt/nfs_share
```

Since all the client machines need to access the shared directory, remove any restrictions in the directory permissions.

```sh
sudo chown -R nobody:nogroup /mnt/nfs_share/
sudo chmod 777 /mnt/nfs_share/
```

### 3. Grant NFS Share Access to Client Systems

Permissions for accessing the NFS server are defined in the `/etc/exports` file. Edit the file with vim:

```sh
sudo vim /etc/exports
```

To grant access to a single client, use the syntax:

```
/mnt/nfs_share  client_IP_1 (re,sync,no_subtree_check)
```

For multiple clients, specify each client on a separate file:

```
/mnt/nfs_share  client_IP_1 (re,sync,no_subtree_check)
/mnt/nfs_share  client_IP_2 (re,sync,no_subtree_check)
```

Explanation about the options used in the above command:

- **rw**: Stands for Read/Write.
- **sync**: Requires changes to be written to the disk before they are applied.
- **No_subtree_check**: Eliminates subtree checking.

![image-20201108131134342](https://i.loli.net/2020/11/09/dBMlSDJ8emTqj5E.png)

### 4. Export the NFS Share Directory

After granting access to the preferred client systems, export the NFS share directory and restart the NFS kernel server for the changes to come into effect.

```sh
sudo exportfs -a
sudo systemctl restart nfs-kernel-server
```

### 5. Allow NFS Access through the Firewall

Reload or enable the firewall (if it was turned off) and check the status of the firewall. Port **2049**, which is the default file share, should be opened.

```sh
sudo ufw enable
sudo ufw status
```

