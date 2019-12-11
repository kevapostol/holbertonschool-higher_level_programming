#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node of a sorted linked list
 *
 * @head: the head address of a linked list
 * @number: the number to be acces to the new node
 *
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *cur;

	cur = *head;
	new = malloc(sizeof(listint_t));

	if (head == NULL || new == NULL)
		return (NULL);

	if (*head == NULL)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (*head);
	}

	while (cur != NULL)
	{
		if (cur->n < number && number < cur->next->n)
		{
			new->n = number;
			new->next = cur->next;
			cur->next = new;
			break;
		}
		cur = cur->next;
	}

	return (new);
}
