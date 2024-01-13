"""
Revisión: Obtener el resultado de un comando del sistema

 Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su
 ejecución y pueden usarse como referencia para consultar.


 result = subprocess.run(["host", "8.8.8.8"], capture_output=True)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())

import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)


import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)

import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)"""
# print(result.stderr)

"""
Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su 
ejecución y pueden usarse como referencia para consultar. 

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
"""
# ¿Qué método utiliza para preparar un nuevo entorno para modificar las variables de entorno?




