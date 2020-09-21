
import os
from os.path import expanduser
ModifyList = globals()["ModifyList"]

# Location: install
__install_uri = os.getenv("OZARK_MONGODB_INSTALL",
                          "montydb://" + expanduser("~/rez/ozark-data"))
__install_loc = os.getenv("OZARK_LOCATION_INSTALL",
                          "mongozark@install.rez.ozark")

# Location: release
__release_uri = os.getenv("OZARK_MONGODB_RELEASE",
                          "localhost:27017")
__release_loc = os.getenv("OZARK_LOCATION_RELEASE",
                          "mongozark@release.rez.ozark")


__profiles_path = [
    __install_loc,
    __release_loc,
]
packages_path = ModifyList(append=__profiles_path)


plugins = {
    "package_repository": {
        "mongozark": {
            "uri": {
                "install": __install_uri,
                "release": __release_uri,
            },
            "location": {
                "install": __install_loc,
                "release": __release_loc
            },
            # (NOTE) Rez config do not save custom attributes, so we save
            #   our profile packages path here, with order preserved.
            "profiles": __profiles_path,

            # database settings
            "mongodb": {
                "select_timeout": int(
                    os.getenv("OZARK_MONGODB_SELECT_TIMEOUT", "3000")  # 3 sec
                ),
            },
        },
    }
}

plugin_path = ModifyList(append=[
    # The path *above* rezplugins/ directory
    os.path.dirname(os.path.dirname(__file__))
])

# Turn this on if plugin not loaded.
# Or set environment var `REZ_DEBUG_PLUGINS=1`
debug_plugins = False
