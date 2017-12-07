#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	listint_t *temp = *head;

	if (newnode == NULL)
		return (NULL);

	if (head == NULL)
	{
		free(newnode);
		return (NULL);
	}
	newnode->n = number;
	while (temp->next != NULL)
	{
		if ((*head) == NULL)
		{
			(*head) = newnode;
			newnode->next = NULL;
			return (newnode);
		}
		if (number < temp->n && temp->next == NULL)
		{
			newnode->next = temp;
			temp = newnode;
			return (newnode);
		}
		if (temp->next == NULL)
		{
			temp->next = newnode;
			newnode->next = NULL;
			return (newnode);
		}
		if (number < (temp->next->n))
		{
			newnode->next = temp->next;
			temp->next = newnode;
			return (newnode);
		}
		temp = temp->next;
	}
	return (NULL);
}
