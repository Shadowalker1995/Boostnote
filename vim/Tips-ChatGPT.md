Vim uses its own flavor of regular expressions, which is similar to (but not exactly the same as) other regex implementations you might be familiar with. Here are some common regex elements in Vim:

- `.`: Matches any single character.
- `*`: Matches zero or more of the preceding character.
- `\+`: Matches one or more of the preceding character.
- `\?`: Matches zero or one of the preceding character.
- `\w`: Matches a word character (alphanumeric or underscore).
- `\W`: Matches a non-word character.
- `\s`: Matches a whitespace character (space or tab).
- `\S`: Matches a non-whitespace character.
- `\d`: Matches a digit.
- `\D`: Matches a non-digit.
- `\t`: Matches a tab character.
- `\n`: Matches a newline character.
- `\{n,m}`: Matches the preceding element at least `n` times but no more than `m` times.
- `\{n}`: Matches the preceding element exactly `n` times.
- `\{n,}`: Matches the preceding element at least `n` times.
- `\(` and `\)`: Define a capturing group.
- `\|`: Represents alternation (either the expression before or after the vertical bar).
- `^`: Matches the beginning of a line.
- `$`: Matches the end of a line.
- `\<` and `\>`: Match the beginning and end of a word, respectively.

For example, if you want to search for all occurrences of the word "example" followed by a digit, you can enter the following search in Vim:

```
/example\d
```

---

https://github.com/j1z0/vim-config

https://github.com/voldikss/dotfiles/tree/dev

---

