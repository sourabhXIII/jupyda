# jupyda
Ipython extension to execute CUDA C code in Jupyter notebook.
Now you can easily use the power of Google colab GPUs with your CUDA C code.

See this example colab [notebook](https://colab.research.google.com/drive/1NWnRqRfl3yY-DiezTwqS1NH-YVZptqu6).


## Usage:

1. Install the extension <br />
`!pip install jupyda`
2. Load the extension <br />
`%load_ext jupyda`
3. Check the params of the extension (optional) <br />
`%%jupyda?`
4. Execute a cell with `nvcc` <br />
`%%jupyda`
5. Adding a cell as a header file named `add.h` <br />
`%%jupyda -n add.h -nc`
6. To use the header file in a subsequent cell and execute <br />
`%%jupyda`
`#include"add.h"`
