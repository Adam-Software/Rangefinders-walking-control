from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='Rangefinders-walking-control',
    version='0.1.1',
    packages=['src', 'tests'],
    url='https://github.com/Adam-Software/Rangefinders-walking-control',
    license='MIT',
    author='vertigra',
    author_email='a@nesterof.com',
    description='Rangefinders and walking control of the Adam robot',
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=['Adam-Serial-for-controller'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Other',
        'Programming Language :: C',
        'Programming Language :: Python :: 3'
    ]
)
