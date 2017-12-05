#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - Checks linked list to see if it's a cycle
 * @list: A pointer to the linked list being checked
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *check1 = list;
	listint_t *check2 = list;

	while (check2 != NULL && check2->next != NULL && check2->next->next != NULL)
	{
		check1 = check1->next;
		check2 = check2->next->next;
		if(check1 == check2)
			return (1);
	}
	return (0);
}
