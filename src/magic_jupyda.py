import os
import subprocess
import argparse
from subprocess import CalledProcessError
from IPython.core.magic import (Magics, magics_class, cell_magic)
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

# idea is this:
# for each cell with jupyda cell magic will be saved as a file in project folder
# the project will be compiled
# and run by main() function


def print_byte_stream(bstream):
    for line in bstream.decode().split('\n'):
        print(line)


@magics_class
class Jupyda(Magics):
    def __init__(self, shell):
        super(Jupyda, self).__init__(shell)
        
        # try to get the compiler first
        try:
            self.compiler = subprocess.check_output(['which', 'gcc']
                , stderr=subprocess.STDOUT).decode().split('\n')[0]
        except CalledProcessError as cpe:
            print("Looks like the compiler doesn't exist.")
            print_byte_stream(cpe.output)
            self.compiler = None
            
            
        # current working directory
        self.cwd = os.getcwd()
        
        # this is the project folder to save all the source file
        self.src = os.path.join(self.cwd, 'src')
        
        # create the folder
        if not os.path.exists(self.src):
            os.mkdir(self.src)
        
        # if source file name not given then we will use a generic file name
        self.inp = os.path.join(self.src, '4beed3b9c4a886067de0e3a094246f78.cu')
        
        # we will use a common file name for all the compiled files (like a.out)
        self.aout = os.path.join(self.src, 'aout.o')
        
        
    def compile(self, src, aout, filepath):
        # compile it
        subprocess.check_output([self.compiler, '-v', '-I='+src, '-o='+aout, filepath]
           , stderr=subprocess.STDOUT
        )

        # subprocess.check_output([self.compiler, '-Wall', '-o'+aout, filepath]
        #    , stderr=subprocess.STDOUT
        # )
        
    @staticmethod
    def exec(obj):
        output = subprocess.check_output(
                [obj]
                , stderr=subprocess.STDOUT)
        return output
        
    
    @magic_arguments()
    @argument('-n', '--name', type=str, help='entire cell content will be saved in file with this name.')
    @argument('-nc', '--no_compile', help='save the file. ideally should be a .h file.', action="store_true")
    @cell_magic
    def jupyda(self, line, cell=None):
        """Saves this cells content in a file with the given name (optional).
            Compiles it.
            Runs it if not used with -oc argument.
        """
        
        # exit if compiler not found
        if self.compiler is None:
            print("Can't do anything without a compiler.")
            return
        
        # parser for the arguments
        args = parse_argstring(self.jupyda, line)
        filename = args.name
        nc = args.no_compile
        
        # if no filename provided, use the default filename
        if filename is None:
            filename=self.inp
        
        # check for legal file extensions
        ext = filename.split('.')[1]
        if ext not in ['cu', 'h']:
            print("Jupyda can handle only .cu and .h files. Please correct the extension [{}].".format(ext))
            return
        if (ext == 'h') and (nc is False):
            print("Can't compile .h files. Use -nc argument.")
            

        # write the cell content in a file in our project folder
        filepath = os.path.join(self.src, filename)
        with open(filepath, "w") as f:
            f.write(cell)
        
        output = b""
        if not nc:
            try:
                # compile the file
                self.compile(self.src, self.aout, filepath)
                print("======== Compilation successful! ========")
                # run the file
                output = self.exec(self.aout)
            except CalledProcessError as cpe:
                print_byte_stream(cpe.output)
            print_byte_stream(output)

 
