
import os


name = "%s"
version = "1.0.0"

# Variables unrelated to Rez are typically prefixed with `_`
_data = {
    "label": "%s",
    "icon": "{root}/resources/icon.png"
}

authors = [
    # profile owners
]

views = [
    # List out features of this profile,
    # e.g. "show.ongoing", "dev.pipeline", ...
]

roles = [
    # List out which role can have access to this profile,
    # e.g. "artist", "technical", "developer", "admin", ...
    # or simple username.
]

requires = [
    # List out profile required packages,
    # e.g. "~maya-2020", "~python-3", "~pycharm", ...
]


# Set up environment
def commands():
    env = globals()["env"]


"""
!!! Do not change following attributes !!!
"""
filesystem_root = os.getcwd()  # for mongozark repository
build_command = False
ozark_profile = True
no_variants = True
