
import os
import shutil
import identicon
import subprocess
from rez.config import config as config_


def init():
    ozark_root = os.environ["REZ_OZARK_ROOT"]
    template = os.path.join(ozark_root, ".resources", "package_template.py")
    package_py = os.path.join(os.getcwd(), "package.py")
    if os.path.exists(package_py):
        print("package.py already exists in current directory.")
        return

    profile_name = os.path.basename(os.getcwd())

    with open(template, "r") as plate:
        lines = plate.read() % (profile_name, profile_name)
    with open(package_py, "w") as pkg_file:
        pkg_file.write(lines)

    res_dir = os.path.join(os.getcwd(), "resources")
    os.makedirs(res_dir)

    # generate identicon for profile
    icon_path = identicon.generate(profile_name)
    shutil.move(icon_path, os.path.join(res_dir, "icon.png"))

    # Open profile package with default editor for authoring
    subprocess.call([
        "idle",
        "-e",
        package_py,
    ])


def ls(location=None):
    if location:
        location = get_location(location)
        if location is None:
            raise Exception("Location '%s' not registered in mongozark.")

        args = [
            "rez-search",
            "--paths",
            location,
        ]

    else:
        locations = get_location()
        if not locations:
            raise Exception("Not any location registered in mongozark.")

        args = [
            "rez-search",
            "--paths",
            os.path.pathsep.join(locations)
        ]

    subprocess.call(args)


def build(location=None):
    if location:
        location = get_location(location)
        if location is None:
            raise Exception("Location '%s' not registered in mongozark.")

        args = [
            "rez-build",
            "--install",
            "--prefix",
            location,
        ]

    else:
        args = [
            "rez-build",
        ]

    os.environ["REZ_OZARK_BUILD"] = "1"
    subprocess.check_call(args)


def get_location(name=None):
    config = get_config()
    if name:
        return getattr(config.location, name, None)
    else:
        return list(config.location.values())


def get_config():
    return config_.plugins.package_repository.mongozark
