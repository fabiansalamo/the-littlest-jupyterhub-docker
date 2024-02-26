from setuptools import find_packages, setup

setup(
    name="the-littlest-jupyterhub-docker",
    version="1.0.1.dev",
    description="A small JupyterHub distribution that spawns user servers in individual Docker containers",
    url="https://github.com/fabiansalamo/the-littlest-jupyterhub-docker",
    author="Fabian Salamo",
    author_email="fabian278@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "ruamel.yaml==0.17.*",
        "jinja2",
        "pluggy==1.*",
        "backoff",
        "requests",
        "bcrypt",
        "jupyterhub-traefik-proxy==1.*",
        "docker"
    ],
    entry_points={
        "console_scripts": [
            "tljh-config = tljh.config:main",
        ]
    },
)
