#include <stdio.h>

/* print Fahrenheight - Celcius table for
 * farh = 0, 20, 40, ..., 300 */

main()
{
    float fahr, celcius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;
    
    printf("Fahrenheight | Celcius");
    printf("\n");

    fahr = lower;
    while (fahr <= upper) {
        celcius = (5.0/9.0) * (fahr - 32.0);
        /* Three characters wide and no decimal,
         * then six characters wide and one decimal */ 
        printf("%3.0f\t\t%6.1f\n", fahr, celcius);
        fahr = fahr + step;
    }
}

