import setuptools

with open('requirements.txt') as require:
    REQUIRE = require.read().splitlines()

with open('README.md') as readme:
    README = readme.read()

setuptools.setup(
    name = 'utrrs',
    version = 0.2,
    description = 'The Unicode Text Rendering Reference System (UTRRS).',
    long_description = README,
    url = 'http://fuelproject.org/utrrs',
    author = 'Vishal Vijayraghavan',
    author_email = 'vishalvvr@fedoraproject.org',
    license = 'GPLv3',
    install_requires = REQUIRE,
    python_requires=">=3.6",
    zip_safe=False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3 :: Only",
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)