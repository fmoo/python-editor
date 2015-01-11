`python-editor` is a library that provides the `editor` module for programmatically
interfacing with your system's $EDITOR.

Examples
--------

```python
import editor
commit_msg = editor.edit(contents="# Enter commit message here")
```
Opens an editor, prefilled with the contents, `# Enter commit message here`.
When the editor is closed, returns the contents in variable `commit_msg`.


```python
import editor
editor.edit(file="README.txt")
```
Opens README.txt in an editor.  Changes are saved in place.


How it Works
------------
`editor` first looks for the ${EDITOR} environment variable.  If set, it uses
the value as-is, without fallbacks.

If no $EDITOR is set, editor will search through a list of known editors, and
use the first one that exists on the system.

For example, on Linux, `editor` will look for the following editors in order:

* vim
* emacs
* nano

When calling the `edit()` function, `editor` will open the editor in a subprocess,
inheriting the parent process's stdin, stdout
