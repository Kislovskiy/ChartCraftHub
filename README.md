<img src="./docs/source/images/logo.svg" alt="drawing" width="400"/>

## Home for "Code, debug, reuse this chart" workshop materials
"Code, debug, reuse this chart" will take place on 24th of March 2024 at 09:00 at Applied Machine Learning Days 2024 in Lausanne, Switzerland.


![AMLD 2024](./docs/source/images/amld_code_debug_reuse_this_chart.png)

## Getting started

There are three ways to follow this tutorial:
* [Dev Containers](#dev-containers-recommended) if you have Docker and Visual Studio Code installed
* [GitHub Codespaces](#github-codespaces) if you don't want to install anything on your local machine
* [Local installation](#local-installation) if you are a fan of local development.

We recommend using Dev Containers or GitHub Codespaces to avoid any issues with the environment setup.

### Dev Containers

To use it, you need to have [Docker](https://www.docker.com/) and [Visual Studio Code](https://code.visualstudio.com/) installed.
This project is configured to use [devcontainer](https://code.visualstudio.com/docs/remote/containers) for development.

First, we need to install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.
Then, open the project in VSCode and click on the green button in the bottom right corner of the window.
This will open a new window in a container with all the necessary tools installed.
It could take a few minutes to build the container for the first time.

Once the container is running, you'll see green "Dev Container" badge in the bottom left corner of the VSCode window.
The development environment is ready to use.
Since Docker provides an isolated environment, we don't need to create a virtual environment or install any dependencies on the host machine.

### GitHub Codespaces

If you don't want to install anything on your local machine, you could use [GitHub Codespaces](https://docs.github.com/en/codespaces/overview) throughout this tutorial.
To use it, you need to have a GitHub account and a repository forked to your account.
After that, you could open the repository in GitHub and click on the "Code" button in the top right corner of the page.
Then, select "Open with Codespaces" from the dropdown menu.
It could take a few minutes to create the environment for the first time.

Once the environment is ready, you'll see a new tab in your browser with the VSCode editor.
The development environment is ready to use.

### Local installation MacOS / Linux

If you prefer to use your local machine, you need to have Python 3.12 installed.
Create a virtual environment and install the dependencies:

```shell
$ python3 -m pip venv .venv
$ source .venv/bin/activate
$ make install
```
