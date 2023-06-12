#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: head of the list
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int nod = 0, a = 0, *arr = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (temp)
	{
		nod++;
		temp = temp->next;
	}
	arr = malloc(sizeof(int) * nod);
	temp = *head;
	while (temp)
	{
		arr[a++] = temp->n;
		temp = temp->next;
	}
	a = 0;
	while (a < nod / 2)
	{
		if (arr[a] != arr[nod - 1 - a])
		{
			free(arr);
			return (0);
		}
		a++;
	}
	free(arr);
	return (1);
}
