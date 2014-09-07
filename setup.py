from setuptools import setup, find_packages

package = 'Sceptre'
version = '0.1'

setup(name=package,
      version=version,
      description="An evdev Python Joystick and Gamepad Library",
      install_requires=["evdev", "funcy"],
      packages=find_packages(),
      url='https://github.com/mvcisback/sceptre')
