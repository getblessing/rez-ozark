
name = "ozark"

version = "0.2.3"

description = "Able to read from MongoDB"

authors = ["davidlatwe"]

tools = [
    "party",
]

requires = [
    "rez",
    "localz",
    "identicon",
    "pymongo",
    "montydb",
    "allzpark",
    "graphviz",
]

build_command = "python {root}/rezbuild.py {install}"


def commands():
    import os
    env = globals()["env"]

    # Keep pre-exists `REZ_CONFIG_FILE` if any, e.g. from ~/.bash_profile
    # which might get overwritten when new shell spawned.
    env["REZ_CONFIG_FILE"] = os.getenv("REZ_CONFIG_FILE", "")
    env["REZ_CONFIG_FILE"].append("{root}/config/rezconfig.py")

    env["ALLZPARK_CONFIG_FILE"] = "{root}/config/allzparkconfig.py"

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")


def post_commands():
    # print mongodb uri
    pass
