from Browser import Browser

br = Browser()
keywords = br.get_keyword_names()
function_list = list()
for keyword in keywords:
    if ' ' in keyword:
        for key in br.attributes.keys():
            if keyword == br.attributes[key].robot_name and ' ' not in key:
                keyword_name = key
                break
    else:
        keyword_name = keyword
    args = br.get_keyword_arguments(keyword)
    types = br.get_keyword_types(keyword)
    args_str = ""
    for arg in args:
        if isinstance(arg, tuple):
            arg_name = arg[0]
            if arg_name[0] == '*':
                tpe = types[arg_name[1:]]
            else:
                tpe = types[arg_name]
            try:
                arg_type = tpe.__name__
            except:
                arg_type = str(tpe.__repr__()).lstrip('typing.')
            if arg[1] is None:
                arg_type_str = f'Optional[{arg_type}]'
            else:
                arg_type_str = arg_type
            if arg_type == 'str':
                arg_str = f"{arg_name}: {arg_type_str} = '{arg[1]}'"
            else:
                arg_str = f"{arg_name}: {arg_type_str} = {arg[1]}"
        else:
            if arg[0] == '*':
                arg_name = arg[1:]
            else:
                arg_name = arg
            if arg_name in types:
                tpe = types[arg_name]
                try:
                    arg_type = tpe.__name__
                except:
                    arg_type = str(tpe.__repr__()).lstrip('typing.')
                arg_str = f'{arg}: {arg_type}'
            else:
                arg_str = f'{arg}'

        args_str = f'{args_str}, {arg_str}'
    function_list.append(f'    def {keyword_name}(self{args_str}): ...\n')

function_list.sort()

with open('__init__.pyi', 'w') as stub_file:
    stub_file.write("""from concurrent.futures import Future
from typing import Union, Any, Dict, List, Optional

from .assertion_engine import (
    bool_verify_assertion,
    verify_assertion,
    list_verify_assertion,
    dict_verify_assertion,
    int_dict_verify_assertion,
    int_str_verify_assertion,
    AssertionOperator,
)
from .keywords.input import SelectAttribute, MouseButton, KeyboardModifier
from .keywords.playwright_state import SupportedBrowsers, ViewportDimensions, ColorScheme
from .keywords.waiter import ElementState
from .playwright import Playwright
from .version import VERSION


class Browser:\n""")
    stub_file.writelines(function_list)