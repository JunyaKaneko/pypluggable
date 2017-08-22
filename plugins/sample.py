import sys
sys.path.append('..')

import pluggable

@pluggable.plugin
class SamplePlugin:
    def say_hello(self):
        return 'hello'
        
