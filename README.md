ostack-ovs : Open vSwitch with DPDK
======================

This document describes how to configure vSwitch using a DPDK
datapath. Open vSwitch can use the DPDK library to operate entirely in
userspace.

Build requirements
------------------

- A `DPDK supported NIC`_, but not inclide mlx4, mlx5, bnx2x, qede

  Only required when physical ports are in use

- A suitable kernel

  On Linux Distros running kernel version >= 3.0, only `IOMMU` needs to enabled
  via the grub cmdline,

.. _DPDK supported NIC: http://dpdk.org/doc/nics


Installing
----------


1. Download ostack-release-1.0-1.el7.centos.x86_64.rpm

       $ rpm --force -ivh http://123.56.72.53:81/ec2/once/releases/ostack/ostack-release-1.0-1.el7.centos.x86_64.rpm

2. Install openvswitch with dpdk 

       $ yum install openvswitch

Install OVS
~~~~~~~~~~~

OVS can be installed using different methods. For OVS to use DPDK datapath, it
has to be configured with DPDK support (``--with-dpdk``).

.. note::
  This section focuses on generic recipe that suits most cases. For
  distribution specific instructions, refer to one of the more relevant guides.

.. _OVS sources: http://openvswitch.org/releases/

Setup
-----

Setup Hugepages
~~~~~~~~~~~~~~~

Allocate a number of 2M Huge pages:

-  For persistent allocation of huge pages, write to hugepages.conf file
   in `/etc/sysctl.d`::

       $ echo 'vm.nr_hugepages=2048' > /etc/sysctl.d/hugepages.conf

-  For run-time allocation of huge pages, use the ``sysctl`` utility::

       $ sysctl -w vm.nr_hugepages=N  # where N = No. of 2M huge pages

To verify hugepage configuration::

    $ grep HugePages_ /proc/meminfo

Mount the hugepages, if not already mounted by default::

    $ mount -t hugetlbfs none /dev/hugepages``


Setup OVS
~~~~~~~~~

Open vSwitch should be started as described following, and the ``dpdk-init`` option must be set to
``true``. For example::

    $ ssytemctl start openvswitch
    $ ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-init=true

There are many other configuration options, the most important of which are
listed below. Defaults will be provided for all values not explicitly set.

``dpdk-init``
  Specifies whether OVS should initialize and support DPDK ports. This is a
  boolean, and defaults to false.

``dpdk-lcore-mask``
  Specifies the CPU cores on which dpdk lcore threads should be spawned and
  expects hex string (eg '0x123').

``dpdk-socket-mem``
  Comma separated list of memory to pre-allocate from hugepages on specific
  sockets.

``dpdk-hugepage-dir``
  Directory where hugetlbfs is mounted

``vhost-sock-dir``
  Option to set the path to the vhost-user unix socket files.

If allocating more than one GB hugepage (as for IVSHMEM), you can configure the
amount of memory used from any given NUMA nodes. For example, to use 1GB from
NUMA node 0, run::

    $ ovs-vsctl --no-wait set Open_vSwitch . \
        other_config:dpdk-socket-mem="1024,0"

Similarly, if you wish to better scale the workloads across cores, then
multiple pmd threads can be created and pinned to CPU cores by explicity
specifying ``pmd-cpu-mask``. For example, to spawn two pmd threads and pin
them to cores 1,2, run::

    $ ovs-vsctl set Open_vSwitch . other_config:pmd-cpu-mask=6


Creating bridges and ports
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now use ovs-vsctl to set up bridges and other Open vSwitch features.
Bridges should be created with a ``datapath_type=netdev``::

    $ ovs-vsctl add-br br0 -- set bridge br0 datapath_type=netdev

Now you can add DPDK devices. OVS expects DPDK device names to start with
``dpdk`` and end with a portid. ovs-vswitchd should print the number of dpdk
devices found in the log file::

    $ ovs-vsctl add-port br0 dpdk0 -- set Interface dpdk0 type=dpdk
    $ ovs-vsctl add-port br0 dpdk1 -- set Interface dpdk1 type=dpdk

After the DPDK ports get added to switch, a polling thread continuously polls
DPDK devices and consumes 100% of the core, as can be checked from 'top' and
'ps' cmds::

    $ top -H
    $ ps -eLo pid,psr,comm | grep pmd

Creating bonds of DPDK interfaces is slightly different to creating bonds of
system interfaces. For DPDK, the interface type must be explicitly set. For
example::

    $ ovs-vsctl add-bond br0 dpdkbond dpdk0 dpdk1 \
        -- set Interface dpdk0 type=dpdk \
        -- set Interface dpdk1 type=dpdk

To stop ovs-vswitchd & delete bridge, run::

    $ systemctl stop openvswitch

PMD thread statistics
~~~~~~~~~~~~~~~~~~~~~

To show current stats::

    $ ovs-appctl dpif-netdev/pmd-stats-show

To clear previous stats::

    $ ovs-appctl dpif-netdev/pmd-stats-clear

Port/rxq assigment to PMD threads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To show port/rxq assignment::

    $ ovs-appctl dpif-netdev/pmd-rxq-show

To change default rxq assignment to pmd threads, rxqs may be manually pinned to
desired cores using::

    $ ovs-vsctl set Interface <iface> \
        other_config:pmd-rxq-affinity=<rxq-affinity-list>

where:

- ``<rxq-affinity-list>`` ::= ``NULL`` | ``<non-empty-list>``
- ``<non-empty-list>`` ::= ``<affinity-pair>`` |
                           ``<affinity-pair>`` , ``<non-empty-list>``
- ``<affinity-pair>`` ::= ``<queue-id>`` : ``<core-id>``

For example::

    $ ovs-vsctl set interface dpdk0 options:n_rxq=4 \
        other_config:pmd-rxq-affinity="0:3,1:7,3:8"

This will ensure:

- Queue #0 pinned to core 3
- Queue #1 pinned to core 7
- Queue #2 not pinned
- Queue #3 pinned to core 8

After that PMD threads on cores where RX queues was pinned will become
``isolated``. This means that this thread will poll only pinned RX queues.

.. warning::
  If there are no ``non-isolated`` PMD threads, ``non-pinned`` RX queues will
  not be polled. Also, if provided ``core_id`` is not available (ex. this
  ``core_id`` not in ``pmd-cpu-mask``), RX queue will not be polled by any PMD
  thread.

.. _dpdk-guest-setup:

DPDK in the VM
--------------

Coming one....
