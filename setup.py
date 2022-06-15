from setuptools import setup

setup(
    name='crypto_trade_helpers',
    version='1.1',
    packages=['crypto_utils'], # contains our actual code
    author='chris',
    author_email='chris@packagr.app',
    description='a random person generator',
    # scripts=['bin/make-person'], # the launcher script
    install_requires=["pytest","aio_pika"] # our external dependencies
)