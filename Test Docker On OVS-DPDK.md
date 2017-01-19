# **Test Docker On OVS-DPDK**

For Details on OVS-DPDK, refer to [guide on Github](https://github.com/openvswitch/ovs/blob/master/INSTALL.DPDK.md#ovs-dpdk-install-guide)

>VMware linux: ubuntu 16.04 kylin

>docker 1.11.2 / openvswitch 2.6.90 / dpdk 16.07

##### 1.Install Docker
```bash
$sudo apt-get install docker.io
```

##### 2.Install and setup DPDK

```bash
$git clone git://dpdk.org/dpdk
$cd dpdk/
$./tools/dpdk-setup.sh
```

For Details on DPDK setup, refer to [install and setup dpdk](http://oc15i8gxi.bkt.clouddn.com/pdf/DPDK/dpdk%E5%AE%89%E8%A3%85%E5%B9%B6%E8%BF%90%E8%A1%8C%E5%AE%9E%E4%BE%8B.pdf).

```bash
$export DPDK_BUILD=/home/zena/Downloads/dpdk/x86_64-ivshmem-linuxapp-gcc
```

Note:Select ```x86_64-ivshmem-linuxapp-gcc``` as the DPDK environment to build 

##### 3.install OVS
```bash 
$git clone https://github.com/openvswitch/ovs.git
$cd ovs
$sudo apt-get install autoconf automake libtool
$sudo ./boot.sh
$./configure --with-dpdk=$DPDK_BUILD
$sudo make install
```

##### 4.Setup OVS
a. delete OVS DB and kill ovsdb_server(if need cleaning)

   ```bash
$sudo pkill -9 ovs
$sudo rm -rf /usr/local/var/run/openvswitch
$sudo rm -rf /usr/local/etc/openvswitch/
$sudo rm -f /usr/local/etc/openvswitch/conf.db
```
b. DB creation
```bash
$sudo mkdir -p /usr/local/etc/openvswitch
$sudo mkdir -p /usr/local/var/run/openvswitch
$sudo ovsdb-tool create /usr/local/etc/openvswitch/conf.db \
/usr/local/share/openvswitch/vswitch.ovsschema
```
c. Start ovsdb-server(No SSL support)
```bash
$sudo ovsdb-server \
--remote=punix:/usr/local/var/run/openvswitch/db.sock \
--remote=db:Open_vSwitch,Open_vSwitch,manager_options \
--pidfile --detach
```
d. Initialize DB
```bash
$sudo ovs-vsctl --no-wait init
```

e. start vswitch
>Open vSwitch can be started as normal. DPDK will be initialized as long as the dpdk-init option has been set to 'true'.

```bash
$export DB_SOCK=/usr/local/var/run/openvswitch/db.sock
$sudo ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-init=true
$sudo ovs-vswitchd unix:$DB_SOCK --pidfile --detach
```

##### 5. Setup Network
```bash
$sudo service docker start
$ifconfig docker0               #172.17.0.1
```
![1](http://oc15i8gxi.bkt.clouddn.com/image/test-ovs/VM-ovs-dpdk.png)



```bash
$sudo ovs-vsctl add-br br0 -- set bridge br0 datapath_type=netdev
$ifconfig br0 172.17.0.101/24 #in VM2 set br0 172.17.0.102/24
# create br0
$ovs-vsctl add-port br0 dpdk0 -- set Interface dpdk0 type=dpdk
# bind dpdk0 to br0
$ovs-vsctl add-port br0 vxlan -- set interface vxlan type=vxlan \
options:remote_ip=172.17.0.102 #in VM2 set br0 172.17.0.101
# setup vxlan
$ovs-vsctl show
```

```bash
$sudo docker run --net=none --privileged=true -it ubuntu:14.04 bash
# create new container
```

```bash
$sudo wget https://github.com/openvswitch/ovs/raw/master/utilities/ovs-docker  
$sudo chmod a+x ./ovs-docker
# download ovs-docker
$sudo ./ovs-docker add-port br0 eth0 b062406bc6b6 
# create eth0 in container, and bind it to br0. 
# b062406bc6b6 is container ID
```
```bash
b062406bc6b6@root: ifconfig eth0 172.17.0.11/24
#in VM2, container eth0 is set to 172.17.0.12/24
```


##### 6. Test
```bash
b062406bc6b6@root: ping 172.17.0.12
```

![2](http://oc15i8gxi.bkt.clouddn.com/image/test-ovs/Screenshot%20-ping-f1t2.png)

<br />

>有任何问题，欢迎讨论

>联系作者： zhangyiming15@otcaix.iscas.ac.cn