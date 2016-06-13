#include <stdio.h>
#include <inttypes.h>
main() {

  uint64_t tmp_var1,  tmp_var2;
  uint32_t tmp = 0xffffffff;

  tmp_var1 = (uint64_t)(10 * tmp); 
  tmp_var2 = (uint64_t)tmp * 10; 

  //printf("%lx\n", tmp_var);
}
