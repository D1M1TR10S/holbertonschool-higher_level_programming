#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *check1 = list;
	listint_t *check2 = list;

	while (check2 != NULL && check1 != NULL)
	{
		check1 = check1->next;
		check2 = check2->next;
		check2 = check2->next;
		if(check1 == check2)
			return (1);
	}
	return (0);
}
