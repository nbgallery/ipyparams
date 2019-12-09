# ipyparams

Send parameters/arguments to notebooks via URL query string parameters.

## Examples

If you want to prepopulate parameters like `foo=bar` and `baz=1` in a notebook, you can simply encode them in the URL:

```
https://your.jupyter.server/awsome_notebook.ipynb?foo=bar&baz=1
```

In the notebook, just include the following:

```python
import ipyparams
```

The values are now accessible in the `ipyparams.params` dictionary.

```python
ipyparams.params['foo']  # returns "bar"
ipyparams.params['baz']  # returns "1"
```

### Duplicate parameters

URL query strings can contain multiple parameters with the same name, such as `https://your.jupyter.server/awsome_notebook.ipynb?foo=bar&foo=baz`.  The `ipyparams.params` dictionary only contains the last value for each name, but you can still access all the "raw" parameters using `ipyparams.raw_params` dictionary.

```python
import ipyparams
ipyparams.params['foo']      # returns 'baz'
ipyparams.raw_params['foo']  # returns ['bar', 'baz']
```

### Missing parameters

If you try to access a parameter that does not exist, you will simply get `None` back.

```python
import ipyparams
ipyparams.params['unicorn']      # returns None
ipyparams.raw_params['unicorn']  # returns None
```

### Get the notebook name

```python
import ipyparams
ipyparams.notebook_name  # returns 'awesome_notebook.ipynb'
```

### Get the full, raw URL of the notebook

```python
import ipyparams
ipyparams.raw_url
# returns https://your.jupyter.server/awsome_notebook.ipynb?foo=bar&baz=1
```
