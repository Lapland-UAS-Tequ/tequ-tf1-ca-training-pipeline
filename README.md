# tequ-tf1-ca-training-pipeline
This guide is for configuring your Windows machine to train Tensorflow.js models. Guide assumes that source image files are annotated with Cloud Annotations tool (https://cloud.annotations.ai/).

## Requirements

- Windows OS (Windows 10 & Windows 2019 server are tested)
- NVIDIA GPU (Quadro P600 and Tesla P100 are tested)
- 



## Configuration

### 1. Download and install following software.

| Software      | Version       | Link |
| ------------- |:-------------:| :-------------:| 
| CUDA          | 10.0.130      | https://developer.nvidia.com/cuda-downloads |
| cuDNN         | 7.6.5.32      | https://developer.nvidia.com/cudnn |
| Protoc        | 3.17.3        | https://developers.google.com/protocol-buffers/docs/downloads |
| Python        | 3.7.9         | https://www.python.org/downloads/release/python-379/ |
| Git           | 2.33.0        | https://git-scm.com/downloads |
| GPU drivers   | |                     


### 2. cuDNN installation

Copy extracted files to CUDA Toolkit installation folder following the same folder structure.

Copy extracted files in folder ```Cuda\bin``` to ```C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin```

Copy extracted files in folder ```Cuda\lib``` to ```C::\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\lib```

Copy extracted files in folder ```Cuda\include``` to ```C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\include```

You could also setup environment variables to point the location of cuDNN files to make things work.



