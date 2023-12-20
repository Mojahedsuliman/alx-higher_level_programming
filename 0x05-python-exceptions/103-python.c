#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
		if (!PyList_Check(p))
		{
				printf("[ERROR] Invalid PyListObject\n");
				return;
		}

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
		fflush(stdout);
}

void print_python_bytes(PyObject *p)
{
		if (!PyBytes_Check(p))
		{
				printf("[ERROR] Invalid PyBytesObject\n");
				return;
		}

		printf("[.] bytes object info\n");
		printf("  [.] Address of the object: %p\n", (void *)p);
		printf("  [.] Bytes: ");
		Py_ssize_t size = PyBytes_Size(p);
		Py_ssize_t max_bytes = (size > 10) ? 10 : size;
		char *bytes = PyBytes_AsString(p);
		for (Py_ssize_t i = 0; i < max_bytes; ++i)
		{
				printf("%02hhx ", bytes[i]);
		}
		if (size > 10)
		{
				printf("\n  [.] First 10 bytes: displayed");
		}
		printf("\n");
		fflush(stdout);
}

void print_python_float(PyObject *p)
{
		if (!PyFloat_Check(p))
		{
				printf("[ERROR] Invalid PyFloatObject\n");
				return;
		}

		printf("[.] float object info\n");
		printf("  [.] Value: %f\n", PyFloat_AsDouble(p));
		fflush(stdout);
}
