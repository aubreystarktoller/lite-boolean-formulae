import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        if self.distribution.tests_require:
            self.distribution.fetch_build_eggs(self.distribution.tests_require)

        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='lite-boolean-formulae',
    version='0.1b1',
    description="A naive CNF implentation to help with buliding logical statements",
    author='Aubrey Stark-Toller',
    author_email='aubrey@deepearth.uk',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=["six"],
    keywords='utils',
    packages=["lite_boolean_formulae"],
    tests_require = ['pytest', 'pytest-cov'],
    cmdclass = {'test': PyTest}
)
