#include "lists.h"
/**
 * check_cycle - checks if the linked list cycles
 * @list: checked list
 * Return: 1 if cycle 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *check = list;
	listint_t *checc = list;

	if (check == NULL)
		return (0);
	while (check && check->next && checc->next->next)
	{
		check = check->next;
		checc = checc->next->next;
		if (check == checc)
			return (1);
	}
	return (0);
}
