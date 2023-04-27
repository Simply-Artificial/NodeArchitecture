from setuptools import setup

setup(
    name='sa-node-architecture',
    version='{{VERSION_PLACEHOLDER}}',
    description="Node Architecture: A simple method to communicate between applications using UNIX sockets",
    url='https://github.com/Simply-Artificial/NodeArchitecture',
    author='ItsMeAlfie0',
    author_email='simply-artificial@itsmealfie0.com',
    license='MIT',
    packages=[
        'node_architecture',
        'node_architecture.Server'
    ],
    install_requires=open('requirements.txt').read().splitlines(),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        "Operating System :: Linux",
    ],
)
