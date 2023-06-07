#include "lists.h"

/**
  * insert_node - inserts a number into a sorted singly linked list
  * @head: head of the linked list
  * @number: number to insert into the linked list
  *
  * Return: address of the new node, or NULL if it failed
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = NULL, *new_node = NULL, *temp = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	if (*head)
	{
		curr = *head;
		if (number <= curr->n)
		{
			new_node->next = curr;
			*head = new_node;
		}
		else
		{
			while (curr->next)
			{
				if (number <= curr->next->n)
				{
					temp = curr->next;
					curr->next = new_node;
					new_node->next = temp;
					return (*head);
				}
				curr = curr->next;
			}
			temp = curr->next;
			curr->next = new_node;
			new_node->next = temp;
		}
		return (*head);
	}
	new_node->next = NULL;
	*head = new_node;
	return (*head);
}
