
import os
import sys
import shutil
import subprocess


additional_rez_core_dependencies = [
    "montydb",
    "pymongo",
]


def build(source_path, build_path, install_path, targets=None):
    targets = targets or []

    if "install" in targets:
        dst = install_path
    else:
        dst = build_path

    dst = os.path.normpath(dst)

    if os.path.isdir(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)

    print("Installing additional dependencies into Rez core")
    install_rez_dependency(additional_rez_core_dependencies)

    for dirname in [".resources", "bin", "config", "python", "rezplugins"]:
        dir_src = os.path.join(source_path, dirname)
        dir_dst = os.path.join(dst, dirname)
        shutil.copytree(dir_src, dir_dst)

    print("Ozark installed.")


def install_rez_dependency(modules):
    args = [
        "rez-env",
        "rezcore",  # Dive into Rez's virtual env
        "--",
        "pip",
        "install"
    ] + modules

    subprocess.check_call(args)


if __name__ == "__main__":
    build(source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
          build_path=os.environ["REZ_BUILD_PATH"],
          install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
          targets=sys.argv[1:])
