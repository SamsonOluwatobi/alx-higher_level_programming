#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

void print_python_object_info(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		print_python_float(p);
	}
	else if (PyBytes_Check(p))
	{
		print_python_bytes(p);
	}
	else if (PyList_Check(p))
	{
		print_python_list(p);
	}
	else
	{
		printf("[.] Unknown object info\n");
		printf("  [ERROR] Invalid Object\n");
	}
}

void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;
	double d = f->ob_fval;

	char *str = NULL;

	printf("[.] float object info\n");
	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

void print_python_bytes(PyObject *p)
{
	unsigned long int size;

	unsigned int i;

	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	size = ((PyVarObject *)p)->ob_size;
	trying_str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", trying_str);

	if (size < 10)
		printf("  first %lu bytes:", size + 1);
	else
		printf("  first 10 bytes:");

	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", trying_str[i]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
	unsigned long int size;

	unsigned int i;

	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		print_python_object_info(list->ob_item[i]);
	}
}
