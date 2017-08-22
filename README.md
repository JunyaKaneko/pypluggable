# pypluggable

# Usage

/path/to/plugin/directory/sample.py

```py3
import pluggable.plugin


@pluggable.plugin
class SamplePlugin:
    def say_hello(self):
        return 'hello'
```

/path/to/main/program/main.py

```py3
import pluggable


loader = pluggable.Loader(['/path/to/plugin/directory', ])

sample_plugin = loder.load('SamplePlugin')

print(sample_plugin.say_hello())
```