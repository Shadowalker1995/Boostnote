# Install the NFS Client on the Client Systems

### 1. Install the NFS-Common Package

```sh
sudo apt update
sudo apt install nfs-common
```

### 2. Create a NFS Mount Point on Client

Create a mount point on which you will mount the nfs share from the NFS server.

```sh
sudo mkdir -p /mnt/nfs_clientshare
```

### 3. Mount NFS Share on Client System

Check the NFS Server’s IP address using `ifconfig` command

```sh
sudo mount SEVER_IP:/mnt/nfs_share /mnt/nfs_clientshare
```

### 4. Testing the NFS Share on Client System

Create a few files in the NFS share directory located in the server.

```sh
cd /mnt/nfs_share/
touch file1.txt file2.txt file3.txt
```

Now head back to the NFS client system and check if the files exist.

```sh
ls -l /mnt/nfs_clientshare/
```

