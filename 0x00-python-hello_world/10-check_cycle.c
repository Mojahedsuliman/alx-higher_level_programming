#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly list has a cycle in it
 * @list: singly linked list
 *
 * Return: 0 if no cycle, 1 if there is
*/
int check_cycle(listint_t *list)
{
		listint_t *slow = list;
		listint_t *fast = list;

		while (slow && fast && fast->next)
		{
				slow = slow->next;
				fast = fast->next->next;
				if (slow == fast)
				return (1);
			}
		return (0);
}
