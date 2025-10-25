import subprocess
import sys


def uninstall_all_packages():
    # 获取已安装的包列表
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    packages = result.stdout.strip().split("\n")

    # 卸载每个包
    for package in packages:
        if package:
            subprocess.run(["pip", "uninstall", "-y", package])


if __name__ == "__main__":
    uninstall_all_packages()
