QuantConnect Python Algorithm Project
=============

Before we enable python support, follow the [installation instructions](https://github.com/QuantConnect/Lean#installation-instructions) to get LEAN running C# algorithms in your machine. 

### Install Python 3.6:
#### [Windows](https://github.com/QuantConnect/Lean#windows) 
##### Using [Anaconda](https://www.anaconda.com/) distribution:

1. Download the [installer](http://cdn.quantconnect.com/anaconda/Anaconda3-5.2.0-Windows-x86_64.exe) from QuantConnect
2. Execute the installer to install python in your system
   - After installation you will need to run the following conda instruction:

   ```bash
   conda install -y python=3.6.8
   ```

3. Install [pandas 0.25.3](https://pandas.pydata.org/)

   ```bash
   conda install -y pandas=0.25.3
   ```

##### Using [python.org](https://www.python.org/) distribution:

1. Download the [installer](http://cdn.quantconnect.com/python/python-3.6.8.exe) from QuantConnect
   - For AMD64/EM64T/x64, please use this [installer](http://cdn.quantconnect.com/python/python-3.6.8-amd64.exe) instead.
2. Execute the installer to install python in your system
   - When asked to select the features to be installed, make sure you select "Add python.exe to Path"
3. Open a Windows Powershell and install [pandas 0.25.3](https://pandas.pydata.org/)

   ```bash
   pip install pandas==0.25.3
   ```

##### Optional for both distributions:

1. Create `PYTHONHOME` system variables which value must be the location of your python installation (e.g. `C:\Anaconda3`):
   1. Right mouse button on My Computer. Click Properties.
   2. Click Advanced System Settings -> Environment Variables -> System Variables
   3. Click **New**.
      - Name of the variable: `PYTHONHOME`.
      - Value of the variable: python installation path.
2. Reboot computer to ensure changes are propogated.

#### [macOS](https://github.com/QuantConnect/Lean#macos)
##### Using [Anaconda](https://www.anaconda.com/) distribution:

1. Download the [installer](http://cdn.quantconnect.com/anaconda/Anaconda3-5.2.0-MacOSX-x86_64.pkg) from QuantConnect
2. Follow "[Installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os)" instructions from Anaconda documentation page.
   - After installation you will need to run the following conda instruction:

   ```bash
   conda install -y python=3.6.8
   ```

3. Install [pandas 0.25.3](https://pandas.pydata.org/)

   ```bash
   conda install -y pandas=0.25.3
   ```

##### Using [python.org](https://www.python.org/) distribution:

1. Download the [installer](http://cdn.quantconnect.com/python/python-3.6.8-macosx10.9.pkg) from QuantConnect
2. Execute the installer to install python in your system
3. Install [pandas 0.25.3](https://pandas.pydata.org/)

   ```bash
   pip install pandas==0.25.3
   ```

##### Note for both distributions:

If you encounter the "System.DllNotFoundException: python3.6m" runtime error when running Python algorithms:

1. Find `libpython3.6m.dylib` in your Python installation folder. If you installed Python with Anaconda, it may be find at

   `/Users/{your_user_name}/anaconda3/lib/libpython3.6m.dylib`

2. Open `Lean/Launcher/bin/Debug/Python.Runtime.dll.config`, add the following text and save:

   ```xml
   <configuration>
      <dllmap dll="python3.6m" target="{the path in step 1 including libpython3.6m.dylib}" os="!windows"/>
   </configuration>
   ```

#### [Linux](https://github.com/QuantConnect/Lean#linux-debian-ubuntu)

By default, **miniconda** is installed in the users home directory (`$HOME`):

   ```bash
   export PATH="$HOME/miniconda3/bin:$PATH"
   wget https://cdn.quantconnect.com/miniconda/Miniconda3-4.5.12-Linux-x86_64.sh
   bash Miniconda3-4.5.12-Linux-x86_64.sh -b
   rm -rf Miniconda3-4.5.12-Linux-x86_64.sh
   sudo ln -s $HOME/miniconda3/lib/libpython3.6m.so /usr/lib/libpython3.6m.so
   conda update -y conda pip
   conda install -y python=3.6.8
   conda install -y cython=0.29.17
   conda install -y pandas=0.25.3
   ```

#### Important note for Anaconda/Conda:

There is a [known issue](https://github.com/pythonnet/pythonnet/issues/609) with python 3.6.5 that prevents pythonnet installation. Please specify the install of v3.6.8 _exactly_, i.e. with

   ```bash
   conda install -y python=3.6.8
   ```

to upgrade python to version 3.6.8 as this is a known compatible version, used in QuantConnect Cloud, and other versions may have issues as of this writing

### Run python algorithm

1. Update the [config](https://github.com/QuantConnect/Lean/blob/master/Launcher/config.json) to run the python algorithm:

   ```json
   "algorithm-type-name": "BasicTemplateAlgorithm",
   "algorithm-language": "Python",
   "algorithm-location": "../../../Algorithm.Python/BasicTemplateAlgorithm.py",
   ```

2. Rebuild LEAN.
3. Run LEAN. You should see the same result of the C# algorithm you tested earlier.