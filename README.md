## Requirements

```
python: >3.7, <3.11
```

## Installation

CPU support:

```bash
pip install rembg
```

GPU support:

First of all, you need to check if your system supports the `onnxruntime-gpu`.

Go to https://onnxruntime.ai and check the installation matrix.

<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/danielgatis/rembg/master/onnxruntime-installation-matrix.png" width="400" />
</p>

If yes, just run:

```bash
pip install rembg[gpu]
```

After successfully installing rembg[gpu], you can run the Main Jupyter notebook file. Modify the input and output paths as necessary and make any additional changes required for resolution adjustments.