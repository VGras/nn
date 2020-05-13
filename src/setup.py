import setuptools

setuptools.setup(
    name                            = "test",
    packages                        = setuptools.find_packages(where = "python"),
    package_dir                     = {
        "" : "python"
    },
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
