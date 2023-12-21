#include <stdio.h>
#include <stdlib.h>
#include "structs.h"

int
main()
{


    printf("Size of struct A: %zu bytes\n", sizeof(struct A));

    printf("Size of struct B: %zu bytes\n", sizeof(struct B));



    struct A* a_ptr = malloc(sizeof(struct A));

    if (a_ptr == NULL)
    {

        printf("Failed to allocate memory for struct A\n");

        return 1;

    }


    a_ptr->i = 1738;

    a_ptr->c = 'J';

    a_ptr->d = -0.69;


    printf("i: %d\n", a_ptr->i);

    printf("c: %c\n", a_ptr->c);

    printf("d: %lf\n", a_ptr->d);


    free(a_ptr);


    return 0;

}


