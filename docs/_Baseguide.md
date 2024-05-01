# **Baseguide**

## **Overview**

Baseguide is a collaboration platform for parties working in the music industry. Different parties collaborate in activities from producing songs, publish , manages distribution and events for artists and songs.

## **Platform guidelines**

Django is chosen to be the platform for the core system of Baseguide. Features and services provided by guides will be grouped in modules based on relevance, services to be sold on the platform, and roles.

1. The term module is refered to Django App when used as first level.

   the module will include in the MVC files in directory
2. The term Package is refered to Django App when it includes multiple modules.

   The package will include multiple modules, each module will contain its own MVC files.
3. Platform will be rendering functionality to user through web UI to browsers as well as API Interface for mobile apps and front-end apps.
   Modules are expected to have 2 url patterns

   1) `<module-name>`/function : views will render web template
   2) `api/<module-name>`/function : views will render API response in json
4. All functions are expected to have documentation brief at the beginning of the function definition. Below is sample

```
def do\_action():
    """
    this is the documentation section for function do\_action
    """
    return True;
```

5. All related functionality related to a feature or a service to be contained within a module.

- when there are multiple services/functionality to be grouped in parent Module, it should be treated as package, where every functionality will be contained in submodule within the package.
- Example:
  - There will be common services/functionality that will be grouped together such as phonebook, calendar, etc.
  - Then, main module (package) will be named "Common" where submodules will be created "Phonebook" & "calendar".
  - Each submodule will contain related models, views, api views, init, other code segments.

6. The development of module shall undergo the following stages
   1. design: in this stage the definition of the models, views and helper functions are created with related documentation (point 4).
   2. api views development: at this stage the api views of the module is built. render views can be used for processing but not necessary have UI finalized.
   3. Djngo Tests: develop Django tests for the selected features to ensure that business logic is sound and acts per design.
   4. UI Design.
7. CRUD functions:
   1. Each model shall include its own CRUD functions.
   2. objects of model shall be used to update itself, and not to pass the object to pdate function.
   3. models that has linked models as sub-model (for example profile model has sub-model for billing address) shall include the CRUD functions for the sub-model.
   4. su-model shall include its CRUD functions, but to be used in the main model.
8. UI Design:
   1. Bootstrap will be used for the UI design in Django templates.
   2. if module will undergo frontend framework UI, module has to be locked for backend development prior UI design activity starts.

## **Modules `<Django Apps>`**

Baseguide core system modules will be progressively added, elaborated, and described.

Modules are

1. [Profile Module](./profile-module.md "./profile-module.md")
2. [Common Module](common-module.md)
3. [Plans Module](./plans-module.md)
