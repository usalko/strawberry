try:
    # import modules and objects from external strawberry-graphql-tortoise-orm
    # package so that it can be used through strawberry.tortoise_orm namespace
    from strawberry_tortoise_orm import *  # noqa: F401, F403
except ModuleNotFoundError:
    import importlib

    def __getattr__(name):
        # try to import submodule and raise exception only if it does not exist
        import_symbol = f"{__name__}.{name}"
        try:
            return importlib.import_module(import_symbol)
        except ModuleNotFoundError:
            raise AttributeError(
                f"Attempted import of {import_symbol} failed. Make sure to install the"
                "'strawberry-graphql-tortoise-orm' package to use the Strawberry Tortoise ORM "
                "extension API."
            )
