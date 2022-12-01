#include "lists.h"
/**
 * check_cycle - check if linked list has a cycle
 * @list: list
 * Return: return 0 if false else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *element1 = list;
	listint_t *element2 = list;
	if (!list)
		retun (0);
	while (element1->next != NULL && element1->next->next !=NULL)
	{
		element1 = element1->next->next;
		element2 = element->next;

		if (element1 == element2)
			return (1);
		else
		      retun (0);
	}
}

