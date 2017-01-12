## 网卡型号： broadcom 57810
>[dpdk官网支持的网卡列表](http://dpdk.org/doc/nics)

##### dpdk 将 broadcom 57810 网卡归类为Qlogic bnx2x. 
##### bnx2x 驱动的网卡 dpdk 要求做[额外的配置](http://dpdk.org/doc/guides/nics/bnx2x.html)。

### 1. 适配工作：

#### dpdk:
##### 下载 firmware version 7.2.51.0

#### bess:
##### 打开```CONFIG_RTE_LIBRTE_BNX2X_PMD```选项

#### ovs-dpdk:
#####  打开```CONFIG_RTE_LIBRTE_BNX2X_PMD```选项，添加 zlib 运行库

#### [vpp](https://github.com/oncecloud/oStack-Network/blob/master/vpp-bnx2x.md):  
##### 打开```CONFIG_RTE_LIBRTE_BNX2X_PMD```选项，添加 zlib 运行库

### 2. debug工作：

##### 在按照官网要求配置后，使用了 ovs-dpdk, bess, vpp三种网络方案进行尝试，均存在不同程度的问题

>##### 正常流程：接管网卡->添加网卡->传输数据包
>##### - ovs-dpdk: 添加dpdk网卡时卡死
>##### - bess: PMD 无法正常传输数据包
>##### - vpp: 不能正常接管网卡


##### bess在dpdk数据包传输上存在问题，所以希望通过对ovs和bess调用dpdk API 的源码进行对比解析，定位ovs添加网卡的问题，改变源码从而解决ovs的问题，适配网卡。

##### 代码对比：
##### ovs/dpdk_eth_dev_init

```c
rte_eth_dev_is_valid_port
rte_eth_dev_info_get
dpdk_eth_dev_queue_setup
  ---rte_eth_dev_configure
  ---rte_eth_rx_queue_setup
  ---rte_eth_tx_queue_setup
rte_eth_dev_start
rte_eth_promiscuous_enable
rte_eth_allmulticast_enable
rte_eth_macaddr_get
rte_eth_link_get_nowait
rte_mempool_get_priv
rte_eth_dev_flow_ctrl_get
```

##### bess/pmd_init_port

```c
find_dpdk_port
rte_eth_dev_info_get
rte_rte_dev_configure
rte_eth_promiscuous_enable
rte_eth_rx_queue_setup
rte_eth_tx_queue_setup
rte_eth_dev_flow_ctrl_get
rte_eth_dev_start
```

##### 通过在bess,ovs,dpdk源码中添加[日志代码](https://github.com/oncecloud/oStack-Network)，得到运行流程的[日志信息](https://github.com/oncecloud/oStack-Network/tree/master/log)。

>##### 问题定位：

>##### ovs添加网卡卡死在 rte_eth_dev_start函数 中，然后进程被杀死，ovs再重启添加网卡进程，不断重复。

##### 尝试改动ovs传递的默认pmd配置参数，但是依旧存在卡死的问题。

