#include "lists.h"

/**
 * check_cylce - checks if there is a cycle in a sigly linked list
 * @list: the linked list, contains the address of the head
 *
 * Return: returns 0 it there is no cycle, if there is any, returns 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
