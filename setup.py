import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="eddy-mc-core",
    version="0.4.3",
    author="Cerberus Nuclear",
    author_email="nuclear@cerberusnuclear.com",
    description="Eddy, the MCNP and SCALE HTML output converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cerberus-Nuclear/Eddy-Core",
    packages=['eddymc_core', 'eddymc_core//mcnp', 'eddymc_core//scale', 'eddymc_core//static'],
    package_data={'eddymc_core//static': ['*']},
    install_requires=['Jinja2', 'importlib-resources'],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
