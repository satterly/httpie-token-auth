from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='httpie-token-auth',
    description='Token Auth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.1.0',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    license='MIT',
    url='https://github.com/guardian/httpie-token-auth',
    download_url='https://github.com/guardian/httpie-token-auth',
    py_modules=['httpie_token_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_token_auth = httpie_token_auth:TokenAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
