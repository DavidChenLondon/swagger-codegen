# coding: utf-8

"""
    Nomad Hawk

    This is the API descriptor for the Nomad Hawk API, responsible for tracking and analytics.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: paul@samarkand.global
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Nomad Hawk",
    author_email="paul@samarkand.global",
    url="",
    keywords=["Swagger", "Nomad Hawk"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the API descriptor for the Nomad Hawk API, responsible for tracking and analytics.  # noqa: E501
    """
)