backtick (\`): jump to the precise position (line and column) of a mark

single quote (`'`): jump to the line of a mark, placing the cursor on the first non-blank character of the line

---

```
v  ["          *@:<C-U>exe "normal! gv"|call search('\%(^\s*".*\n\)\%(^\s*"\)\@!', "bW")<CR>
n  ["          *@:call search('\%(^\s*".*\n\)\%(^\s*"\)\@!', "bW")<CR>
v  []          *@m':<C-U>exe "normal! gv"|call search('^\s*end\(f\%[unction]\|def\)\>', "bW")<CR>
n  []          *@m':call search('^\s*end\(f\%[unction]\|def\)\>', "bW")<CR>
v  [[          *@m':<C-U>exe "normal! gv"|call search('^\s*\(fu\%[nction]\|def\)\>', "bW")<CR>
n  [[          *@m':call search('^\s*\(fu\%[nction]\|def\)\>', "bW")<CR>
v  ]"          *@:<C-U>exe "normal! gv"|call search('^\(\s*".*\n\)\@<!\(\s*"\)', "W")<CR>
n  ]"          *@:call search('^\(\s*".*\n\)\@<!\(\s*"\)', "W")<CR>
v  ][          *@m':<C-U>exe "normal! gv"|call search('^\s*end\(f\%[unction]\|def\)\>', "W")<CR>
n  ][          *@m':call search('^\s*end\(f\%[unction]\|def\)\>', "W")<CR>
v  ]]          *@m':<C-U>exe "normal! gv"|call search('^\s*\(fu\%[nction]\|def\)\>', "W")<CR>
n  ]]          *@m':call search('^\s*\(fu\%[nction]\|def\)\>', "W")<CR>
n  <Space>y    * :<C-U>CocList -A --normal yank<CR>
n  <Space>p    * :<C-U>CocListResume<CR>
n  <Space>i    * :<C-U>CocPrev<CR>
n  <Space>k    * :<C-U>CocNext<CR>
n  <Space>s    * :<C-U>CocList -I symbols<CR>
n  <Space>o    * :<C-U>CocList outline<CR>
n  <Space>c    * :<C-U>CocList commands<CR>
n  <Space>e    * :<C-U>CocList extensions<CR>
n  <Space>a    * :<C-U>CocList diagnostics<CR>
n  <Space>ef     :CocCommand explorer --preset floating<CR>
n  <Space>ed     :CocCommand explorer --preset .vim<CR>
n  <Space>r    * :RnvimrToggle<CR>
x  #           * y?\V<C-R>"<CR>
                 Nvim builtin
o  %             <Plug>(MatchitOperationForward)
x  %             <Plug>(MatchitVisualForward)
n  %             <Plug>(MatchitNormalForward)
n  &           * :&&<CR>
                 Nvim builtin
x  *           * y/\V<C-R>"<CR>
                 Nvim builtin
n  ,c            <Plug>(iron-clear)
n  ,q            <Plug>(iron-exit)
n  ,i            <Plug>(iron-interrupt)
n  ,<CR>         <Plug>(iron-cr)
n  ,l            <Plug>(iron-send-line)
n  ,r            <Plug>(iron-repeat-cmd)
v  ,s            <Plug>(iron-visual-send)
n  ,s            <Plug>(iron-send-motion)
   ,fl           :r !figlet -f slant<Space>
v  ;str        * :s/\t/    /g
n  ;str        * :%s/\t/    /g
v  ;st         * :s/    /\t/g
n  ;st         * :%s/    /\t/g
n  ;fd         * /\(\<\w\+\>\)\_s*\1
v  ;<CR>       * :nohl<CR>
no ;<CR>       * :nohl<CR>
n  ;sp         * :CtrlSF<CR>
   ;gy           :Goyo<CR>
v  ;tq         * y:ThesaurusQueryReplace <C-R>"<CR>
n  ;tq         * :ThesaurusQueryReplaceCurrentWord<CR>
n  ;fl           :NERDTreeToggle<CR>
x  ;<C-Space>  * :call UltiSnips#SaveLastVisualSelection()<CR>gvs
s  ;<C-Space>  * <Esc>:call UltiSnips#ExpandSnippetOrJump()<CR>
n  ;ca           <Plug>NERDCommenterAltDelims
x  ;cu           <Plug>NERDCommenterUncomment
n  ;cu           <Plug>NERDCommenterUncomment
x  ;cb           <Plug>NERDCommenterAlignBoth
n  ;cb           <Plug>NERDCommenterAlignBoth
x  ;cl           <Plug>NERDCommenterAlignLeft
n  ;cl           <Plug>NERDCommenterAlignLeft
n  ;cA           <Plug>NERDCommenterAppend
x  ;cy           <Plug>NERDCommenterYank
n  ;cy           <Plug>NERDCommenterYank
x  ;cs           <Plug>NERDCommenterSexy
n  ;cs           <Plug>NERDCommenterSexy
x  ;ci           <Plug>NERDCommenterInvert
n  ;ci           <Plug>NERDCommenterInvert
n  ;c$           <Plug>NERDCommenterToEOL
x  ;cn           <Plug>NERDCommenterNested
n  ;cn           <Plug>NERDCommenterNested
x  ;cm           <Plug>NERDCommenterMinimal
n  ;cm           <Plug>NERDCommenterMinimal
x  ;c<Space>     <Plug>NERDCommenterToggle
n  ;c<Space>     <Plug>NERDCommenterToggle
x  ;cc           <Plug>NERDCommenterComment
n  ;cc           <Plug>NERDCommenterComment
n  ;w;m          <Plug>VimwikiMakeTomorrowDiaryNote
n  ;w;y          <Plug>VimwikiMakeYesterdayDiaryNote
n  ;w;t          <Plug>VimwikiTabMakeDiaryNote
n  ;w;w          <Plug>VimwikiMakeDiaryNote
n  ;w;i          <Plug>VimwikiDiaryGenerateLinks
n  ;wi           <Plug>VimwikiDiaryIndex
n  ;ws           <Plug>VimwikiUISelect
n  ;wt           <Plug>VimwikiTabIndex
n  ;ww           <Plug>VimwikiIndex
x  ;T            <Plug>(table-mode-tableize-delimiter)
x  ;tt           <Plug>(table-mode-tableize)
n  ;tt           <Plug>(table-mode-tableize)
   ;tm           :TableModeToggle<CR>
n  ;ba           <Plug>BufKillAlt
n  ;bundo        <Plug>BufKillUndo
n  ;!bw          <Plug>BufKillBangBw
n  ;bw           <Plug>BufKillBw
n  ;!bd          <Plug>BufKillBangBd
n  ;bd           <Plug>BufKillBd
n  ;!bun         <Plug>BufKillBangBun
n  ;bun          <Plug>BufKillBun
n  ;bf           <Plug>BufKillForward
n  ;bb           <Plug>BufKillBack
nos;T          * :CocList tasks<CR>
n  ;tu         * :CocCommand todolist.download<CR>:CocCommand todolist.upload<CR>
n  ;tl         * :CocList todolist<CR>
n  ;tn         * :CocCommand todolist.create<CR>
n  ;a            :<C-U>set operatorfunc=<SNR>3_cocActionsOpenFromSelected<CR>g@
x  ;a            :<C-U>execute 'CocCommand actions.open ' . visualmode()<CR>
v  ;t            <Plug>(coc-translator-pv)
n  ;t            <Plug>(coc-translator-p)
n  ;rn           <Plug>(coc-rename)
   ;c8           :set background=dark<CR>:let g:SnazzyTransparent=1<CR>:colorscheme snazzy<CR>:AirlineTheme badwolf<CR>
   ;c7           :set background=light<CR>:colorscheme gruvbox<CR>:AirlineTheme badwolf<CR>
   ;c6           :set background=dark<CR>:colorscheme gruvbox<CR>:AirlineTheme badwolf<CR>
   ;c5           :set background=dark<CR>:colorscheme molokai<CR>:AirlineTheme molokai<CR>
   ;c4           :set background=light<CR>:let ayucolor="dark"<CR>:colorscheme ayu<CR>:AirlineTheme ayu_dark<CR>
   ;c3           :set background=light<CR>:let ayucolor="light"<CR>:colorscheme ayu<CR>:AirlineTheme ayu_dark<CR>
   ;c2           :set background=dark<CR>:let ayucolor="mirage"<CR>:colorscheme ayu<CR>:AirlineTheme ayu_dark<CR>
   ;c1           :set background=dark<CR>:let g:SnazzyTransparent=0<CR>:colorscheme snazzy<CR>:AirlineTheme badwolf<CR>
n  ;man          :Man 3 <cword><CR>
   ;sc           :set spell!<CR>
   ;=          * :lne<CR>
   ;-          * :lN<CR>
   ;;            <Plug>(easymotion-prefix)
   ;sr           :%s/
   ;r            :r !
   ;/          * :set splitbelow<CR>:split<CR>:res -3<CR>:term<CR>
   ;sl           :vertical resize+5<CR>
   ;sh           :vertical resize-5<CR>
   ;sj           :res -5<CR>
   ;sk           :res +5<CR>
n  ;Q            :qa!<CR>
n  ;WQ           :wa<CR>:qa<CR>
n  ;w            :w<CR>
n  ;q            :BD<CR>
   ;rc         * :e ~/.config/nvim/init.vim<CR>
n  ;p            "+p
v  ;yy         * "+yy
v  ;y          * "+y
n  <           * <<
v  <           * <gv  " better indentation
n  >           * >>
v  >           * >gv  " better indentation
   B           * 5B
n  F           * :call <SNR>3_show_documentation()<CR>
   H           * ^
   J           * 5j
   K           * 5k
   L           * $
   N           * Nzz
   R             :w<CR>:source $MYVIMRC<CR>
x  S             <Plug>VSurround
   T             :TagbarOpenAutoClose<CR>
n  U             :UndotreeToggle<CR>
   W           * 5W
n  Y           * y$
o  [%            <Plug>(MatchitOperationMultiBackward)
x  [%            <Plug>(MatchitVisualMultiBackward)
n  [%            <Plug>(MatchitNormalMultiBackward)
n  [C            9999[c
n  [c            <Plug>(signify-prev-hunk)
n  [g            <Plug>(coc-diagnostic-prev)
n  [b          * :bfirst<CR>
n  \t          * :tabe<CR>:-tabmove<CR>:term sh -c 'alacritty'<CR><C-\><C-N>:q<CR>
   \           * ;
v  \str        * :s/\t/    /g
n  \str        * :%s/\t/    /g
v  \st         * :s/    /\t/g
n  \st         * :%s/    /\t/g
n  \fd         * /\(\<\w\+\>\)\_s*\1
v  \<CR>       * :nohl<CR>
n  \sp         * :CtrlSF<CR>
   \gy           :Goyo<CR>
v  \tq         * y:ThesaurusQueryReplace <C-R>"<CR>
n  \tq         * :ThesaurusQueryReplaceCurrentWord<CR>
   \tm           :TableModeToggle<CR>
n  \fl           :NERDTreeToggle<CR>
n  \c            <Plug>(iron-clear)
n  \q            <Plug>(iron-exit)
n  \i            <Plug>(iron-interrupt)
no \<CR>       * :nohl<CR>
n  \l            <Plug>(iron-send-line)
n  \r            <Plug>(iron-repeat-cmd)
v  \s          * :s//g<Left><Left>
n  \s          * :%s//g<Left><Left>
o  ]%            <Plug>(MatchitOperationMultiForward)
x  ]%            <Plug>(MatchitVisualMultiForward)
n  ]%            <Plug>(MatchitNormalMultiForward)
n  ]C            9999]c
n  ]c            <Plug>(signify-next-hunk)
n  ]g            <Plug>(coc-diagnostic-next)
n  ]b          * :blast<CR>
n  `p          * :<C-U>call signature#marker#Goto("prev", "same", v:count)<CR>
n  `n          * :<C-U>call signature#marker#Goto("next", "same", v:count)<CR>
x  a%            <Plug>(MatchitVisualTextObject)
o  ac            <Plug>(coc-classobj-a)
x  ac            <Plug>(coc-classobj-a)
o  af            <Plug>(coc-funcobj-a)
x  af            <Plug>(coc-funcobj-a)
n  cS            <Plug>CSurround
n  cs            <Plug>Csurround
n  ds            <Plug>Dsurround
n  dm          * :<C-U>call signature#utils#Remove(v:count)<CR>
n  dm?         * :<C-U>call signature#marker#Purge()<CR>
n  dm/         * :<C-U>call signature#mark#Purge("all")<CR>
n  ff            :CocCommand explorer<CR>
x  gx            <Plug>NetrwBrowseXVis
n  gx            <Plug>NetrwBrowseX
o  g%            <Plug>(MatchitOperationBackward)
x  g%            <Plug>(MatchitVisualBackward)
n  g%            <Plug>(MatchitNormalBackward)
x  gS            <Plug>VgSurround
n  gr            <Plug>(coc-references)
n  gi            <Plug>(coc-implementation)
n  gy            <Plug>(coc-type-definition)
n  gd            <Plug>(coc-definition)
n  m?          * :<C-U>call signature#marker#List(v:count, 0)<CR>
n  m/          * :<C-U>call signature#mark#List(0, 0)<CR>
n  m[          * :<C-U>call signature#marker#Goto("prev", "any",  v:count)<CR>
n  m]          * :<C-U>call signature#marker#Goto("next", "any",  v:count)<CR>
n  mp          * :<C-U>call signature#mark#Goto("prev", "spot", "pos")<CR>
n  mn          * :<C-U>call signature#mark#Goto("next", "spot", "pos")<CR>
n  m;          * :<C-U>call signature#mark#Goto("next", "line", "alpha")<CR>
n  m-          * :<C-U>call signature#mark#Purge("line")<CR>
n  m.          * :<C-U>call signature#mark#ToggleAtLine()<CR>
n  m,          * :<C-U>call signature#mark#Toggle("next")<CR>
n  m           * :<C-U>call signature#utils#Input()<CR>
o  nc            <Plug>(coc-classobj-i)
x  nc            <Plug>(coc-classobj-i)
o  nf            <Plug>(coc-funcobj-i)
x  nf            <Plug>(coc-funcobj-i)
   n           * nzz
v  p           * pgvy
   q;            q:
   sr\         * <C-W>b<C-W>H
   sr-         * <C-W>b<C-W>K
   s\            <C-W>t<C-W>H
   s-            <C-W>t<C-W>K
   sd          * :close<CR>
   sw          * <C-W><C-W>
   sj            :set splitbelow<CR>:split<CR>
   sk            :set nosplitbelow<CR>:split<CR>
   sh            :set nosplitright<CR>:vsplit<CR>
   sl            :set splitright<CR>:vsplit<CR>
   s             <Nop>
n  ss            <Plug>(easymotion-s2)
n  tml         * :+tabmove<CR>
n  tmh         * :-tabmove<CR>
n  td          * :tabclose<CR>
n  tl          * :tabnext<CR>
n  th          * :tabprevious<CR>
   tn          * :tabe<CR>
n  ySS           <Plug>YSsurround
n  ySs           <Plug>YSsurround
n  yss           <Plug>Yssurround
n  yS            <Plug>YSurround
n  ys            <Plug>Ysurround
n  y<C-G>      & :<C-U>call setreg(v:register, fugitive#Object(@%))<CR>
v  <Plug>(coc-explorer-key-v->>) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v->>'])<CR>
v  <Plug>(coc-explorer-key-v-<<) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-<<'])<CR>
v  <Plug>(coc-explorer-key-v-]c) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-]c'])<CR>
v  <Plug>(coc-explorer-key-v-[c) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-[c'])<CR>
v  <Plug>(coc-explorer-key-v-]d) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-]d'])<CR>
v  <Plug>(coc-explorer-key-v-[d) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-[d'])<CR>
v  <Plug>(coc-explorer-key-v-]]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-]]'])<CR>
v  <Plug>(coc-explorer-key-v-[[) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-[['])<CR>
v  <Plug>(coc-explorer-key-v-b) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-b'])<CR>
v  <Plug>(coc-explorer-key-v-B) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-B'])<CR>
v  <Plug>(coc-explorer-key-v-F) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-F'])<CR>
v  <Plug>(coc-explorer-key-v-f) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-f'])<CR>
v  <Plug>(coc-explorer-key-v-gd) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-gd'])<CR>
v  <Plug>(coc-explorer-key-v-X) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-X'])<CR>
v  <Plug>(coc-explorer-key-v-q) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-q'])<CR>
v  <Plug>(coc-explorer-key-v-?) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-?'])<CR>
v  <Plug>(coc-explorer-key-v-R) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-R'])<CR>
v  <Plug>(coc-explorer-key-v-zh) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-zh'])<CR>
v  <Plug>(coc-explorer-key-v-.) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-.'])<CR>
v  <Plug>(coc-explorer-key-v-r) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-r'])<CR>
v  <Plug>(coc-explorer-key-v-A) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-A'])<CR>
v  <Plug>(coc-explorer-key-v-a) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-a'])<CR>
v  <Plug>(coc-explorer-key-v-DD) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-DD'])<CR>
v  <Plug>(coc-explorer-key-v-dD) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-dD'])<CR>
v  <Plug>(coc-explorer-key-v-pp) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-pp'])<CR>
v  <Plug>(coc-explorer-key-v-dd) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-dd'])<CR>
v  <Plug>(coc-explorer-key-v-yy) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-yy'])<CR>
v  <Plug>(coc-explorer-key-v-yn) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-yn'])<CR>
v  <Plug>(coc-explorer-key-v-yp) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-yp'])<CR>
v  <Plug>(coc-explorer-key-v-u) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-u'])<CR>
v  <Plug>(coc-explorer-key-v-[bs]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-[bs]'])<CR>
v  <Plug>(coc-explorer-key-v-[cr]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-[cr]'])<CR>
v  <Plug>(coc-explorer-key-v-E) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-E'])<CR>
v  <Plug>(coc-explorer-key-v-L) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-L'])<CR>
v  <Plug>(coc-explorer-key-v-t) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-t'])<CR>
v  <Plug>(coc-explorer-key-v-l) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-l'])<CR>
v  <Plug>(coc-explorer-key-v-e) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-e'])<CR>
v  <Plug>(coc-explorer-key-v-gj) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-gj'])<CR>
v  <Plug>(coc-explorer-key-v-gl) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-gl'])<CR>
v  <Plug>(coc-explorer-key-v-gk) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-gk'])<CR>
v  <Plug>(coc-explorer-key-v-gi) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-gi'])<CR>
v  <Plug>(coc-explorer-key-v-h) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-h'])<CR>
v  <Plug>(coc-explorer-key-v-i) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-i'])<CR>
v  <Plug>(coc-explorer-key-v-[esc]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-[esc]'])<CR>
v  <Plug>(coc-explorer-key-v-I) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-I'])<CR>
v  <Plug>(coc-explorer-key-v-K) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-K'])<CR>
v  <Plug>(coc-explorer-key-v-*) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-*'])<CR>
v  <Plug>(coc-explorer-key-v-[tab]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-[tab]'])<CR>
v  <Plug>(coc-explorer-key-v-gp) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-v-gp'])<CR>
n  <Plug>(coc-explorer-key-n->>) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n->>'])<CR>
n  <Plug>(coc-explorer-key-n-<<) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-<<'])<CR>
n  <Plug>(coc-explorer-key-n-]c) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-]c'])<CR>
n  <Plug>(coc-explorer-key-n-[c) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-[c'])<CR>
n  <Plug>(coc-explorer-key-n-]d) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-]d'])<CR>
n  <Plug>(coc-explorer-key-n-[d) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-[d'])<CR>
n  <Plug>(coc-explorer-key-n-]]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-]]'])<CR>
n  <Plug>(coc-explorer-key-n-[[) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-[['])<CR>
n  <Plug>(coc-explorer-key-n-b) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-b'])<CR>
n  <Plug>(coc-explorer-key-n-B) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-B'])<CR>
n  <Plug>(coc-explorer-key-n-F) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-F'])<CR>
n  <Plug>(coc-explorer-key-n-f) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-f'])<CR>
n  <Plug>(coc-explorer-key-n-gd) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-gd'])<CR>
n  <Plug>(coc-explorer-key-n-X) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-X'])<CR>
n  <Plug>(coc-explorer-key-n-q) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-q'])<CR>
n  <Plug>(coc-explorer-key-n-?) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-?'])<CR>
n  <Plug>(coc-explorer-key-n-R) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-R'])<CR>
n  <Plug>(coc-explorer-key-n-zh) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-zh'])<CR>
n  <Plug>(coc-explorer-key-n-.) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-.'])<CR>
n  <Plug>(coc-explorer-key-n-r) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-r'])<CR>
n  <Plug>(coc-explorer-key-n-A) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-A'])<CR>
n  <Plug>(coc-explorer-key-n-a) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-a'])<CR>
n  <Plug>(coc-explorer-key-n-DD) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-DD'])<CR>
n  <Plug>(coc-explorer-key-n-dD) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-dD'])<CR>
n  <Plug>(coc-explorer-key-n-pp) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-pp'])<CR>
n  <Plug>(coc-explorer-key-n-dd) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-dd'])<CR>
n  <Plug>(coc-explorer-key-n-yy) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-yy'])<CR>
n  <Plug>(coc-explorer-key-n-yn) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-yn'])<CR>
n  <Plug>(coc-explorer-key-n-yp) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-yp'])<CR>
n  <Plug>(coc-explorer-key-n-u) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-u'])<CR>
n  <Plug>(coc-explorer-key-n-[bs]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-[bs]'])<CR>
n  <Plug>(coc-explorer-key-n-o) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-o'])<CR>
n  <Plug>(coc-explorer-key-n-[cr]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-[cr]'])<CR>
n  <Plug>(coc-explorer-key-n-E) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-E'])<CR>
n  <Plug>(coc-explorer-key-n-L) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-L'])<CR>
n  <Plug>(coc-explorer-key-n-t) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-t'])<CR>
n  <Plug>(coc-explorer-key-n-l) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-l'])<CR>
n  <Plug>(coc-explorer-key-n-e) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-e'])<CR>
n  <Plug>(coc-explorer-key-n-gj) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-gj'])<CR>
n  <Plug>(coc-explorer-key-n-gl) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-gl'])<CR>
n  <Plug>(coc-explorer-key-n-gk) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-gk'])<CR>
n  <Plug>(coc-explorer-key-n-gi) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-gi'])<CR>
n  <Plug>(coc-explorer-key-n-j) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-j'])<CR>
n  <Plug>(coc-explorer-key-n-h) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-h'])<CR>
n  <Plug>(coc-explorer-key-n-k) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-k'])<CR>
n  <Plug>(coc-explorer-key-n-i) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-i'])<CR>
n  <Plug>(coc-explorer-key-n-[esc]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-[esc]'])<CR>
n  <Plug>(coc-explorer-key-n-I) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-I'])<CR>
n  <Plug>(coc-explorer-key-n-K) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-K'])<CR>
n  <Plug>(coc-explorer-key-n-*) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-*'])<CR>
n  <Plug>(coc-explorer-key-n-[tab]) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-[tab]'])<CR>
n  <Plug>(coc-explorer-key-n-gp) * :<C-U>call coc#rpc#request('doKeymap', ['explorer-key-n-gp'])<CR>
x  <Plug>(coc-git-chunk-outer) * :<C-U>call coc#rpc#request('doKeymap', ['git-chunk-outer'])<CR>
o  <Plug>(coc-git-chunk-outer) * :<C-U>call coc#rpc#request('doKeymap', ['git-chunk-outer'])<CR>
x  <Plug>(coc-git-chunk-inner) * :<C-U>call coc#rpc#request('doKeymap', ['git-chunk-inner'])<CR>
o  <Plug>(coc-git-chunk-inner) * :<C-U>call coc#rpc#request('doKeymap', ['git-chunk-inner'])<CR>
n  <Plug>(coc-git-showblamedoc) * :<C-U>call coc#rpc#notify('doKeymap', ['git-showblamedoc'])<CR>
n  <Plug>(coc-git-commit) * :<C-U>call coc#rpc#notify('doKeymap', ['git-commit'])<CR>
n  <Plug>(coc-git-chunkinfo) * :<C-U>call coc#rpc#notify('doKeymap', ['git-chunkinfo'])<CR>
n  <Plug>(coc-git-keepboth) * :<C-U>call coc#rpc#notify('doKeymap', ['git-keepboth'])<CR>
n  <Plug>(coc-git-keepincoming) * :<C-U>call coc#rpc#notify('doKeymap', ['git-keepincoming'])<CR>
n  <Plug>(coc-git-keepcurrent) * :<C-U>call coc#rpc#notify('doKeymap', ['git-keepcurrent'])<CR>
n  <Plug>(coc-git-prevconflict) * :<C-U>call coc#rpc#notify('doKeymap', ['git-prevconflict'])<CR>
n  <Plug>(coc-git-nextconflict) * :<C-U>call coc#rpc#notify('doKeymap', ['git-nextconflict'])<CR>
n  <Plug>(coc-git-prevchunk) * :<C-U>call coc#rpc#notify('doKeymap', ['git-prevchunk'])<CR>
n  <Plug>(coc-git-nextchunk) * :<C-U>call coc#rpc#notify('doKeymap', ['git-nextchunk'])<CR>
v  <Plug>(coc-translator-rv) * :<C-U>call coc#rpc#notify('doKeymap', ['translator-rv'])<CR>
n  <Plug>(coc-translator-r) * :<C-U>call coc#rpc#notify('doKeymap', ['translator-r'])<CR>
v  <Plug>(coc-translator-ev) * :<C-U>call coc#rpc#notify('doKeymap', ['translator-ev'])<CR>
n  <Plug>(coc-translator-e) * :<C-U>call coc#rpc#notify('doKeymap', ['translator-e'])<CR>
v  <Plug>(coc-translator-pv) * :<C-U>call coc#rpc#notify('doKeymap', ['translator-pv'])<CR>
n  <Plug>(coc-translator-p) * :<C-U>call coc#rpc#notify('doKeymap', ['translator-p'])<CR>
v  <Plug>(coc-snippets-select) * :<C-U>call coc#rpc#notify('doKeymap', ['snippets-select'])<CR>
x  <Plug>(coc-convert-snippet) * :<C-U>call coc#rpc#notify('doKeymap', ['convert-snippet'])<CR>
n  <SNR>163_:  * :<C-U><C-R>=v:count ? v:count : ''<CR>
   <Plug>AirlineSelectNextTab * :<C-U>call <SNR>143_jump_to_tab(v:count1)<CR>
   <Plug>AirlineSelectPrevTab * :<C-U>call <SNR>143_jump_to_tab(-v:count1)<CR>
   <Plug>AirlineSelectTab0 * :call <SNR>143_select_tab(9)<CR>
   <Plug>AirlineSelectTab9 * :call <SNR>143_select_tab(8)<CR>
   <Plug>AirlineSelectTab8 * :call <SNR>143_select_tab(7)<CR>
   <Plug>AirlineSelectTab7 * :call <SNR>143_select_tab(6)<CR>
   <Plug>AirlineSelectTab6 * :call <SNR>143_select_tab(5)<CR>
   <Plug>AirlineSelectTab5 * :call <SNR>143_select_tab(4)<CR>
   <Plug>AirlineSelectTab4 * :call <SNR>143_select_tab(3)<CR>
   <Plug>AirlineSelectTab3 * :call <SNR>143_select_tab(2)<CR>
   <Plug>AirlineSelectTab2 * :call <SNR>143_select_tab(1)<CR>
   <Plug>AirlineSelectTab1 * :call <SNR>143_select_tab(0)<CR>
x  <Plug>NetrwBrowseXVis * :<C-U>call netrw#BrowseXVis()<CR>
n  <Plug>NetrwBrowseX * :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))<CR>
x  <Plug>(MatchitVisualTextObject)   <Plug>(MatchitVisualMultiBackward)o<Plug>(MatchitVisualMultiForward)
o  <Plug>(MatchitOperationMultiForward) * :<C-U>call matchit#MultiMatch("W",  "o")<CR>
o  <Plug>(MatchitOperationMultiBackward) * :<C-U>call matchit#MultiMatch("bW", "o")<CR>
x  <Plug>(MatchitVisualMultiForward) * :<C-U>call matchit#MultiMatch("W",  "n")<CR>m'gv``
x  <Plug>(MatchitVisualMultiBackward) * :<C-U>call matchit#MultiMatch("bW", "n")<CR>m'gv``
n  <Plug>(MatchitNormalMultiForward) * :<C-U>call matchit#MultiMatch("W",  "n")<CR>
n  <Plug>(MatchitNormalMultiBackward) * :<C-U>call matchit#MultiMatch("bW", "n")<CR>
o  <Plug>(MatchitOperationBackward) * :<C-U>call matchit#Match_wrapper('',0,'o')<CR>
o  <Plug>(MatchitOperationForward) * :<C-U>call matchit#Match_wrapper('',1,'o')<CR>
x  <Plug>(MatchitVisualBackward) * :<C-U>call matchit#Match_wrapper('',0,'v')<CR>m'gv``
x  <Plug>(MatchitVisualForward) * :<C-U>call matchit#Match_wrapper('',1,'v')<CR>:if col("''") != col("$") | exe ":normal! m'" | endif<CR>gv``
n  <Plug>(MatchitNormalBackward) * :<C-U>call matchit#Match_wrapper('',0,'n')<CR>
n  <Plug>(MatchitNormalForward) * :<C-U>call matchit#Match_wrapper('',1,'n')<CR>
o  <Plug>(coc-classobj-a) * :<C-U>call CocAction('selectSymbolRange', v:false, '', ['Interface', 'Struct', 'Class'])<CR>
o  <Plug>(coc-classobj-i) * :<C-U>call CocAction('selectSymbolRange', v:true, '', ['Interface', 'Struct', 'Class'])<CR>
v  <Plug>(coc-classobj-a) * :<C-U>call CocAction('selectSymbolRange', v:false, visualmode(), ['Interface', 'Struct', 'Class'])<CR>
v  <Plug>(coc-classobj-i) * :<C-U>call CocAction('selectSymbolRange', v:true, visualmode(), ['Interface', 'Struct', 'Class'])<CR>
o  <Plug>(coc-funcobj-a) * :<C-U>call CocAction('selectSymbolRange', v:false, '', ['Method', 'Function'])<CR>
o  <Plug>(coc-funcobj-i) * :<C-U>call CocAction('selectSymbolRange', v:true, '', ['Method', 'Function'])<CR>
v  <Plug>(coc-funcobj-a) * :<C-U>call CocAction('selectSymbolRange', v:false, visualmode(), ['Method', 'Function'])<CR>
v  <Plug>(coc-funcobj-i) * :<C-U>call CocAction('selectSymbolRange', v:true, visualmode(), ['Method', 'Function'])<CR>
n  <Plug>(coc-cursors-position) * :<C-U>call CocAction('cursorsSelect', bufnr('%'), 'position', 'n')<CR>
n  <Plug>(coc-cursors-word) * :<C-U>call CocAction('cursorsSelect', bufnr('%'), 'word', 'n')<CR>
v  <Plug>(coc-cursors-range) * :<C-U>call CocAction('cursorsSelect', bufnr('%'), 'range', visualmode())<CR>
n  <Plug>(coc-cursors-operator) * :<C-U>set operatorfunc=<SNR>88_CursorRangeFromSelected<CR>g@
n  <Plug>(coc-refactor) * :<C-U>call       CocActionAsync('refactor')<CR>
n  <Plug>(coc-command-repeat) * :<C-U>call       CocAction('repeatCommand')<CR>
n  <Plug>(coc-float-jump) * :<C-U>call       coc#float#jump()<CR>
n  <Plug>(coc-float-hide) * :<C-U>call       coc#float#close_all()<CR>
n  <Plug>(coc-fix-current) * :<C-U>call       CocActionAsync('doQuickfix')<CR>
n  <Plug>(coc-openlink) * :<C-U>call       CocActionAsync('openLink')<CR>
n  <Plug>(coc-references-used) * :<C-U>call       CocActionAsync('jumpUsed')<CR>
n  <Plug>(coc-references) * :<C-U>call       CocActionAsync('jumpReferences')<CR>
n  <Plug>(coc-type-definition) * :<C-U>call       CocActionAsync('jumpTypeDefinition')<CR>
n  <Plug>(coc-implementation) * :<C-U>call       CocActionAsync('jumpImplementation')<CR>
n  <Plug>(coc-declaration) * :<C-U>call       CocActionAsync('jumpDeclaration')<CR>
n  <Plug>(coc-definition) * :<C-U>call       CocActionAsync('jumpDefinition')<CR>
n  <Plug>(coc-diagnostic-prev-error) * :<C-U>call       CocActionAsync('diagnosticPrevious', 'error')<CR>
n  <Plug>(coc-diagnostic-next-error) * :<C-U>call       CocActionAsync('diagnosticNext',     'error')<CR>
n  <Plug>(coc-diagnostic-prev) * :<C-U>call       CocActionAsync('diagnosticPrevious')<CR>
n  <Plug>(coc-diagnostic-next) * :<C-U>call       CocActionAsync('diagnosticNext')<CR>
n  <Plug>(coc-diagnostic-info) * :<C-U>call       CocActionAsync('diagnosticInfo')<CR>
n  <Plug>(coc-format) * :<C-U>call       CocActionAsync('format')<CR>
n  <Plug>(coc-format-selected) * :<C-U>set        operatorfunc=<SNR>88_FormatFromSelected<CR>g@
n  <Plug>(coc-rename) * :<C-U>call       CocActionAsync('rename')<CR>
n  <Plug>(coc-codeaction-cursor) * :<C-U>call       CocActionAsync('codeAction',         'cursor')<CR>
n  <Plug>(coc-codeaction-line) * :<C-U>call       CocActionAsync('codeAction',         'line')<CR>
n  <Plug>(coc-codeaction) * :<C-U>call       CocActionAsync('codeAction',         '')<CR>
n  <Plug>(coc-codeaction-selected) * :<C-U>set        operatorfunc=<SNR>88_CodeActionFromSelected<CR>g@
v  <Plug>(coc-codeaction-selected) * :<C-U>call       CocActionAsync('codeAction',         visualmode())<CR>
v  <Plug>(coc-format-selected) * :<C-U>call       CocActionAsync('formatSelected',     visualmode())<CR>
n  <Plug>(coc-codelens-action) * :<C-U>call       CocActionAsync('codeLensAction')<CR>
n  <Plug>(coc-range-select) * :<C-U>call       CocActionAsync('rangeSelect',     '', v:true)<CR>
v  <Plug>(coc-range-select-backward) * :<C-U>call       CocActionAsync('rangeSelect',     visualmode(), v:false)<CR>
v  <Plug>(coc-range-select) * :<C-U>call       CocActionAsync('rangeSelect',     visualmode(), v:true)<CR>
   <Plug>(easymotion-prefix)N   <Plug>(easymotion-N)
   <Plug>(easymotion-prefix)n   <Plug>(easymotion-n)
   <Plug>(easymotion-prefix)k   <Plug>(easymotion-k)
   <Plug>(easymotion-prefix)j   <Plug>(easymotion-j)
   <Plug>(easymotion-prefix)gE   <Plug>(easymotion-gE)
   <Plug>(easymotion-prefix)ge   <Plug>(easymotion-ge)
   <Plug>(easymotion-prefix)E   <Plug>(easymotion-E)
   <Plug>(easymotion-prefix)e   <Plug>(easymotion-e)
   <Plug>(easymotion-prefix)B   <Plug>(easymotion-B)
   <Plug>(easymotion-prefix)b   <Plug>(easymotion-b)
   <Plug>(easymotion-prefix)W   <Plug>(easymotion-W)
   <Plug>(easymotion-prefix)w   <Plug>(easymotion-w)
   <Plug>(easymotion-prefix)T   <Plug>(easymotion-T)
   <Plug>(easymotion-prefix)t   <Plug>(easymotion-t)
   <Plug>(easymotion-prefix)s   <Plug>(easymotion-s)
   <Plug>(easymotion-prefix)F   <Plug>(easymotion-F)
   <Plug>(easymotion-prefix)f   <Plug>(easymotion-f)
x  <Plug>(easymotion-activate) * :<C-U>call EasyMotion#activate(1)<CR>
nos<Plug>(easymotion-activate) * :<C-U>call EasyMotion#activate(0)<CR>
   <Plug>(easymotion-dotrepeat) * :<C-U>call EasyMotion#DotRepeat()<CR>
x  <Plug>(easymotion-repeat) * <Esc>:<C-U>call EasyMotion#Repeat(1)<CR>
nos<Plug>(easymotion-repeat) * :<C-U>call EasyMotion#Repeat(0)<CR>
x  <Plug>(easymotion-prev) * :<C-U>call EasyMotion#NextPrevious(1,1)<CR>
nos<Plug>(easymotion-prev) * :<C-U>call EasyMotion#NextPrevious(0,1)<CR>
x  <Plug>(easymotion-next) * :<C-U>call EasyMotion#NextPrevious(1,0)<CR>
nos<Plug>(easymotion-next) * :<C-U>call EasyMotion#NextPrevious(0,0)<CR>
x  <Plug>(easymotion-wl) * <Esc>:<C-U>call EasyMotion#WBL(1,0)<CR>
nos<Plug>(easymotion-wl) * :<C-U>call EasyMotion#WBL(0,0)<CR>
x  <Plug>(easymotion-lineforward) * <Esc>:<C-U>call EasyMotion#LineAnywhere(1,0)<CR>
nos<Plug>(easymotion-lineforward) * :<C-U>call EasyMotion#LineAnywhere(0,0)<CR>
x  <Plug>(easymotion-lineanywhere) * <Esc>:<C-U>call EasyMotion#LineAnywhere(1,2)<CR>
nos<Plug>(easymotion-lineanywhere) * :<C-U>call EasyMotion#LineAnywhere(0,2)<CR>
x  <Plug>(easymotion-bd-wl) * <Esc>:<C-U>call EasyMotion#WBL(1,2)<CR>
nos<Plug>(easymotion-bd-wl) * :<C-U>call EasyMotion#WBL(0,2)<CR>
x  <Plug>(easymotion-linebackward) * <Esc>:<C-U>call EasyMotion#LineAnywhere(1,1)<CR>
nos<Plug>(easymotion-linebackward) * :<C-U>call EasyMotion#LineAnywhere(0,1)<CR>
x  <Plug>(easymotion-bl) * <Esc>:<C-U>call EasyMotion#WBL(1,1)<CR>
nos<Plug>(easymotion-bl) * :<C-U>call EasyMotion#WBL(0,1)<CR>
x  <Plug>(easymotion-el) * <Esc>:<C-U>call EasyMotion#EL(1,0)<CR>
nos<Plug>(easymotion-el) * :<C-U>call EasyMotion#EL(0,0)<CR>
x  <Plug>(easymotion-gel) * <Esc>:<C-U>call EasyMotion#EL(1,1)<CR>
nos<Plug>(easymotion-gel) * :<C-U>call EasyMotion#EL(0,1)<CR>
x  <Plug>(easymotion-bd-el) * <Esc>:<C-U>call EasyMotion#EL(1,2)<CR>
nos<Plug>(easymotion-bd-el) * :<C-U>call EasyMotion#EL(0,2)<CR>
x  <Plug>(easymotion-jumptoanywhere) * <Esc>:<C-U>call EasyMotion#JumpToAnywhere(1,2)<CR>
nos<Plug>(easymotion-jumptoanywhere) * :<C-U>call EasyMotion#JumpToAnywhere(0,2)<CR>
x  <Plug>(easymotion-vim-n) * <Esc>:<C-U>call EasyMotion#Search(1,0,1)<CR>
nos<Plug>(easymotion-vim-n) * :<C-U>call EasyMotion#Search(0,0,1)<CR>
x  <Plug>(easymotion-n) * <Esc>:<C-U>call EasyMotion#Search(1,0,0)<CR>
nos<Plug>(easymotion-n) * :<C-U>call EasyMotion#Search(0,0,0)<CR>
x  <Plug>(easymotion-bd-n) * <Esc>:<C-U>call EasyMotion#Search(1,2,0)<CR>
nos<Plug>(easymotion-bd-n) * :<C-U>call EasyMotion#Search(0,2,0)<CR>
x  <Plug>(easymotion-bd-n) * <Esc>:<C-U>call EasyMotion#Search(1,2,0)<CR>
nos<Plug>(easymotion-bd-n) * :<C-U>call EasyMotion#Search(0,2,0)<CR>
x  <Plug>(easymotion-vim-N) * <Esc>:<C-U>call EasyMotion#Search(1,1,1)<CR>
nos<Plug>(easymotion-vim-N) * :<C-U>call EasyMotion#Search(0,1,1)<CR>
x  <Plug>(easymotion-N) * <Esc>:<C-U>call EasyMotion#Search(1,1,0)<CR>
nos<Plug>(easymotion-N) * :<C-U>call EasyMotion#Search(0,1,0)<CR>
x  <Plug>(easymotion-eol-j) * <Esc>:<C-U>call EasyMotion#Eol(1,0)<CR>
nos<Plug>(easymotion-eol-j) * :<C-U>call EasyMotion#Eol(0,0)<CR>
x  <Plug>(easymotion-sol-k) * <Esc>:<C-U>call EasyMotion#Sol(1,1)<CR>
nos<Plug>(easymotion-sol-k) * :<C-U>call EasyMotion#Sol(0,1)<CR>
x  <Plug>(easymotion-sol-j) * <Esc>:<C-U>call EasyMotion#Sol(1,0)<CR>
nos<Plug>(easymotion-sol-j) * :<C-U>call EasyMotion#Sol(0,0)<CR>
x  <Plug>(easymotion-k) * <Esc>:<C-U>call EasyMotion#JK(1,1)<CR>
nos<Plug>(easymotion-k) * :<C-U>call EasyMotion#JK(0,1)<CR>
x  <Plug>(easymotion-j) * <Esc>:<C-U>call EasyMotion#JK(1,0)<CR>
nos<Plug>(easymotion-j) * :<C-U>call EasyMotion#JK(0,0)<CR>
x  <Plug>(easymotion-bd-jk) * <Esc>:<C-U>call EasyMotion#JK(1,2)<CR>
nos<Plug>(easymotion-bd-jk) * :<C-U>call EasyMotion#JK(0,2)<CR>
x  <Plug>(easymotion-eol-bd-jk) * <Esc>:<C-U>call EasyMotion#Eol(1,2)<CR>
nos<Plug>(easymotion-eol-bd-jk) * :<C-U>call EasyMotion#Eol(0,2)<CR>
x  <Plug>(easymotion-sol-bd-jk) * <Esc>:<C-U>call EasyMotion#Sol(1,2)<CR>
nos<Plug>(easymotion-sol-bd-jk) * :<C-U>call EasyMotion#Sol(0,2)<CR>
x  <Plug>(easymotion-eol-k) * <Esc>:<C-U>call EasyMotion#Eol(1,1)<CR>
nos<Plug>(easymotion-eol-k) * :<C-U>call EasyMotion#Eol(0,1)<CR>
x  <Plug>(easymotion-iskeyword-ge) * <Esc>:<C-U>call EasyMotion#EK(1,1)<CR>
nos<Plug>(easymotion-iskeyword-ge) * :<C-U>call EasyMotion#EK(0,1)<CR>
x  <Plug>(easymotion-w) * <Esc>:<C-U>call EasyMotion#WB(1,0)<CR>
nos<Plug>(easymotion-w) * :<C-U>call EasyMotion#WB(0,0)<CR>
x  <Plug>(easymotion-bd-W) * <Esc>:<C-U>call EasyMotion#WBW(1,2)<CR>
nos<Plug>(easymotion-bd-W) * :<C-U>call EasyMotion#WBW(0,2)<CR>
x  <Plug>(easymotion-iskeyword-w) * <Esc>:<C-U>call EasyMotion#WBK(1,0)<CR>
nos<Plug>(easymotion-iskeyword-w) * :<C-U>call EasyMotion#WBK(0,0)<CR>
x  <Plug>(easymotion-gE) * <Esc>:<C-U>call EasyMotion#EW(1,1)<CR>
nos<Plug>(easymotion-gE) * :<C-U>call EasyMotion#EW(0,1)<CR>
x  <Plug>(easymotion-e) * <Esc>:<C-U>call EasyMotion#E(1,0)<CR>
nos<Plug>(easymotion-e) * :<C-U>call EasyMotion#E(0,0)<CR>
x  <Plug>(easymotion-bd-E) * <Esc>:<C-U>call EasyMotion#EW(1,2)<CR>
nos<Plug>(easymotion-bd-E) * :<C-U>call EasyMotion#EW(0,2)<CR>
x  <Plug>(easymotion-iskeyword-e) * <Esc>:<C-U>call EasyMotion#EK(1,0)<CR>
nos<Plug>(easymotion-iskeyword-e) * :<C-U>call EasyMotion#EK(0,0)<CR>
x  <Plug>(easymotion-b) * <Esc>:<C-U>call EasyMotion#WB(1,1)<CR>
nos<Plug>(easymotion-b) * :<C-U>call EasyMotion#WB(0,1)<CR>
x  <Plug>(easymotion-iskeyword-b) * <Esc>:<C-U>call EasyMotion#WBK(1,1)<CR>
nos<Plug>(easymotion-iskeyword-b) * :<C-U>call EasyMotion#WBK(0,1)<CR>
x  <Plug>(easymotion-iskeyword-bd-w) * <Esc>:<C-U>call EasyMotion#WBK(1,2)<CR>
nos<Plug>(easymotion-iskeyword-bd-w) * :<C-U>call EasyMotion#WBK(0,2)<CR>
x  <Plug>(easymotion-W) * <Esc>:<C-U>call EasyMotion#WBW(1,0)<CR>
nos<Plug>(easymotion-W) * :<C-U>call EasyMotion#WBW(0,0)<CR>
x  <Plug>(easymotion-bd-w) * <Esc>:<C-U>call EasyMotion#WB(1,2)<CR>
nos<Plug>(easymotion-bd-w) * :<C-U>call EasyMotion#WB(0,2)<CR>
x  <Plug>(easymotion-iskeyword-bd-e) * <Esc>:<C-U>call EasyMotion#EK(1,2)<CR>
nos<Plug>(easymotion-iskeyword-bd-e) * :<C-U>call EasyMotion#EK(0,2)<CR>
x  <Plug>(easymotion-ge) * <Esc>:<C-U>call EasyMotion#E(1,1)<CR>
nos<Plug>(easymotion-ge) * :<C-U>call EasyMotion#E(0,1)<CR>
x  <Plug>(easymotion-E) * <Esc>:<C-U>call EasyMotion#EW(1,0)<CR>
nos<Plug>(easymotion-E) * :<C-U>call EasyMotion#EW(0,0)<CR>
x  <Plug>(easymotion-bd-e) * <Esc>:<C-U>call EasyMotion#E(1,2)<CR>
nos<Plug>(easymotion-bd-e) * :<C-U>call EasyMotion#E(0,2)<CR>
x  <Plug>(easymotion-B) * <Esc>:<C-U>call EasyMotion#WBW(1,1)<CR>
nos<Plug>(easymotion-B) * :<C-U>call EasyMotion#WBW(0,1)<CR>
n  <Plug>(easymotion-overwin-w) * :<C-U>call EasyMotion#overwin#w()<CR>
n  <Plug>(easymotion-overwin-line) * :<C-U>call EasyMotion#overwin#line()<CR>
n  <Plug>(easymotion-overwin-f2) * :<C-U>call EasyMotion#OverwinF(2)<CR>
n  <Plug>(easymotion-overwin-f) * :<C-U>call EasyMotion#OverwinF(1)<CR>
x  <Plug>(easymotion-Tln) * <Esc>:<C-U>call EasyMotion#TL(-1,1,1)<CR>
nos<Plug>(easymotion-Tln) * :<C-U>call EasyMotion#TL(-1,0,1)<CR>
x  <Plug>(easymotion-t2) * <Esc>:<C-U>call EasyMotion#T(2,1,0)<CR>
nos<Plug>(easymotion-t2) * :<C-U>call EasyMotion#T(2,0,0)<CR>
x  <Plug>(easymotion-t) * <Esc>:<C-U>call EasyMotion#T(1,1,0)<CR>
nos<Plug>(easymotion-t) * :<C-U>call EasyMotion#T(1,0,0)<CR>
x  <Plug>(easymotion-s) * <Esc>:<C-U>call EasyMotion#S(1,1,2)<CR>
nos<Plug>(easymotion-s) * :<C-U>call EasyMotion#S(1,0,2)<CR>
x  <Plug>(easymotion-tn) * <Esc>:<C-U>call EasyMotion#T(-1,1,0)<CR>
nos<Plug>(easymotion-tn) * :<C-U>call EasyMotion#T(-1,0,0)<CR>
x  <Plug>(easymotion-bd-t2) * <Esc>:<C-U>call EasyMotion#T(2,1,2)<CR>
nos<Plug>(easymotion-bd-t2) * :<C-U>call EasyMotion#T(2,0,2)<CR>
x  <Plug>(easymotion-tl) * <Esc>:<C-U>call EasyMotion#TL(1,1,0)<CR>
nos<Plug>(easymotion-tl) * :<C-U>call EasyMotion#TL(1,0,0)<CR>
x  <Plug>(easymotion-bd-tn) * <Esc>:<C-U>call EasyMotion#T(-1,1,2)<CR>
nos<Plug>(easymotion-bd-tn) * :<C-U>call EasyMotion#T(-1,0,2)<CR>
x  <Plug>(easymotion-fn) * <Esc>:<C-U>call EasyMotion#S(-1,1,0)<CR>
nos<Plug>(easymotion-fn) * :<C-U>call EasyMotion#S(-1,0,0)<CR>
x  <Plug>(easymotion-bd-tl) * <Esc>:<C-U>call EasyMotion#TL(1,1,2)<CR>
nos<Plug>(easymotion-bd-tl) * :<C-U>call EasyMotion#TL(1,0,2)<CR>
x  <Plug>(easymotion-fl) * <Esc>:<C-U>call EasyMotion#SL(1,1,0)<CR>
nos<Plug>(easymotion-fl) * :<C-U>call EasyMotion#SL(1,0,0)<CR>
x  <Plug>(easymotion-bd-tl2) * <Esc>:<C-U>call EasyMotion#TL(2,1,2)<CR>
nos<Plug>(easymotion-bd-tl2) * :<C-U>call EasyMotion#TL(2,0,2)<CR>
x  <Plug>(easymotion-bd-fn) * <Esc>:<C-U>call EasyMotion#S(-1,1,2)<CR>
nos<Plug>(easymotion-bd-fn) * :<C-U>call EasyMotion#S(-1,0,2)<CR>
x  <Plug>(easymotion-f) * <Esc>:<C-U>call EasyMotion#S(1,1,0)<CR>
nos<Plug>(easymotion-f) * :<C-U>call EasyMotion#S(1,0,0)<CR>
x  <Plug>(easymotion-bd-fl) * <Esc>:<C-U>call EasyMotion#SL(1,1,2)<CR>
nos<Plug>(easymotion-bd-fl) * :<C-U>call EasyMotion#SL(1,0,2)<CR>
x  <Plug>(easymotion-Fl2) * <Esc>:<C-U>call EasyMotion#SL(2,1,1)<CR>
nos<Plug>(easymotion-Fl2) * :<C-U>call EasyMotion#SL(2,0,1)<CR>
x  <Plug>(easymotion-tl2) * <Esc>:<C-U>call EasyMotion#TL(2,1,0)<CR>
nos<Plug>(easymotion-tl2) * :<C-U>call EasyMotion#TL(2,0,0)<CR>
x  <Plug>(easymotion-f2) * <Esc>:<C-U>call EasyMotion#S(2,1,0)<CR>
nos<Plug>(easymotion-f2) * :<C-U>call EasyMotion#S(2,0,0)<CR>
x  <Plug>(easymotion-Fln) * <Esc>:<C-U>call EasyMotion#SL(-1,1,1)<CR>
nos<Plug>(easymotion-Fln) * :<C-U>call EasyMotion#SL(-1,0,1)<CR>
x  <Plug>(easymotion-sln) * <Esc>:<C-U>call EasyMotion#SL(-1,1,2)<CR>
nos<Plug>(easymotion-sln) * :<C-U>call EasyMotion#SL(-1,0,2)<CR>
x  <Plug>(easymotion-tln) * <Esc>:<C-U>call EasyMotion#TL(-1,1,0)<CR>
nos<Plug>(easymotion-tln) * :<C-U>call EasyMotion#TL(-1,0,0)<CR>
x  <Plug>(easymotion-fl2) * <Esc>:<C-U>call EasyMotion#SL(2,1,0)<CR>
nos<Plug>(easymotion-fl2) * :<C-U>call EasyMotion#SL(2,0,0)<CR>
x  <Plug>(easymotion-bd-fl2) * <Esc>:<C-U>call EasyMotion#SL(2,1,2)<CR>
nos<Plug>(easymotion-bd-fl2) * :<C-U>call EasyMotion#SL(2,0,2)<CR>
x  <Plug>(easymotion-T2) * <Esc>:<C-U>call EasyMotion#T(2,1,1)<CR>
nos<Plug>(easymotion-T2) * :<C-U>call EasyMotion#T(2,0,1)<CR>
x  <Plug>(easymotion-bd-tln) * <Esc>:<C-U>call EasyMotion#TL(-1,1,2)<CR>
nos<Plug>(easymotion-bd-tln) * :<C-U>call EasyMotion#TL(-1,0,2)<CR>
x  <Plug>(easymotion-T) * <Esc>:<C-U>call EasyMotion#T(1,1,1)<CR>
nos<Plug>(easymotion-T) * :<C-U>call EasyMotion#T(1,0,1)<CR>
x  <Plug>(easymotion-bd-t) * <Esc>:<C-U>call EasyMotion#T(1,1,2)<CR>
nos<Plug>(easymotion-bd-t) * :<C-U>call EasyMotion#T(1,0,2)<CR>
x  <Plug>(easymotion-Tn) * <Esc>:<C-U>call EasyMotion#T(-1,1,1)<CR>
nos<Plug>(easymotion-Tn) * :<C-U>call EasyMotion#T(-1,0,1)<CR>
x  <Plug>(easymotion-s2) * <Esc>:<C-U>call EasyMotion#S(2,1,2)<CR>
nos<Plug>(easymotion-s2) * :<C-U>call EasyMotion#S(2,0,2)<CR>
x  <Plug>(easymotion-Tl) * <Esc>:<C-U>call EasyMotion#TL(1,1,1)<CR>
nos<Plug>(easymotion-Tl) * :<C-U>call EasyMotion#TL(1,0,1)<CR>
x  <Plug>(easymotion-sn) * <Esc>:<C-U>call EasyMotion#S(-1,1,2)<CR>
nos<Plug>(easymotion-sn) * :<C-U>call EasyMotion#S(-1,0,2)<CR>
x  <Plug>(easymotion-Fn) * <Esc>:<C-U>call EasyMotion#S(-1,1,1)<CR>
nos<Plug>(easymotion-Fn) * :<C-U>call EasyMotion#S(-1,0,1)<CR>
x  <Plug>(easymotion-sl) * <Esc>:<C-U>call EasyMotion#SL(1,1,2)<CR>
nos<Plug>(easymotion-sl) * :<C-U>call EasyMotion#SL(1,0,2)<CR>
x  <Plug>(easymotion-Fl) * <Esc>:<C-U>call EasyMotion#SL(1,1,1)<CR>
nos<Plug>(easymotion-Fl) * :<C-U>call EasyMotion#SL(1,0,1)<CR>
x  <Plug>(easymotion-sl2) * <Esc>:<C-U>call EasyMotion#SL(2,1,2)<CR>
nos<Plug>(easymotion-sl2) * :<C-U>call EasyMotion#SL(2,0,2)<CR>
x  <Plug>(easymotion-bd-fln) * <Esc>:<C-U>call EasyMotion#SL(-1,1,2)<CR>
nos<Plug>(easymotion-bd-fln) * :<C-U>call EasyMotion#SL(-1,0,2)<CR>
x  <Plug>(easymotion-F) * <Esc>:<C-U>call EasyMotion#S(1,1,1)<CR>
nos<Plug>(easymotion-F) * :<C-U>call EasyMotion#S(1,0,1)<CR>
x  <Plug>(easymotion-bd-f) * <Esc>:<C-U>call EasyMotion#S(1,1,2)<CR>
nos<Plug>(easymotion-bd-f) * :<C-U>call EasyMotion#S(1,0,2)<CR>
x  <Plug>(easymotion-F2) * <Esc>:<C-U>call EasyMotion#S(2,1,1)<CR>
nos<Plug>(easymotion-F2) * :<C-U>call EasyMotion#S(2,0,1)<CR>
x  <Plug>(easymotion-bd-f2) * <Esc>:<C-U>call EasyMotion#S(2,1,2)<CR>
nos<Plug>(easymotion-bd-f2) * :<C-U>call EasyMotion#S(2,0,2)<CR>
x  <Plug>(easymotion-Tl2) * <Esc>:<C-U>call EasyMotion#TL(2,1,1)<CR>
nos<Plug>(easymotion-Tl2) * :<C-U>call EasyMotion#TL(2,0,1)<CR>
x  <Plug>(easymotion-fln) * <Esc>:<C-U>call EasyMotion#SL(-1,1,0)<CR>
nos<Plug>(easymotion-fln) * :<C-U>call EasyMotion#SL(-1,0,0)<CR>
o  <Plug>(fzf-maps-o) * <C-C>:<C-U>call fzf#vim#maps('o', 0)<CR>
x  <Plug>(fzf-maps-x) * :<C-U>call fzf#vim#maps('x', 0)<CR>
n  <Plug>(fzf-maps-n) * :<C-U>call fzf#vim#maps('n', 0)<CR>
n  <Plug>(fzf-normal) * <Nop>
n  <Plug>(fzf-insert) * i
s  <C-R>       * <C-G>"_c<C-R>
s  <C-H>       * <C-G>"_c
s  <Del>       * <C-G>"_c
s  <BS>        * <C-G>"_c
s  <C-Tab>     * <Esc>:call UltiSnips#ListSnippets()<CR>
n  <Plug>CtrlSFQuickfixPwordExec * <SNR>80_SearchPwordCmd('CtrlSFQuickfix', 1)
n  <Plug>CtrlSFQuickfixPwordPath * <SNR>80_SearchPwordCmd('CtrlSFQuickfix', 0)
v  <Plug>CtrlSFQuickfixVwordExec * <SNR>80_SearchVwordCmd('CtrlSFQuickfix', 1)
v  <Plug>CtrlSFQuickfixVwordPath * <SNR>80_SearchVwordCmd('CtrlSFQuickfix', 0)
n  <Plug>CtrlSFQuickfixCCwordExec * <SNR>80_SearchCwordCmd('CtrlSFQuickfix', 1, 1)
n  <Plug>CtrlSFQuickfixCCwordPath * <SNR>80_SearchCwordCmd('CtrlSFQuickfix', 1, 0)
n  <Plug>CtrlSFQuickfixCwordExec * <SNR>80_SearchCwordCmd('CtrlSFQuickfix', 0, 1)
n  <Plug>CtrlSFQuickfixCwordPath * <SNR>80_SearchCwordCmd('CtrlSFQuickfix', 0, 0)
n  <Plug>CtrlSFQuickfixPrompt * :CtrlSFQuickfix<Space>
n  <Plug>CtrlSFPwordExec * <SNR>80_SearchPwordCmd('CtrlSF', 1)
n  <Plug>CtrlSFPwordPath * <SNR>80_SearchPwordCmd('CtrlSF', 0)
v  <Plug>CtrlSFVwordExec * <SNR>80_SearchVwordCmd('CtrlSF', 1)
v  <Plug>CtrlSFVwordPath * <SNR>80_SearchVwordCmd('CtrlSF', 0)
n  <Plug>CtrlSFCCwordExec * <SNR>80_SearchCwordCmd('CtrlSF', 1, 1)
n  <Plug>CtrlSFCCwordPath * <SNR>80_SearchCwordCmd('CtrlSF', 1, 0)
n  <Plug>CtrlSFCwordExec * <SNR>80_SearchCwordCmd('CtrlSF', 0, 1)
n  <Plug>CtrlSFCwordPath * <SNR>80_SearchCwordCmd('CtrlSF', 0, 0)
n  <Plug>CtrlSFPrompt * :CtrlSF<Space>
n  <Plug>NERDCommenterAltDelims * :call nerdcommenter#SwitchToAlternativeDelimiters(1)<CR>
x  <Plug>NERDCommenterUncomment * :call nerdcommenter#Comment("x", "Uncomment")<CR>
n  <Plug>NERDCommenterUncomment * :call nerdcommenter#Comment("n", "Uncomment")<CR>
x  <Plug>NERDCommenterAlignBoth * :call nerdcommenter#Comment("x", "AlignBoth")<CR>
n  <Plug>NERDCommenterAlignBoth * :call nerdcommenter#Comment("n", "AlignBoth")<CR>
x  <Plug>NERDCommenterAlignLeft * :call nerdcommenter#Comment("x", "AlignLeft")<CR>
n  <Plug>NERDCommenterAlignLeft * :call nerdcommenter#Comment("n", "AlignLeft")<CR>
n  <Plug>NERDCommenterAppend * :call nerdcommenter#Comment("n", "Append")<CR>
x  <Plug>NERDCommenterYank * :call nerdcommenter#Comment("x", "Yank")<CR>
n  <Plug>NERDCommenterYank * :call nerdcommenter#Comment("n", "Yank")<CR>
x  <Plug>NERDCommenterSexy * :call nerdcommenter#Comment("x", "Sexy")<CR>
n  <Plug>NERDCommenterSexy * :call nerdcommenter#Comment("n", "Sexy")<CR>
x  <Plug>NERDCommenterInvert * :call nerdcommenter#Comment("x", "Invert")<CR>
n  <Plug>NERDCommenterInvert * :call nerdcommenter#Comment("n", "Invert")<CR>
n  <Plug>NERDCommenterToEOL * :call nerdcommenter#Comment("n", "ToEOL")<CR>
x  <Plug>NERDCommenterNested * :call nerdcommenter#Comment("x", "Nested")<CR>
n  <Plug>NERDCommenterNested * :call nerdcommenter#Comment("n", "Nested")<CR>
x  <Plug>NERDCommenterMinimal * :call nerdcommenter#Comment("x", "Minimal")<CR>
n  <Plug>NERDCommenterMinimal * :call nerdcommenter#Comment("n", "Minimal")<CR>
x  <Plug>NERDCommenterToggle * :call nerdcommenter#Comment("x", "Toggle")<CR>
n  <Plug>NERDCommenterToggle * :call nerdcommenter#Comment("n", "Toggle")<CR>
x  <Plug>NERDCommenterComment * :call nerdcommenter#Comment("x", "Comment")<CR>
n  <Plug>NERDCommenterComment * :call nerdcommenter#Comment("n", "Comment")<CR>
v  <Plug>VgSurround * :<C-U>call <SNR>77_opfunc(visualmode(),visualmode() ==# 'V' ? 0 : 1)<CR>
v  <Plug>VSurround * :<C-U>call <SNR>77_opfunc(visualmode(),visualmode() ==# 'V' ? 1 : 0)<CR>
n  <Plug>YSurround * <SNR>77_opfunc2('setup')
n  <Plug>Ysurround * <SNR>77_opfunc('setup')
n  <Plug>YSsurround * <SNR>77_opfunc2('setup').'_'
n  <Plug>Yssurround * '^'.v:count1.<SNR>77_opfunc('setup').'g_'
n  <Plug>CSurround * :<C-U>call <SNR>77_changesurround(1)<CR>
n  <Plug>Csurround * :<C-U>call <SNR>77_changesurround()<CR>
n  <Plug>Dsurround * :<C-U>call <SNR>77_dosurround(<SNR>77_inputtarget())<CR>
n  <Plug>SurroundRepeat * .
n  <Plug>VimwikiMakeTomorrowDiaryNote & :<C-U>call vimwiki#diary#make_note(v:count, 0, vimwiki#diary#diary_date_link(localtime() + 60*60*24))<CR>
n  <Plug>VimwikiMakeYesterdayDiaryNote & :<C-U>call vimwiki#diary#make_note(v:count, 0, vimwiki#diary#diary_date_link(localtime() - 60*60*24))<CR>
n  <Plug>VimwikiTabMakeDiaryNote & :<C-U>call vimwiki#diary#make_note(v:count, 1)<CR>
n  <Plug>VimwikiMakeDiaryNote & :<C-U>call vimwiki#diary#make_note(v:count)<CR>
n  <Plug>VimwikiDiaryGenerateLinks & :VimwikiDiaryGenerateLinks<CR>
n  <Plug>VimwikiDiaryIndex & :<C-U>call vimwiki#diary#goto_diary_index(v:count)<CR>
n  <Plug>VimwikiUISelect & :VimwikiUISelect<CR>
n  <Plug>VimwikiTabIndex & :<C-U>call vimwiki#base#goto_index(v:count, 1)<CR>
n  <Plug>VimwikiIndex & :<C-U>call vimwiki#base#goto_index(v:count)<CR>
n  <Plug>(table-mode-sort) * :call tablemode#spreadsheet#Sort('')<CR>
n  <Plug>(table-mode-echo-cell) * :call tablemode#spreadsheet#EchoCell()<CR>
n  <Plug>(table-mode-eval-formula) * :call tablemode#spreadsheet#formula#EvaluateFormulaLine()<CR>
n  <Plug>(table-mode-add-formula) * :call tablemode#spreadsheet#formula#Add()<CR>
n  <Plug>(table-mode-insert-column-after) * :<C-U>call tablemode#spreadsheet#InsertColumn(1)<CR>
n  <Plug>(table-mode-insert-column-before) * :<C-U>call tablemode#spreadsheet#InsertColumn(0)<CR>
n  <Plug>(table-mode-delete-column) * :<C-U>call tablemode#spreadsheet#DeleteColumn()<CR>
n  <Plug>(table-mode-delete-row) * :<C-U>call tablemode#spreadsheet#DeleteRow()<CR>
x  <Plug>(table-mode-cell-text-object-i) * :<C-U>call tablemode#spreadsheet#cell#TextObject(1)<CR>
x  <Plug>(table-mode-cell-text-object-a) * :<C-U>call tablemode#spreadsheet#cell#TextObject(0)<CR>
o  <Plug>(table-mode-cell-text-object-i) * :<C-U>call tablemode#spreadsheet#cell#TextObject(1)<CR>
o  <Plug>(table-mode-cell-text-object-a) * :<C-U>call tablemode#spreadsheet#cell#TextObject(0)<CR>
n  <Plug>(table-mode-motion-right) * :<C-U>call tablemode#spreadsheet#cell#Motion('l')<CR>
n  <Plug>(table-mode-motion-left) * :<C-U>call tablemode#spreadsheet#cell#Motion('h')<CR>
n  <Plug>(table-mode-motion-down) * :<C-U>call tablemode#spreadsheet#cell#Motion('j')<CR>
n  <Plug>(table-mode-motion-up) * :<C-U>call tablemode#spreadsheet#cell#Motion('k')<CR>
n  <Plug>(table-mode-realign) * :call tablemode#table#Realign('.')<CR>
x  <Plug>(table-mode-tableize-delimiter) * :<C-U>call tablemode#TableizeByDelimiter()<CR>
x  <Plug>(table-mode-tableize) * :Tableize<CR>
n  <Plug>(table-mode-tableize) * :Tableize<CR>
x  <Plug>(signify-motion-outer-visual) * :<C-U>call sy#util#hunk_text_object(1)<CR>
o  <Plug>(signify-motion-outer-pending) * :<C-U>call sy#util#hunk_text_object(1)<CR>
x  <Plug>(signify-motion-inner-visual) * :<C-U>call sy#util#hunk_text_object(0)<CR>
o  <Plug>(signify-motion-inner-pending) * :<C-U>call sy#util#hunk_text_object(0)<CR>
n  <Plug>(signify-prev-hunk) * &diff ? '[c' : ":\<C-U>call sy#jump#prev_hunk(v:count1)\<CR>"
n  <Plug>(signify-next-hunk) * &diff ? ']c' : ":\<C-U>call sy#jump#next_hunk(v:count1)\<CR>"
n  <Plug>fugitive: & <Nop>
n  <Plug>fugitive:y<C-G> & :<C-U>call setreg(v:register, fugitive#Object(@%))<CR>
n  <Plug>(conflict-marker-prev-hunk) * :<C-U>ConflictMarkerPrevHunk<CR>
n  <Plug>(conflict-marker-next-hunk) * :<C-U>ConflictMarkerNextHunk<CR>
n  <Plug>(conflict-marker-none) * :<C-U>ConflictMarkerNone<CR>
n  <Plug>(conflict-marker-both-rev) * :<C-U>ConflictMarkerBoth!<CR>
n  <Plug>(conflict-marker-both) * :<C-U>ConflictMarkerBoth<CR>
n  <Plug>(conflict-marker-ourselves) * :<C-U>ConflictMarkerOurselves<CR>
n  <Plug>(conflict-marker-themselves) * :<C-U>ConflictMarkerThemselves<CR>
n  <Plug>(ctrlp) * :<C-U>CtrlP<CR>
   <Plug>SlimeConfig & :<C-U>SlimeConfig<CR>
   <Plug>SlimeParagraphSend & <SNR>21_Operatorip
   <Plug>SlimeMotionSend & <SNR>21_Operator
   <Plug>SlimeLineSend & :<C-U>call slime#send_lines(v:count1)<CR>
   <Plug>SlimeRegionSend & :<C-U>call slime#send_op(visualmode(), 1)<CR>
   <SNR>21_Operator * :<C-U>call slime#store_curpos()<CR>:set opfunc=slime#send_op<CR>g@
   <Plug>BufKillUndo * :call <SNR>20_UndoKill()<CR>
   <Plug>BufKillBangBw * :call <SNR>20_BufKill('bw', '!')<CR>
   <Plug>BufKillBw * :call <SNR>20_BufKill('bw', '')<CR>
   <Plug>BufKillBangBd * :call <SNR>20_BufKill('bd', '!')<CR>
   <Plug>BufKillBd * :call <SNR>20_BufKill('bd', '')<CR>
   <Plug>BufKillBangBun * :call <SNR>20_BufKill('bun', '!')<CR>
   <Plug>BufKillBun * :call <SNR>20_BufKill('bun', '')<CR>
   <Plug>BufKillBangForward * :call <SNR>20_GotoBuffer('bufforward', '!')<CR>
   <Plug>BufKillForward * :call <SNR>20_GotoBuffer('bufforward', '')<CR>
   <Plug>BufKillBw * :call <SNR>20_BufKill('bw', '')<CR>
   <Plug>BufKillBangBd * :call <SNR>20_BufKill('bd', '!')<CR>
   <Plug>BufKillBd * :call <SNR>20_BufKill('bd', '')<CR>
   <Plug>BufKillBangBun * :call <SNR>20_BufKill('bun', '!')<CR>
   <Plug>BufKillBun * :call <SNR>20_BufKill('bun', '')<CR>
   <Plug>BufKillBangForward * :call <SNR>20_GotoBuffer('bufforward', '!')<CR>
   <Plug>BufKillForward * :call <SNR>20_GotoBuffer('bufforward', '')<CR>
   <Plug>BufKillBangBack * :call <SNR>20_GotoBuffer('bufback', '!')<CR>
   <Plug>BufKillBack * :call <SNR>20_GotoBuffer('bufback', '')<CR>
   <Plug>BufKillBangAlt * :call <SNR>20_GotoBuffer('#', '!')<CR>
   <Plug>BufKillAlt * :call <SNR>20_GotoBuffer('#', '')<CR>
   <F8>          :call Rungdb()<CR>
   <F5>          :call CompileRunGcc()<CR>
   <C-X>       * ea<C-X>s
   <M-C-F>       :Format<CR>
n  <C-S>         zz
n  <C-Bslash>  * :BA<CR>
n  <C-Left>    * :BB<CR>
n  <C-Right>   * :BF<CR>
n  <C-H>       * :bp<CR>
   <C-W><C-L>  * <C-W>l
   <C-W><C-K>  * <C-W>k
   <C-W><C-J>  * <C-W>j
   <C-W><C-H>  * <C-W>h
   <C-J>       * 5<C-E>
   <C-K>       * 5<C-Y>
   <Right>       <Nop>
   <Left>        <Nop>
   <Down>        <Nop>
   <Up>          <Nop>
v  <C-Z>       * <C-C>:update<CR>
no <C-Z>       * :update<CR>
   <C-Q>       * :q<CR>
n  <C-D>       * <C-X>
n  <C-G>       * <C-A>
   <F11>         :call ToggleFullscreen()<CR>
   <C-P>         :CtrlP<CR>
n  <C-E>v        <Plug>SlimeConfig
n  <C-E><C-E>    <Plug>SlimeParagraphSend
x  <C-E><C-E>    <Plug>SlimeRegionSend
n  <C-L>       * :bn<CR>
```





```
x  #           * y?\V<C-R>"<CR>
                 Nvim builtin
n  &           * :&&<CR>
                 Nvim builtin
x  *           * y/\V<C-R>"<CR>
                 Nvim builtin
n  Y           * y$
                 Nvim builtin
   \           * ;
n  <C-L>       * <Cmd>nohlsearch|diffupdate|normal! <C-L><CR>
```

---

`timeout` and `timeoutlen` apply to **mappings**

These are pretty straightforward: if you increase the length of `timeoutlen`, then Vim will wait for longer after each keystroke of the mapping before aborting it and carrying out the behaviour of the keys typed so far. If you instead unset `timeout`, then Vim will wait *forever* for you to either type the complete mapping or type something which doesn't match any of your mappings.

`ttimeout` and `ttimeoutlen` apply to **key codes**.

A common example of something sends key codes is the arrow keys. In the terminal presses of the arrow keys are generally represented by *sequences* of characters. You can see what (Vim thinks) your terminal is sending when you press e.g. the left arrow key by executing the command:

```
:set <left>?
```

In my terminal, when I run the above, Vim outputs the following:

```
t_kl <Left>     ^[O*D
```

This means that what my terminal sends to Vim when I press the arrow key is the sequences of characters: EscapeO*D.

(`^[` is a plain-text representation of the **ESC** character)

The only way that Vim can distinguish these sequences from actual keypresses is the speed with which it receives them, and you configure this with the `ttimeout` and `ttimeoutlen` settings.

Thus, if you set `ttimeoutlen` to a sufficiently large value (try `5000`: five seconds) then you can move your cursor to the left by literally typing EscapeO*D on your keyboard.

However, this *also* means that if you press Escape in visual mode, then Vim will wait 5 seconds to whether you actually pressed Escape (to exit visual mode) or in fact just pressed Left in an extremely slow terminal.

Generally, you want to set `timeout` and `timeoutlen` according to how quickly you generally type mappings, and you should set `ttimeoutlen` to a pretty small value: `defaults.vim` sets this to 100 milliseconds, but you can probably go a fair bit shorter than this without unwanted consequences.

Longer values of `ttimeoutlen` are only required for "slow terminals or very busy systems" when key codes are timing out, but as processor and network speeds increase this is less and less of an issue in practice.

---

1. `zt` (scroll to Top): This command scrolls the current line to the top of the window.
2. `zz` (scroll to center): This command scrolls the current line to the center of the window.
3. `zb` (scroll to Bottom): This command scrolls the current line to the bottom of the window.

folding-related commands:

1. `za` (toggle fold): This command toggles the current fold open or closed.
2. `zo` (open fold): This command opens the current fold.
3. `zc` (close fold): This command closes the current fold.
4. `zm` (fold more): This command increases the fold level, closing more folds.
5. `zr` (fold less): This command decreases the fold level, opening more folds.

---

In Vim, `map` and `nmap` are both used to create key mappings, but they have different scopes:

- `map`: Creates a key mapping that works in Normal, Visual, Select, and Operator-pending modes. In other words, it's a general mapping that applies to several modes.
- `nmap`: Creates a key mapping that works only in Normal mode. It's more specific and does not affect other modes.

---