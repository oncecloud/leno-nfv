// Author: zym-ustc
// E-mail: zym201111@gmail.com

// For ovs-dpdk and bess to print log in specific file.
// Set ZF_ENABLE = 0 to disable the log function or 1 to enable.
// Set ZF_FILENAME = Absolute Filepath to change the path of logfile.
#include <stdio.h>
#include <stdlib.h>

#define ZF_ENABLE 1
#define ZF_FILENAME "/root/test/run/log/log-1"

int zf_enter(char* functionName);
int zf_out(char* functionName, char* returninfo);


