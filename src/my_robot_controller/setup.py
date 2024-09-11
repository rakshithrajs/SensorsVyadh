from setuptools import find_packages, setup

package_name = "my_robot_controller"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="rakshith",
    maintainer_email="rakshith@todo.todo",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "test_node = my_robot_controller.my_first_node:main",
            "draw = my_robot_controller.draw_circle:main",
            "serial = my_robot_controller.h:main",
            "butt = my_robot_controller.butt:main",
        ],
    },
)
