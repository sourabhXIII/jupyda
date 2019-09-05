from src.magic_jupyda import Jupyda as jupyda

def load_ipython_extension(ipython):
    # register the magics function
    plugin = jupyda(ipython)
    ip.register_magics(plugin)

