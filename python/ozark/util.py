
import os
import shutil
import identicon
import subprocess
from rez.config import config as config_


def init():
    default_template = os.path.join(os.environ["REZ_OZARK_ROOT"], "template")
    template_dir = os.getenv("REZ_OZARK_TEMPLATE", default_template)
    template = os.path.join(template_dir, "profile.py")

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
