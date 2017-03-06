### 1. modify /etc/vpp/startup.conf

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
    socket-mem 4096
}

api-trace {
  on
}

api-segment {
  gid vpp
}
```

### 2. start vpp
```
modprobe uio
insmod /root/ovs-dpdk/dpdk-stable-16.07.1/x86_64-native-linuxapp-gcc/kmod/igb_uio.ko
service vpp start
```

### 3.config vpp

##### host A: 

```
vppctl set int ip addr TenGigabitEthernet81/0/0 10.3.0.2/24
vppctl set int state TenGigabitEthernet81/0/0 up

rm -f /tmp/vhost2.sock
vppctl create vhost-user socket /tmp/vhost2.sock server
vppctl set int state VirtualEthernet0/0/0 up
vppctl set int l2 bridge VirtualEthernet0/0/0 200 0

vppctl create vxlan tunnel src 10.3.0.2 dst 10.3.0.1 vni 200
vppctl set int l2 bridge vxlan_tunnel0 200 1
```
##### host B:

```
vppctl set int ip addr TenGigabitEthernet81/0/0 10.3.0.2/24
vppctl set int state TenGigabitEthernet81/0/0 up

rm -f /tmp/vhost2.sock
vppctl create vhost-user socket /tmp/vhost2.sock server
vppctl set int state VirtualEthernet0/0/0 up
vppctl set int l2 bridge VirtualEthernet0/0/0 200 0

vppctl create vxlan tunnel src 10.3.0.2 dst 10.3.0.1 vni 200
vppctl set int l2 bridge vxlan_tunnel0 200 1
```



### 4. create VM with vhost-user socket

###### create VM
```
virt-install --virt-type kvm --name VM1 --ram 512 --vcpus=1 --network network=default --cdrom /root/CentOS-7-x86_64-Minimal-1611.iso --disk path=/vm-images/vm1.img,size=8 --graphics vnc,listen=0.0.0.0 --noautoconsole --os-type=linux --os-variant=rhel7

virsh edit VM1
```

###### modify configuration of VM
```
<domain type='kvm' xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'>
  <name>VM1</name>
  <uuid>1789d5b7-fc13-4f12-a01a-b2c388524f57</uuid>
  <memory unit='KiB'>4194304</memory>
  <currentMemory unit='KiB'>4194304</currentMemory>
  <vcpu placement='static'>4</vcpu>
...
  <qemu:commandline>
    <qemu:arg value='-chardev'/>
    <qemu:arg value='socket,id=char0,path=/tmp/vhost2.sock'/>
    <qemu:arg value='-netdev'/>
    <qemu:arg value='vhost-user,id=mynet2,chardev=char0'/>
    <qemu:arg value='-device'/>
    <qemu:arg value='virtio-net-pci,netdev=mynet2,mac=52:54:00:01:00:33'/>
    <qemu:arg value='-object'/>
    <qemu:arg value='memory-backend-file,id=mem,size=4096M,mem-path=/dev/hugepages,share=on'/>
    <qemu:arg value='-numa'/>
    <qemu:arg value='node,memdev=mem'/>
    <qemu:arg value='-mem-prealloc'/>
  </qemu:commandline>
</domain>
```

###### start VM
```
virsh start VM1
```

![Architecture](http://oc15i8gxi.bkt.clouddn.com//vpp/vxlan/vpp-vxlan%20%E6%80%A7%E8%83%BD%E6%9E%B6%E6%9E%84%E5%9B%BE.png)


### 4. test

VM1 on host A:

![](http://oc15i8gxi.bkt.clouddn.com//vpp/vxlan/%E6%80%A7%E8%83%BD%E7%BB%93%E6%9E%9C.PNG)
