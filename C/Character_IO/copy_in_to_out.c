#include <stdio.h>

/* Version 1 */

main()
{
    int c;
    c = getchar();
    while (c != EOF) {
        putchar(c); 
        c = getchar();
    }
}
