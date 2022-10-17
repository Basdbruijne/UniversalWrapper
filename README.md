# UniversalWrapper
UniversalWrapper is a convenient shell wrapper for python, allowing you to interact with command line interfaces as if they were Python modules. UniversalWrapper now also supports async commands since version 2.0.

Tested on ubuntu only.

# Getting started

```bash
pip install UniversalWrapper
```

# Usage
Imagine you want to call
```bash
$ ls /home --recursive
```
from python. Rather than using `subprocess.check_output`, you can just
```python
from universalwrapper import ls
ls("/home", recursive=True)
```
UniversalWrapper uses a set of simple rules to convert python commands to bash commands. The default conversion rules are:
 - "_" is changed to "-" (see `uw_settings.divider` and `uw_settings.flag_divider`)
 - between classes (the .) a space is added (see `uw_settings.class_divider`)
 - A argument is converted to a string
 - Keyword arguments are converted to flags, if `arg=True`, only the flag is use (no arguments)
   if `arg=False` the flag is removed if it is present in `uw_settings.input_add`
 - Keyword arguments with list repeat the flag: `foo=['bar', 'bar']` calls `--foo bar --foo bar`

Repetitive commands or output modifications can be set `uw_settings`, see advanced usage.

# Examples
## Example: create and delete lxd containers

```python
from universalwrapper import lxc

lxc.launch("ubuntu:20.04", "testcontainer")
# calls $ lxc launch ubuntu:20.04 testcontainer

lxc.delete("testcontainer", force=True)
# calls $ lxc delete testcontainer --force
```

## Example: clone a library

```python
from universalwrapper import git

git.clone("https://github.com/Basdbruijne/UniversalWrapper.git")
# calls $ git clone https://github.com/Basdbruijne/UniversalWrapper.git
```
check git diff files:
```python
diff = git.diff(name_only=True)
# calls $ git diff --name-only
```

Commands can be chained as well (see `uw_settings.class_divider`):
```python
git.remote.rename("origin", "foo")
```

`True` and `False` flags are not forwarded to the cli. Instead `True` will add the flag only (without arguments) and `False` will remove the flag in case it is present elsewhere in the command. The latter can be useful is input overrides are used (see advanced usage). To avoid this behaviour, pass True or False as strings.

## Example: Async pip install

Async is enabled locally if a command stars with `async_`. To enable async globally, use `command.uw_settings.async = True`.

Install pip requirements asynchronously

```python
import asyncio
from universalwrapper import pip

async def install_deps():
    install = await pip.async_install(requirement="requirements.txt")
    # Do other stuff while waiting for the install
    return await install

asyncio.run(install_deps())
```

## Example: send a notification

```python
from universalwrapper import notify_send

notify_send("title", "subtitle", i="face-wink")
# calls $ notify-sed title subtitle -i face-wink
```

The argument `(root=True)` will trigger `sudo ` in the command.

# Advanced usage

The universal wrapper does not have any functions build in that are made for one specific cli. If there are repetitive modifications to commands that need to be made, this can be done by editing the uw_settings:

```python
from universalwrapper import foo

foo.uw_settings
>>
foo.uw_settings.cmd: str # base command
foo.uw_settings.divider: str = '-' # string to replace '_' with in command
foo.uw_settings.class_divider: str = ' ' # string to put between classes
foo.uw_settings.flag_divider: str = '-' # string to replace '_' with in flags
foo.uw_settings.debug: bool = False # if True, don't execute command but just print it
foo.uw_settings.input_add: dict: {str: int, str: int} = {} # {extra command, index where to add it}
foo.uw_settings.input_move: dict: {str: int, str: int} = {} # {extra command, index where to move it to}
foo.uw_settings.input_custom: list[str] # custom command: e.g. "command.reverse()"
foo.uw_settings.output_decode: bool = True, # Decode output to str
foo.uw_settings.output_splitlines: bool = False, # Split output lines into list
foo.uw_settings.output_yaml: bool = False, # Try to parse yaml from output
foo.uw_settings.output_json: bool = False, # Try to parse json from output
foo.uw_settings.output_custom: list[str] # custom command: e.g. "output.reverse()"
foo.uw_settings.enable_async: bool = False, # enable asyncio
```

# Limitations

Not all commands can be called cleanly with UniversalWrapper, for example:
```bash
example --log-level Debug command --flag value separate_value
```
Can only be called with
```python
from uw import example
example("--log-level", "Debug", "command", "--flag", "value", "separate_value")
```
due to the limitation in python that keywords arguments must come after non-keyword arguments.
UniversalWrapper V3 may contain workarounds for this.

