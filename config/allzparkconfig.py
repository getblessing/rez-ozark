
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
    user_roles = {getpass.getuser()}

    accessible_profiles = list()
    for pkg_family in iter_package_families(paths=__mongozark.profiles):

        latest_version = next(pkg_family.iter_packages())
        required_roles = set(getattr(latest_version, "roles", []))

        if required_roles.intersection(user_roles):
            accessible_profiles.append(pkg_family.name)

    return accessible_profiles


def applications():
    """Return list of applications

    Applications are typically provided by the profile,
    this function is called when "Show all apps" is enabled.

    """

    return []


def style_loader():
    try:
        from ozark import style
    except ImportError:
        print("Failed to load Ozark CSS stylesheet.")
        return

    return style.load_stylesheet()
