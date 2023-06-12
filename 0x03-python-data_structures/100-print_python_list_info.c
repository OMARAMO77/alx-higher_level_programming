#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, a = 0;
	PyObject *object;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	while (a < size)
	{
		printf("Element %d: ", a);
		object = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(object)->tp_name);
		a++;
	}
}
