#include <stdio.h>

void b();
void a();

void a() {
    printf("..ENTER A\n");
    b(); //Unresolved [ BUT shared libs allow unresolve symbols by default ]
    printf("..EXIT A\n");
}
