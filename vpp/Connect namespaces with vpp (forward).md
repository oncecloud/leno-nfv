### 1. modify /etc/vpp/startup.conf (on host B)

###### both hosts need be modified
```
unix {
  nodaemon
  log /tmp/vpp.log
  full-coredump
}

dpdk {
    uio-driver uio_pci_generic
    dev 0000:81:00.0
    dev 0000:82:00.0
    socket-mem 4096
}

api-trace {
  on
}

api-segment {
  gid vpp
}
```

### 2. start vpp (on host B)
```
modprobe uio
insmod /root/ovs-dpdk/dpdk-stable-16.07.1/x86_64-native-linuxapp-gcc/kmod/igb_uio.ko
service vpp start
```

### 3. create namespace (on host A)

```
ip netns add ns0
ifconfig ens5f0 up
ip link set dev ens5f0 netns ns0
ip netns exec ns0 ifconfig ens5f0 10.0.1.1/24 up
ip netns exec ns0 ip route add 10.0.2.0/24 via 10.0.1.2 dev ens5f0

ip netns add ns1
ifconfig ens5f1 up
ip link set dev ens5f1 netns ns1
ip netns exec ns1 ifconfig ens5f1 10.0.2.1/24 up
ip netns exec ns1 ip route add 10.0.1.0/24 via 10.0.2.2 dev ens5f1
```

```
# ip netns exec ns0 ip route
10.0.1.0/24 dev ens5f0  proto kernel  scope link  src 10.0.1.1 
10.0.2.0/24 via 10.0.1.2 dev ens5f0
# ip netns exec ns1 ip route
10.0.1.0/24 via 10.0.2.2 dev ens5f1 
10.0.2.0/24 dev ens5f1  proto kernel  scope link  src 10.0.2.1
```

### 4. config vpp (on host B)

```
vppctl set int ip address TenGigabitEthernet81/0/0 10.0.1.2/24
vppctl set int ip address TenGigabitEthernet81/0/1 10.0.2.2/24
vppctl set int state TenGigabitEthernet81/0/0 up
vppctl set int state TenGigabitEthernet81/0/1 up
vppctl set int l2 bridge TenGigabitEthernet81/0/0 200
vppctl set int l2 bridge TenGigabitEthernet81/0/1 200

```

```
#vppctl show int
              Name               Idx       State          Counter          Count     
TenGigabitEthernet81/0/0          1         up       
TenGigabitEthernet81/0/1          2         up       
local0                            0        down
```

![](http://oc15i8gxi.bkt.clouddn.com//vpp/vm-vpp-vm/forward%20vpp.png)

### 4. test (on host A)

```
# ip netns exec ns0 ping 10.0.2.1
PING 10.0.2.1 (10.0.2.1) 56(84) bytes of data.
64 bytes from 10.0.2.1: icmp_seq=1 ttl=63 time=0.147 ms
64 bytes from 10.0.2.1: icmp_seq=2 ttl=63 time=0.127 ms
64 bytes from 10.0.2.1: icmp_seq=3 ttl=63 time=0.098 ms
64 bytes from 10.0.2.1: icmp_seq=4 ttl=63 time=0.104 ms
64 bytes from 10.0.2.1: icmp_seq=5 ttl=63 time=0.096 ms
64 bytes from 10.0.2.1: icmp_seq=6 ttl=63 time=0.097 ms
64 bytes from 10.0.2.1: icmp_seq=7 ttl=63 time=0.099 ms
64 bytes from 10.0.2.1: icmp_seq=8 ttl=63 time=0.096 ms
64 bytes from 10.0.2.1: icmp_seq=9 ttl=63 time=0.099 ms
64 bytes from 10.0.2.1: icmp_seq=10 ttl=63 time=0.100 ms
64 bytes from 10.0.2.1: icmp_seq=11 ttl=63 time=0.099 ms
^C
--- 10.0.2.1 ping statistics ---
11 packets transmitted, 11 received, 0% packet loss, time 10000ms
rtt min/avg/max/mdev = 0.096/0.105/0.147/0.019 ms
```

ns1:

```
# ip netns exec ns1 iperf -s
------------------------------------------------------------
Server listening on TCP port 5001
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  4] local 10.0.2.1 port 5001 connected with 10.0.1.1 port 43722
[ ID] Interval       Transfer     Bandwidth
[  4]  0.0-10.0 sec  11.0 GBytes  9.40 Gbits/sec
```

ns0:
```
[root@localhost ~]# ip netns exec ns0 iperf -c 10.0.2.1
------------------------------------------------------------
Client connecting to 10.0.2.1, TCP port 5001
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 10.0.1.1 port 43722 connected with 10.0.2.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  11.0 GBytes  9.41 Gbits/sec
```