#include "lists.h"
/**
 * print_python_list_info - Prints basic information about a Python list.
 *
 * @p: A pointer to a PyObject list.
 *
 * Return: Nothing.
 */

void print_python_list_info(PyObject *p)
{
	int size, allocate, i;
	PyObject *Object;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		Object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(Object)->tp_name);
	}
}
