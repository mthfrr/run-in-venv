# Run In Venv

## Why ?

I hate to have to remember to enter a venv before running a script.

## Usage

### Import runfromvenv.py

At the beginning of your main python file **AND ONLY THERE**, import `runfromvenv.py`

```py
import run-from-venv

import other-stuff

# do actual work
```

### Paste oneliner

At the beginning of your main python file **AND ONLY THERE**, paste the content
of `minified`

```py
# paste here
exec(__import__...

import other-stuff

# do actual work
```
