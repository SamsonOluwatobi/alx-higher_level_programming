#include <Python.h>
#include <stdio.h>
/**
* print_python_bytes - Print information about Python bytes objects
* @p: Pointer to the Python object
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	unsigned long size, i;

	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);
	str = bytes->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
		printf("%02x%c", (unsigned char)str[i], i == 9 ||
		i == size - 1 ? '\n' : ' ');

}

/**
* print_python_list - Print information about Python lists
* @p: Pointer to the Python object
*/
void print_python_list(PyObject *p)
{
	PyListObject *list;
	unsigned long size, i;

	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
