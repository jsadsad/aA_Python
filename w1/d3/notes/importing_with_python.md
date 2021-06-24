1. A module is simply Python code in a separate file.
2. A package is the path to a directory that contains modules which is also a special type of module.
3. **init**.py is the default file for a package.
4. A submodule is another file in a module’s folder.
5. A function is (obviously!) a function in a module.

## Import Statements

Here are some common examples of importing modules

- import <module> - most basic
- import <package>.<subpackage>.<module> - dot syntax
- from <package> import <module> - one module in a package
- from <package> import <module>, <module> - multiple modules or submodules in a package
- from . import <submodule>- special case for module's **init**.py to get submodules in the same folder
- from <module> import <function>, <function> - down to the function level
- from <package> import <module> as <altName> - renaming to avoid confusion or conflict
