#include <stdio.h>

/* print Fahrenheight - Celcius table for
 * farh = 0, 20, 40, ..., 300 */

main()
{
    float fahr;
    printf("Fahrenheight | Celcius");
    printf("\n");

    for (fahr = 300; fahr >= 0; fahr -= 20)
        printf("%3.0f\t\t%6.1f\n", fahr, (5.0/9.0) * (fahr - 32.0));
}

