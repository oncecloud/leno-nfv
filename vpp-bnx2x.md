1. 先将```vpp```中的```dpdk-16.11.tar.xz```解压，然后```conf```目录下的```common_base```文件中的 ```BNX2X_PMD```为```y```，再压缩为```dpdk-16.11.tar.xz```
报错： ```md5 checksum bad```
```
make[2]: Entering directory `/home/zym/vpp/dpdk'
Bad Checksum! Please remove /home/zym/vpp/dpdk/dpdk-16.11.tar.xz and retry
make[2]: *** [/home/zym/vpp/build-root/build-vpp-native/dpdk/.download.ok] Error 1
make[2]: Leaving directory `/home/zym/vpp/dpdk'
make[1]: *** [dpdk-build] Error 2
make[1]: Leaving directory `/home/zym/vpp/build-root'
make: *** [install-rpm] Error 1
```
2. 修改 ```dpdk-16.11.tar.xz``` md5 码与新的压缩文件一致。
报错：```(bnx2x.o): undefined reference to symbol 'inflateInit2_'```

3. 缺少 ```zlib``` 库的支持，参考以前的ovs的做法，找到产生错误的Makefile 添加CFLAGS选项 ```-lz```
报错：```File /home/zym/vpp/build-root/rpm/SOURCES/vpp-17.04-rc0~9_g9902fcd.tar.gz: No such file or directory```

4. 在```/home/zym/vpp/build-root/rpm/SOURCES/```目录下找到了```vpp-17.01```的tgz的包，估计是因为dpdk的bnx2x选项打开后导致的需求的包名不一样。直接将其改名为```vpp-17.04-rc0~9_g9902fcd.tar.gz```。
报错：解压后找不到```vpp-17.04```

5. 将tgz的包解压发现文件夹名为```17.01```，于是改成```17.04```，重新打包。
问题：编译过程中开始下载dpdk

6. 虽然不知道为什么编译到这里还要在这个目录下再次下载dpdk，但是预测如果这里dpdk选项不改依旧不能支持bnx2x的网卡，将之前打包好的```dpdk-16.11.tar.xz```拷贝到17.04文件夹中的dpdk文件夹中。并修改文件夹中的dpdk md5码校验。
编译报错 ：```(bnx2x.o): undefined reference to symbol 'inflateInit2_'```

7. 这个问题和2中遇到的问题一样，去找错误的Makefile，发现并没有CFLAGS选项，添加 ```CFLAGS += "-lz"```，依旧失败。

下一步进行的工作
1. 尝试寻找生成该Makefile的地方，添加CFLAGS选项。 
2. 在父目录中以及其他可能对该Makefile造成影响的Makefile文件配置CFLAGS。

方案1的工作进度：
找到相关文件：```/home/zym/vpp/build-data/packages/vpp.mk```

方案2的尝试：
```
./rpm/vpp-17.04/build-root/Makefile
./rpm/vpp-17.04/build-root/build-tool-vpp-native/vppinfra/Makefile
./rpm/vpp-17.04/build-root/build-tool-vpp-native/vppapigen/Makefile
./rpm/vpp-17.04/build-root/build-vpp-native/vppinfra/Makefile
./rpm/vpp-17.04/build-root/build-vpp-native/svm/Makefile
./rpm/vpp-17.04/build-root/build-vpp-native/vlib/Makefile
./rpm/vpp-17.04/build-root/build-vpp-native/vlib-api/Makefile
./rpm/vpp-17.04/build-root/build-vpp-native/vnet/Makefile
./rpm/vpp-17.04/build-root/build-vpp-native/vpp/Makefile
./Makefile
```


6. 按照4中的提示信息进行库路径的修改
首先利用  ```/sbin/ldconfig -p | grep libz.so``` 指令查看库路径 得到结果
```
libz.so.1 (libc6,x86-64) => /lib64/libz.so.1
libz.so (libc6,x86-64) => /lib64/libz.so
```
然后将结果的路径添加到 ```./Makefile``` 文件中的 ```LD_LIBRARY_PATH``` 变量中去

但是如何在链接过程中添加 ```-L[LIBDIR]```
而且如果能够添加 ```-L[LIBDIR]``` 不如直接添加 ```-lz``` 更方便。

7. 尝试使用 libtool 工具， 上网阅读教程，粗浅总结，libtool使得引用库更方便，但是对于目前的问题，即，无法找到添CFLAGS位置，并没有什么有力的帮助。

下一步的工作：
阅读 vpp 的 Makefile， 了解它的 Makefile 是如何构建的， 了解 库的添加机制。


8. 回到3中的问题，到```/home/zym/vpp/build-root/rpm/SOURCES``` 目录下， 发现有一个```vpp-17.01```的压缩包，将其改为 ```vpp-17.04-rc0~9_g9902fcd.tar.gz```
提示问题：解压发现```vpp-17.04```不存在

9. 将```vpp-17.01```改名为```vpp-17.04```再压缩
继续编译过程中发现它重新下载了```dpdk-17.11.tar.xz```， 在vpp-17.04目录下，将之前打包的dpdk拷进来，并且改变Makefile中的MD5码。
同时上层目录中的```rpm/vpp-17.04 rpm/vpp-17.01```下也做了如下操作

10.编译报错 ：```(bnx2x.o): undefined reference to symbol 'inflateInit2_'```
企图修改```/home/zym/vpp/build-root/rpm/vpp-17.04/build-root/build-vpp-native/vpp/Makefile```
中的CFLAGS添加-lz，发现与之前不同的是，这里的Makefile并没有这样的选项。

11. 修改  ```/home/zym/vpp/build-data/packages/vpp.mk``` 中的LDFLAGS，添加lz选项。


成功。
