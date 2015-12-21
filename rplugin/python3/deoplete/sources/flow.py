import subprocess
import json

from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim);

        self.name = 'flow'
        self.mark = '[FL]'

    def gather_candidates(self, context):
        suggestions = []

        line = self.vim.current.cursor[0]
        column = self.vim.current.cursor[1]
        command = ['flow', 'autocompletion', '--json', '--no-auto-start', line, column]

        command_results = subprocess.check_output(command, stdin=self.vim.current.buffer, universal_newlines=True)

        results = json.loads(command_results);

        return [{word: x.name} for x in results.result] 
