#include "lists.h"

/**
 * insert_node - insert node in sorted list
 * @head: point to head of list
 * @number: node to be inserted
 * Return: address of new node or NULL on fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *tmp = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	
	if (*head == NULL)/*if no element in list insert as only item in list*/
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	if ((*head)->next == NULL)/*if only one item in list, comapare the two nodes*/
	{
		if ((*head)->n < new->n)
			(*head)->n = new->n;
		else
		{
			new->next = *head;
			*head = new;
		}
		return (new);
	}
	tmp = *head;/*if many nodes present, do comparison*/
	while (tmp->next != NULL)
	{
		if (new->n < tmp->n)
		{
			new->next = tmp;
			*head = new;
			return (new);
		}
		/*new node is the same as the exisiting node,insert*/
		/*compare prev and next node and insert in between*/
		if (((new->n > tmp->n && (new->n < (tmp->next)->n))
			|| new->n == tmp->n))
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	tmp->next = new;
	return (new);
}
