from setuptools import setup

setup(
    name='crypto_trade_helpers',
    version='1.5.4',
    packages=['crypto_utils'],
    description='a random person generator',
    install_requires=["pytest","aio_pika","requests","unicorn_fy","python-dotenv","typing-extensions"] # our external dependencies
)