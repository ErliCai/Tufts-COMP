//
//  calculator.c
//  
//
//  Created by Erli Cai on 29/12/2020.
//

#include <stdio.h>
#include <stdlib.h> /* for atof() */
#include <math.h>

#define MAXOP   100  /* max size of operand or operator */
#define NUMBER  '0'  /* signal that a number was found */
#define SIN  '1'
#define EXP  '2'
#define POW  '3'

int getop(char []);
void push(double);
double pop(void);
/* reverse Polish calculator */
int main()
{
    int type, divisor;
    double op2, op1, r;
    char s[MAXOP];
    
    while ((type = getop(s)) != EOF) {
        switch (type) {
            case NUMBER:
                push(atof(s));
                break;
            case '+':
                push(pop() + pop());
                break;
            case '*':
                push(pop() * pop());
                break;
            case '-':
                op2 = pop();
                push(pop() - op2);
                break;
            case '/':
                op2 = pop();
                push(pop() / op2);
                break;
            case '\n':
                printf("\t%.8g\n", pop());
                break;
            case '%':
                op2 = pop();
                op1 = pop();
                divisor = (int) op1/op2;
                push( (r = op1 - divisor * op2) >= 0? r : op2 + r);
                break;
            case 't':
                op1 = pop();
                push(op1);
                printf("\t%.8g\n", op1);
                break;
            case 'd':
                op1 = pop();
                push(op1);
                push(op1);
                break;
            case 's':
                //printf("1");
                op1 = pop();
                op2 = pop();
                push(op1);
                push(op2);
                break;
            case SIN:
                push(sin(pop()));
                break;
            case POW:
                op2 = pop();
                push(pow(pop(), op2));
                break;
            case EXP:
                push(exp(pop()));
                break;
            default:
                printf("error: unknown command %s\n", s);
                break;
        }
    }
    return 0; }
