
from rez.config import config as config_
from rez.packages import iter_package_families

import getpass


__mongozark = config_.plugins.package_repository.mongozark


def profiles():
    """Return list of profiles

    This function is called asynchronously, and is suitable
    for making complex filesystem or database queries.
    Can also be a variable of type tuple or list

    """
    # view: super set of profile `views` attributes
    #   REZ_VIEW=show.ongoing;dev.pipeline;

    # User name based filtering
    # (TODO) But could be department name or anything else,
    #   and implementing roles as packages.
    user_roles = {getpass.getuser().lower()}

    accessible_profiles = list()
    for pkg_family in iter_package_families(paths=__mongozark.profiles):

        latest_version = next(pkg_family.iter_packages())
        required_roles = set(r.lower() for r in
                             getattr(latest_version, "roles", []))

        if required_roles.intersection(user_roles):
            accessible_profiles.append(pkg_family.name)

    return accessible_profiles


def applications():
    """Return list of applications

    Applications are typically provided by the profile,
    this function is called when "Show all apps" is enabled.

    """

    return []


def themes():
    _themes = []

    try:
        from ozark import style
    except ImportError:
        print("Failed to load Ozark CSS stylesheet.")
    else:
        _themes.append({
            "name": "avalon",
            "source": style.load_stylesheet(),
        })

    return _themes


def application_parent_environment():
    import os
    from rez.resolved_context import ResolvedContext

    rxt = os.getenv("REZ_RXT_FILE")
    if not rxt:
        return os.environ.copy()

    # Allzpark is launched from a Rez resolved context, need to compute the
    # original environment so the application can be launched in a proper
    # parent environment.

    # TODO: Load environment from "house" package (.env file)

    context = ResolvedContext.load(rxt)
    context.append_sys_path = False
    changes = context.get_environ()
    current = os.environ.copy()
    rollbacked = dict()

    for key, value in current.items():
        current_paths = value.split(os.pathsep)
        changed_paths = changes.get(key, "").split(os.pathsep)
        roll_paths = []
        for path in current_paths:
            if path and path not in changed_paths:
                roll_paths.append(path)

        if roll_paths:
            rollbacked[key] = os.pathsep.join(roll_paths)

    return rollbacked
