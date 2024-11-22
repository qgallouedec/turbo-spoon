from setuptools import setup, find_packages

setup(
    name="trl",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["trl=trl.cli:main"],
    },
    install_requires=["transformers", "accelerate"],
)
