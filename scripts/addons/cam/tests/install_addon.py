import tempfile
import sys
import subprocess
import pathlib

INSTALL_CODE=f"""
import bpy
bpy.ops.preferences.addon_install(filepath='{sys.argv[1]}')
bpy.ops.preferences.addon_enable(module='cam')
bpy.ops.wm.save_userpref()
"""

NUM_RETRIES=10

with tempfile.TemporaryDirectory() as td:
  file=pathlib.Path(td,"install.py")
  file.write_text(INSTALL_CODE)
  command = f'blender -b -P "{str(file)}"'
  # blender 4.0 installing addon crashes sometimes on mac github actions...
  for x in range(NUM_RETRIES):
    try:
      subprocess.run(command, shell=True, check=True)
      sys.exit(0)
    except Exception as e:
      print("Install addon failed, retrying:",e)


