from setuptools import setup, find_packages

setup(
    name='automato',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'networkx>=2.6.3',
        'matplotlib>=3.4.3'
    ],
    author='Seu Nome',
    author_email='seu@email.com',
    description='Implementação de Autômato Finito Determinístico',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kfrural/lfa/extra/automato',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)