import os
import inspect
import json


def generate_api_doc(api_functions):
    doc = {}
    for func in api_functions:
        func_info = inspect.unwrap(func)
        doc[func_info.__name__] = {
            'description': func_info.__doc__ or 'No description provided',
            'parameters': inspect.signature(func).parameters,
        }
    return doc


def save_documentation(doc, output_path):
    with open(output_path, 'w') as f:
        json.dump(doc, f, indent=4)


if __name__ == '__main__':
    # Example API functions; you can replace these with your real API functions
    def api_function_one(param1, param2):
        """This is API function one."""
        pass

    def api_function_two(param1):
        """This is API function two with one parameter."""
        pass

    api_functions = [api_function_one, api_function_two]
    doc = generate_api_doc(api_functions)
    output_path = os.path.join('docs', 'api_documentation.json')
    save_documentation(doc, output_path)
