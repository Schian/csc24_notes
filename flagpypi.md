# Flagpypi

```text
Our team has developed a Python package to optimize energy distribution and traffic flow in Intellitown. We've rigorously tested it and are confident there are no secrets hidden within the code. But in a city this complex, can you dig deeper and ensure everything is as secure as we believe? The future of the city's infrastructure is in your hands!

python3 import flagpypi

Flag Format:flag{t_th3_fl8g_l00ks_s0meth1ng_w1th_le11ers_an3_ch8r8cters}
```

## Notes

Created a python virtual environment with `python3 -m venv ./.venv` and installed the package with `pip install flagpypi`.

Wrote a script to determine the python version is correct. It was compiled with my current version of python. I'm not 100% sure if the decompilers will work with python3.13, I may have to revert to 3.12

Okay, so I was really bad at taking notes for this one. I went down a rabbit-hole of trying to decompile various `.pyc` files. This was entirelly the wrong tact.

### What was actually required

The flag was 'accidentally published' in one of the package releases. I had to find the correct release.

### Steps taken

- Set up a virtual python environment so I could remove all artefacts when I was complete
- `pip install flagpypi` installs the latest package
  - Iterating through the files used by the python package there is `main.py`
  - `cat main.py` gives an output of the below

```text
def flag():
    return "fake flag"
```

- After investigating the package for a few hours trying to find any hidden data or metadata, I took a look at the release history of the package on PyPI. There were dozens of versions released on the same day.
- I am hoping to find the release with the largest size and see if that one is interesting.
  - I interrogated the PyPI API to get a JSON file with all the metadata for each release.
    - `curl -s https://pypi.org/pypi/flagpypi/json | jq . | flagpypi.json`
  - Using some linux magic we find the largest size
    - `cat flagpypi.json | grep "size" | cut -d':' -f2 | sort -nr | head`
      - `1565,`
    - `cat flagpypi.json | grep -A5 -B5 '"size": 1565'`
      - `"url": "https://files.pythonhosted.org/packages/54/09/221e0253f220ce50bcd8c1459176edd5768ad6660169735a5a56f19bea36/flagpypi-2.2.11-py3-none-any.whl",`
- Navigate to release 2.2.11 and download the `.whl` file.
  - This is a compressed file, just unzip it.
- Look for `main.py` and run the `cat` command.

### `flag{1_h0p3_y0u_foUnD_1t_1n_4n_3ff1c13nt_w4y}`
