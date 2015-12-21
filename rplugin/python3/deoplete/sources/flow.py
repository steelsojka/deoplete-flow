import json
import deoplete.util

from subprocess import Popen, PIPE
from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim);

        self.rank = 600
        self.name = 'flow'
        self.mark = '[FL]'
        self.min_pattern_length = 0
        self.filetypes = ['javascript']

    def get_complete_position(self, context):
        pos = context['input'].rfind('.')
        return pos if pos < 0 else pos + 1

    def gather_candidates(self, context):
        line = str(self.vim.current.window.cursor[0])
        column = str(self.vim.current.window.cursor[1] + 1)
        command = ['flow', 'autocomplete', '--json', '--no-auto-start', line, column]
        buf = '\n'.join(self.vim.current.buffer[:])

        process = Popen(command, stdout=PIPE, stdin=PIPE)
        command_results = process.communicate(input=str.encode(buf))[0]

        if process.returncode != 0:
            return []

        results = json.loads(command_results.decode('utf-8'))

        return [{'word': x['name'], 'kind': x['type']} for x in results['result']] 
