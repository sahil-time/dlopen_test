#include <dlfcn.h>
#include <stdio.h>
#include <assert.h>
#include <signal.h>

typedef void (*fn_ptr)();

int main(void) {
    printf("\nENTER MAIN\n");

    void* lib = NULL;
    //lib = dlopen("/nobackup/sahisha2/a.so", RTLD_LAZY);
//    assert(lib);
    lib = dlopen("/ws/sahisha2-sjc/dlopen_test/libA.so", RTLD_NOW);
    if (lib == NULL) {
        fprintf(stderr, "=> Error: dlopen failed, %s\n", dlerror());
        return 0;
    }
//    dlclose(lib);
  //  assert(lib);
//    dlclose(lib);
  //  dlclose(lib);
    //int c;
    //scanf("%d\n",&c);
    fn_ptr fn = dlsym(lib, "a");
    if (fn == NULL) {
        fprintf(stderr, "=> Error: dlsym failed, %s\n", dlerror());
        return 0;
    }
   // assert(fn);
    fn();
//    raise(SIGSTOP);
    
    printf("EXIT MAIN\n\n");
    return 0;
}
