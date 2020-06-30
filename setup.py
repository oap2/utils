from setuptools import setup, find_packages

setup(
    name="oap-utils",
    version="0.1.0",
    description="oap common utils",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    author='wang wei',
    author_email="huawiceo@163.com",
    url='https://github.com/oap2/utils',
    install_requires=[
        'openpyxl',
        'pycryptodome',
        'boto3'
    ],
    license='MIT',
    packages=find_packages(),
    include_package_data=False,
    zip_safe=True,
)
