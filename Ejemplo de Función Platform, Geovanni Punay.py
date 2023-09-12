#Módulo Platform
import platform

print(platform.platform())
print(platform.platform(1)) # type: ignore
print(platform.platform(False, True))

#Metodo Machine
print('-'*50)
print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.version())

print('-'*50)
print(platform.python_implementation())
print(platform.python_version())
print(platform.python_version_tuple())

print('Está trabajando actualmente en un sistema operativo: ', platform.system())