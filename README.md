# Flask Data App

Example Flask Website for Data Analysis.

## Helpful Links

[Display Pandas Data via Excel Graph](https://pandas-xlsxwriter-charts.readthedocs.io)

## Clone Repository

To clone the respository, run the following command:

```
git clone https://github.com/KrakenBadger/Alchemy.git
```

If you do not have git installed, you can install it with the following commands:

### Windows

Using winget

```
winget install -e --id Git.Git
```

### Linux

Using apt-get:

```
sudo apt install git
```

### MacOS 

Using Homebrew:

```
brew install git
```

## Installation Instructions

This project uses Python 3.13, and UV to manage dependencies.

### UV Installation

#### Windows

Open Powershell and run the following command:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### MacOS & Linux

Open Terminal and run the following command:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```




### SASS CSS Preprocessor

If you wish to modify the CSS Styles, you will need the SASS CSS Preprocessor.

You can install this with the following commands.

#### Windows

Using the Chocolatey Package Manager:

```
choco install sass
```

##### Chocolatey Package Manager

To install Chocolatey, open Powershell as an Adminstrator:

1. Check Policies

```
Get-ExecutionPolicy
```

If it returns `Restricted`, run the following command `Set-ExecutionPolicy AllSigned` or `Set-ExecutionPolicy Bypass -Scope Process`.

2. Install Chocolatey

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

#### MacOS & Linux

Using Homebrew:

```
brew install sass/sass/sass
```



## Install Dependencies and Run App

```
uv run app.py
```

If you want to run the application in debug mode, use the --debug flag.

```
uv run app.py --debug
```

You can also specify the IP Address and Port

```
uv run app.py --host 0.0.0.0 --port 5000
```

The default IP address is localhost or 127.0.0.1, and the default port is 5000.

So after running `uv run app.py`, navigate to http://127.0.0.1:5000/ to view the website.


### Compile SCSS -> CSS

Open the terminal and navigate to the project directory.

Run the following command:

```
sass sass/:static/css/
```

To run the file watcher use the --watch flag:

```
sass --watch sass/:static/css/
```

The first part `sass/` is the directory where the SCSS styles are stored.

The second part `static/css/` is the directory where the compiled CSS styles will be outputed.
