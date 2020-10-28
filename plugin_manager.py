import importlib
import pkgutil
import types
from typing import Any, List

import plugins.repo


class PluginManager():

    def __init__(self, plugin_entry_point: str):
        self.plugins: List[Any] = []
        package = plugins.repo
        for importer, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
            if not is_pkg:
                plugin_module = f'{package.__name__}.{module_name}'
                print(f'Loading plugin: {module_name}')
                plugin = importlib.import_module(plugin_module)
                if plugin_entry_point not in plugin.__dict__:
                    print(f'Skip loading, Plugin entry point "{plugin_entry_point} is missing"')
                else:
                    self.plugins.append(plugin)
                    print(f'{plugin.__name__} : Loaded successfully')
            else:
                print(f'Skipping package: {module_name}')

    def get_plugins(self) -> List[types.ModuleType]:
        return self.plugins
