from distutils.core import setup, Extension
 
module1 = Extension('spi', sources = ['spi.c'])
 
setup (name = 'SPI',
        version = '1.0',
        description = 'This is a module to access a hardware SPI device directly from Python.',
        ext_modules = [module1])
