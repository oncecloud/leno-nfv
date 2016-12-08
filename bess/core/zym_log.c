#include <stdio.h>
#include <stdlib.h>

#ifndef ZYM_LOG_H
#define ZYM_LOG_H
#include "zym_log.h"
#endif



int zf_enter(char* functionName){
  if(!ZF_ENABLE) return 0;
  FILE *fp = fopen(ZF_FILENAME, "a+");
  fprintf(fp,"[ZF_LOG]: Start Function  [%s]\n", functionName);
  fclose(fp);
  return 0;
}

int zf_out(char* functionName, char* returninfo){
  if(!ZF_ENABLE) return 0;
  FILE *fp = fopen(ZF_FILENAME, "a+");
  fprintf(fp,"[ZF_LOG]: End Function    [%s] with [%s]\n", functionName, returninfo);
  fclose(fp);
  return 0;
}

