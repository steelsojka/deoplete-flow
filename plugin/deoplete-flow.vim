if exists('g:loaded_deoplete_flow')
  finish
endif

let g:loaded_deoplete_flow = 1

let g:deoplete#sources#flow#flow_bin = get(g:, 'deoplete#sources#flow#flow_bin', 'flow') 
