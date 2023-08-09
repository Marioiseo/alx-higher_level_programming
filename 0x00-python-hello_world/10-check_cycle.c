#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int check_cycle(listint_t *list)
{
	int num = 0;
	listint_t *slow , *fast;

	slow = fast = list;
	while(slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	if (slow == fast)
	{
		printf("lol this is cycle");
		num = 1;
		break;
	}
	if (num == 0)
	printf("there is cycle\n");
	}
	return num;
}
