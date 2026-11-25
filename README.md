# dl-from-scratch-vol1

My study log for **『ゼロから作る Deep Learning』**
(*Deep Learning from Scratch* ❶, O'Reilly Japan, by Koki Saitoh).

I work through the book chapter by chapter, typing and running the code myself
rather than copying it, and add my own notes, experiments, and small variations
along the way. The goal is to understand neural networks from first principles
using NumPy only: perceptrons, backpropagation, optimizers, and CNNs.

This repository covers volume ❶ only. Each later volume of the series gets its
own repository.

## Layout

The layout mirrors the [official sample code](https://github.com/oreilly-japan/deep-learning-from-scratch),
so the book's `sys.path.append(os.pardir)` imports work unchanged:

```
ch02/     # one directory per chapter, two-digit numbers
ch03/
common/   # shared helpers built up in the book (functions.py, layers.py, ...)
dataset/  # data loaders copied from the official code (not typed by hand)
```

- `chMM/` — chapter `MM` (`01`, `02`, ...). Chapter directories are created
  when I start a chapter, not ahead of time.
- `common/` — typed by hand, growing as the book adds to it.
- `dataset/` — `mnist.py` is copied from the official repository. The
  downloaded data (`*.gz`, `mnist.pkl`) is git-ignored and is fetched on the
  first run.
- File names are lowercase `snake_case` describing the content
  (`sigmoid.py`, `three_layer_net.py`) — no hyphens, so files stay importable.

## Progress

Furthest chapter: **ch03**

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Run scripts from inside their chapter directory (the imports resolve `..`
relative to the current directory):

```bash
cd ch03
python mnist.py
```

## Credits and licensing

The code here follows the official sample code published by O'Reilly Japan,
[oreilly-japan/deep-learning-from-scratch](https://github.com/oreilly-japan/deep-learning-from-scratch),
which is released under the MIT License. `dataset/mnist.py` is copied from it
unchanged.

The book text, figures, and explanations are **not** reproduced here — please
buy the book. My own code and notes in this repository are MIT licensed
(see [LICENSE](LICENSE)).
