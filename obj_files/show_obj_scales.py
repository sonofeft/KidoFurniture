import os
from glob import glob
import trimesh
here = os.path.abspath(os.path.dirname(__file__))
print( 'here =', here )

obj_fileL = glob( os.path.join( here, '*.obj' ) )
print( 'Number of *.obj files:', len(obj_fileL) )

for obj_file in obj_fileL:
    mesh = trimesh.load_mesh( obj_file )
    print( os.path.split(obj_file)[-1], '  mesh.scale', mesh.scale )
    print( '  bbox=',mesh.bounding_box.primitive.extents )

