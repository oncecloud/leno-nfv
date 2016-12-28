
#### 1.Download Source
```bash
git clone https://gerrit.fd.io/r/vpp  
```
#### 2.build
(only once):
```bash
sudo vpp/build-root/vagrant/build.sh
```
update and build:
```bash
cd vpp/build-root
sudo git pull
sudo make distclean
sudo ./bootstrap.sh
```
make rpm package
```
sudo make V=0 PLATFORM=vpp TAG=vpp install-rpm
```
#### 3.install
```
sudo rpm -ivh *.rpm
```
#### 4.configure

```
sudo sysctl -w vm.nr_hugepages=2048
sudo modprobe uio_pci_generic
sudo ifconfig p2p1 down  # NIC which bind to dpdk should be down
```
modify startup.conf in the /etc/vpp directory
sample:
```
unix {
  nodaemon
  log /tmp/vpp.log
  full-coredump
}

dpdk {
    uio-driver uio_pci_generic
    dev 0000:03:00.0   #  lspci | grep Ethernet
    socket-mem 1024    #  if two numa nodes: 512, 512 (less than free hugepages)
}

api-trace {
  on
}

api-segment {
  gid vpp
}
```
#### 5.run and stop
```
sudo service vpp start
sudo service vpp stop
```


