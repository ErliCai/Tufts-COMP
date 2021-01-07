/*
 * A program to demonstrate that structures are call by value in C.
 * Also shows that (char *) and array of char are not the same, of
 * course.
 *
 * Mark A. Sheldon
 * Olin College
 * Fall 2009
 *
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_NAME_LEN 512

struct student {
    char name[MAX_NAME_LEN];
    int  num;
};

void print_struct (struct student data)
{
    printf("{ name = %s; num = %d }\n", data.name, data.num);
}

/*
 *  CBV stands for Call By Value.
 */
void cbv_mutate(struct student data)
{
    data.name[0] = 'b';
    data.num     = -1;
}

/*
 * CBR stands for Call By Reference.
 */
void cbr_mutate(struct student *data)
{
    data->name[0] = 'b';
    data->num     = -1;
}

int main(int argc, char **argv)
{
    struct student s, t;
    struct {
        char *name;
        int  num;
    } u;
    
    strncpy(s.name, "foo", MAX_NAME_LEN);
    s.num  = 4;
    
    t = s;
    
    /* u = s;                                                       */
    /*         produces an incompatible type error at compile time  */
    /*         as does an attempt to pass u to print_struct().  So  */
    /*         char[MAX_NAME_LEN] and (char *) are not the same.    */
    /*         Draw pictures of the state of the program after the  */
    /*         next two lines.                                      */
    
    u.name = s.name;
    u.num  = s.num;
    
    print_struct(s);
    
    cbv_mutate(s);
    print_struct(s);
    
    cbr_mutate(&s);
    print_struct(s);
    print_struct(t);
    
    /* print_struct(u); compilation error.  see above */
    printf("{ name = %s; num = %d }\n", u.name, u.num);
    
    return EXIT_SUCCESS;
}
