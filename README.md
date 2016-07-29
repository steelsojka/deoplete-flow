# deoplete-flow

A plugin for [deoplete](https://github.com/Shougo/deoplete.nvim) to get flow
autocompletion functionality.

## Installation

Currently only tested with NeoVim and Python3 client.
Check out the deoplete documentation to get the basic setup.

Install this plugin with your favourite plugin manager.

Also make sure to install your `flow-bin` in your project directory:

```
npm install flow-bin
```

## Configuration

```
# Binary path to your flow, defaults to your $PATH flow 
let g:deoplete#sources#flow#flow_bin = 'flow' 
```

**Local vs. global flow-bin**:

Most of the time you will probably want your `flow-bin` installed in your
`node_modules` directory of your current project. This example configuration
will preferably take the local version before the global one:

```
function! StrTrim(txt)
  return substitute(a:txt, '^\n*\s*\(.\{-}\)\n*\s*$', '\1', '')
endfunction

let g:flow_path = StrTrim(system('PATH=$(npm bin):$PATH && which flow'))

if g:flow_path != 'flow not found'
  let g:deoplete#sources#flow#flow_bin = g:flow_path
endif
```
