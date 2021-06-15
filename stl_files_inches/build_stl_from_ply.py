import os
from glob import glob
import trimesh

here = os.path.abspath(os.path.dirname(__file__))
print( 'here =', here )

ply_dir = r'D:\glb_meshes\ply_files'
print( 'ply_dir =', ply_dir )

ply_fileL = glob( os.path.join( ply_dir, '*.ply' ) )
print( 'Number of *.ply files:', len(ply_fileL) )

for ply_file in ply_fileL:
    mesh = trimesh.load_mesh( ply_file )
    ply_fname = os.path.split(ply_file)[-1]
    print( ply_fname, '  mesh.scale', mesh.scale )
    print( '  ply bbox=',mesh.bounding_box.primitive.extents )
    
    #mesh.vertices *= 1.0/25.4 # convert mm to inches
    stl_fname = os.path.join( here, ply_fname[:-3] + 'stl' )
    print( '  stl_fname =',stl_fname )
    
    trimesh.exchange.export.export_mesh( mesh, stl_fname , file_type='stl' )
    

