from setuptools import setup

setup(
    name='crypto_trade_helpers',
    version='1.4.8',
    packages=['crypto_utils'],
    description='a random person generator',
    install_requires=["pytest","aio_pika","requests","unicorn_fy","python-dotenv"] # our external dependencies
)