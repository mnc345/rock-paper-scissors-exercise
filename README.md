# Rock, Paper, Scissors

A one-player game of rock, paper, scissors against a computer.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

  ## Installation

Fork this [remote repository](https://github.com/mnc345/rock-paper-scissors-exercise) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-exercise

Use Anaconda to create and activate a new virtual environment, perhaps called "rock-paper-scissors-exercise":

```sh
conda create -n rock-paper-scissors-exercise python=3.8
conda activate rock-paper-scissors-exercise
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Usage

Run the game script:

```py
python game.py

When prompted, choose a player name.

When prompted, choose rock, paper, scissors.

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

