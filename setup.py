from setuptools import setup, find_packages

setup(
    name="dpayne",
    version="1.0.1",
    description="Dpayne CLI: A learning platform for Python programming - a Python world",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Dpayne",
    author_email="daniel.payne.unlimited@gmail.com",
    url="https://github.com/yourusername/dpayne",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "flask",
        "flask-socketio",
        "requests",
        "flask-cors",
        "flask-limiter",
        "flask-talisman",
        "gunicorn",
        "gevent",
    ],
    entry_points={
        "console_scripts": [
            "dpayne=dpayne.cli:main",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False,
)
