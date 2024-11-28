from setuptools import setup, find_packages

setup(
    name="dpayne",
    version="1.0.1",
    description="Dpayne CLI: A learning platform for Python programming. a python world",
    author="Dpayne (daniel.payne.unlimited@gmail.com)",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "dpayne=dpayne.cli:main",
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
