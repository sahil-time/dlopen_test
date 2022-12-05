#include <stdio.h>

void c();
void d();

void c() {
    printf("....ENTER C\n");
    d();    //Undefined ANYWHERE
    printf("....EXIT C\n");
}
