# Latex 数学符号大全

[toc]

## 运算符 (Operators)

| Symbol             | Command            | Symbol          | Command             | Symbol           | Command          |
| ------------------ | ------------------ | --------------- | ------------------- | ---------------- | ---------------- |
| $\pm$              | `\pm`              | $\mp$           | `\mp`               | $\times$         | `\times`         |
| $\div$             | `\div`             | $\cdot$         | `\cdot`             | $\ast$           | `\ast`           |
| $\star$            | `\star`            | $\dagger$       | `\dagger`           | $\ddagger$       | `\ddagger`       |
| $\amalg$           | `\amalg`           | $\cap$          | `\cap`              | $\cup$           | `\cup`           |
| $\uplus$           | `\uplus`           | $\sqcap$        | `\sqcap`            | $\sqcup$         | `\sqcup`         |
| $\vee$             | `\vee` or `\lor`   | $\wedge$        | `\wedge` or `\land` | $\oplus$         | `\oplus`         |
| $\ominus$          | `\ominus`          | $\otimes$       | `$\otimes`          | $\circ$          | `\circ`          |
| $\bullet$          | `\bullet`          | $\diamond$      | `\diamond`          | $\lhd$           | `\lhd`           |
| $\rhd$             | `\rhd`             | $\unlhd$        | `\unlhd`            | $\unrhd$         | `\unrhd`         |
| $\oslash$          | `\oslash`          | $\odot$         | `\odot`             | $\bigcirc$       | `\bigcirc`       |
| $\triangleleft$    | `\triangleleft`    | $\Diamond$      | `\Diamond`          | $\bigtriangleup$ | `\bigtriangleup` |
| $\bigtriangledown$ | `\bigtriangledown` | $\Box$          | `\Box`              | $\triangleright$ | `\triangleright` |
| $\setminus$        | `\setminus`        | $\wr$           | `\wr`               | $\sqrt{x}$       | `\sqrt{x}`       |
| $x^{\circ}$        | `x^{\circ}`        | $\triangledown$ | `\triangledown`     | $\sqrt[n]{x}$    | `\sqrt[m]{x}`    |
| $a^x$              | `a^x`              | $a^{xyz}$       | `a^{xyz}`           | $a_x$            | `a_x`            |

**AMS 运算符**

| Symbol       | Command      | Symbol        | Command       | Symbol             | Command            |
| ------------ | ------------ | ------------- | ------------- | ------------------ | ------------------ |
| $\dotplus$   | `\dotplus`   | $\centerdot$  | `\centerdot`  |                    |                    |
| $\ltimes$    | `\ltimes`    | $\rtimes$     | `\rtimes`     | $\divideontimes$   | `\divideontimes`   |
| $\doublecup$ | `\doublecup` | $\doublecap$  | `\doublecap`  | $\smallsetminus$   | `\smallsetminus`   |
| $\veebar$    | `\veebar`    | $\barwedge$   | `\barwedge`   | $\doublebarwedge$  | `\doublebarwedge`  |
| $\boxplus$   | `\boxplus`   | $\boxminus$   | `\boxminus`   | $\circleddash$     | `\circleddash`     |
| $\boxtimes$  | `\boxtimes`  | $\boxdot$     | `\boxdot`     | $\circledcirc$     | `\circledcirc`     |
| $\intercal$  | `\intercal`  | $\circledast$ | `\circledast` | $\rightthreetimes$ | `\rightthreetimes` |
| $\curlyvee$  | `$\curlyvee` | $\curlywedge$ | `\curlywedge` | $\leftthreetimes$  | `\leftthreetimes`  |

## 关系符 (Relations)

| Symbol        | Command       | Symbol      | Command     | Symbol        | Command       |
| ------------- | ------------- | ----------- | ----------- | ------------- | ------------- |
| $\le$         | `\le`         | $\ge$       | `\ge`       | $\neq$        | `\neq`        |
| $\sim$        | `\sim`        | $\ll$       | `\ll`       | $\gg$         | `\gg`         |
| $\doteq$      | `\doteq`      | $\simeq$    | `\simeq`    | $\subset$     | `\subset`     |
| $\supset$     | `\supset`     | $\approx$   | `\approx`   | $\asymp$      | `\asymp`      |
| $\subseteq$   | `\subseteq`   | $\supseteq$ | `\supseteq` | $\cong$       | `\cong`       |
| $\smile$      | `\smile`      | $\sqsubset$ | `\sqsubset` | $\sqsupset$   | `\sqsupset`   |
| $\equiv$      | `\equiv`      | $\frown$    | `\frown`    | $\sqsubseteq$ | `\sqsubseteq` |
| $\sqsupseteq$ | `\sqsupseteq` | $\propto$   | `\propto`   | $\bowtie$     | `\bowtie`     |
| $\in$         | `\in`         | $\ni$       | `\ni`       | $\prec$       | `\prec`       |
| $\succ$       | `\succ`       | $\vdash$    | `\vdash`    | $\dashv$      | `\dashv`      |
| $\preceq$     | `\preceq`     | $\succeq$   | `\succeq`   | $\models$     | `\models`     |
| $\perp$       | `\perp`       | $\parallel$ | `\parallel` |               |               |
| $\mid$        | `\mid`        | $\bumpeq$   | `\bumpeq`   |               |               |

Negations of many of these relations can be formed by just putting `\not` before the symbol, or by slipping an `n` between the `\` and the word. Here are a couple examples, plus many other negations; it works for many of the many others as well.

只要将 `not` 放在符号前面或者在 `\` 和单词之间插入一个 `n`，就可以形成许多这些关系的否定形式，这里有一些例子，加上一些其他的否定，它也适用于许多其他的。

| Symbol          | Command         | Symbol      | Command     | Symbol       | Command           |
| --------------- | --------------- | ----------- | ----------- | ------------ | ----------------- |
| $\nmid$         | `\nmid`         | $\nleq$     | `\nleq`     | $\ngeq$      | `\ngeq`           |
| $\nsim$         | `\nsim`         | $\ncong$    | `\ncong`    | $\nparallel$ | `\nparallel`      |
| $\not<$         | `\not<`         | $\not>$     | `\not>`     | $\not=$      | `\not=` or `\neq` |
| $\not\le$       | `\not\le`       | $\not\ge$   | `\not\ge`   | $\not\sim$   | `\not\sim`        |
| $\not\approx$   | `\not\approx`   | $\not\cong$ | `\not\cong` | $\not\equiv$ | `\not\equiv`      |
| $\not\parallel$ | `\not\parallel` | $\nless$    | `\nless`    | $\ngtr$      | `\ngtr`           |
| $\lneq$         | `\lneq`         | $\gneq$     | `\gneq`     | $\lnsim$     | `\lnsim`          |
| $\lneqq$        | `lneqq`         | $\gneqq$    | `\gneqq`    |              |                   |

## 希腊字母 (Greek Letters)

**小写 (Lowercase Letters)**

| Symbol     | Command    | Symbol        | Command       | Symbol   | Command  | Symbol     | Command    |
| ---------- | ---------- | ------------- | ------------- | -------- | -------- | ---------- | ---------- |
| $\alpha$   | `\alpha`   | $\beta$       | `\beta`       | $\gamma$ | `\gamma` | $\delta$   | `\delta`   |
| $\epsilon$ | `\epsilon` | $\varepsilon$ | `\varepsilon` | $\zeta$  | `\zeta`  | $\eta$     | `\eta`     |
| $\theta$   | `\theta`   | $\vartheta$   | `\vartheta`   | $\iota$  | `\iota`  | $\kappa$   | `\kappa`   |
| $\lambda$  | `\lambda`  | $\mu$         | `\mu`         | $\nu$    | `\nu`    | $\xi$      | `\xi`      |
| $\pi$      | `\pi`      | $\varpi$      | `\varpi`      | $\rho$   | `rho`    | $\varrho$  | `\varrho`  |
| $\sigma$   | `\sigma`   | $\varsigma$   | `\varsigma`   | $\tau$   | `\tau`   | $\upsilon$ | `\upsilon` |
| $\phi$     | `\phi`     | $\varphi$     | `\varphi`     | $\chi$   | `\chi`   | $\psi$     | `\psi`     |
| $\omega$   | `\omega`   |               |               |          |          |            |            |

**大写 (Capital Letters)**

| Symbol      | Command     | Symbol      | Command     | Symbol      | Command     | Symbol        | Command       |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ------------- | ------------- |
| $\Gamma$    | `\Gamma`    | $\Delta$    | `\Delta`    | $\Theta$    | `\Theta`    | $\Lambda$     | `\Lambda`     |
| $\Xi$       | `\Xi`       | $\Pi$       | `\Pi`       | $\Sigma$    | `\Sigma`    | $\Upsilon$    | `\Upsilon`    |
| $\Phi$      | `\Phi`      | $\Psi$      | `\Psi`      | $\Omega$    | `\Omega`    | $\nabla$      | `\nabla`      |
| $\varGamma$ | `\varGamma` | $\varDelta$ | `\varDelta` | $\varTheta$ | `\varTheta` | $\varLambda$  | `\varLambda`  |
| $\varXi$    | `\varXi`    | $\varPi$    | `\varPi`    | $\varSigma$ | `\varSigma` | $\varUpsilon$ | `\varUpsilon` |
| $\varPhi$   | `\varPhi`   | $\varPsi$   | `\varPsi`   | $\varOmega$ | `\varOmega` |               |               |

**古旧 (Archaic letters)**

| Symbol     | Command    | Symbol     | Command    |
| ---------- | ---------- | ---------- | ---------- |
| $\Digamma$ | `\Digamma` | $\digamma$ | `\digamma` |

## 箭头 (Arrows)

| Symbol                    | Command                   | Symbol                | Command               |
| ------------------------- | ------------------------- | --------------------- | --------------------- |
| $\leftarrow$              | `\leftarrow` or `gets`    | $\Leftarrow$          | `\Leftarrow`          |
| $\rightarrow$             | `\rightarrow` or `to`     | $\Rightarrow$         | `\Rightarrow`         |
| $\leftrightarrow$         | `\leftrightarrow`         | $\Leftrightarrow$     | `\Leftrightarrow`     |
| $\mapsto$                 | `\mapsto`                 | $\hookleftarrow$      | `\hookleftarrow`      |
| $\leftharpoonup$          | `\leftharpoonup`          | $\leftharpoondown$    | `\leftharpoondown`    |
| $\rightleftharpoons$      | `$\rightleftharpoons`     | $\longleftarrow$      | `\longleftarrow`      |
| $\Longleftarrow$          | `\Longleftarrow`          | $\longrightarrow$     | `\longrightarrow`     |
| $\Longrightarrow$         | `\Longrightarrow`         | $\longleftrightarrow$ | `\longleftrightarrow` |
| $\Longleftrightarrow$     | `\Longleftrightarrow`     | $\longmapsto$         | `\longmapsto`         |
| $\hookrightarrow$         | `$\hookrightarrow`        | $\rightharpoonup$     | `\rightharpoonup`     |
| $\rightharpoondown$       | `\rightharpoondown`       | $\leadsto$            | `\leadsto`            |
| $\uparrow$                | `\uparrow`                | $\Uparrow$            | `\Uparrow`            |
| $\downarrow$              | `\downarrow`              | $\Downarrow$          | `\Downarrow`          |
| $\updownarrow$            | `\updownarrow`            | $\Updownarrow$        | `\Updownarrow`        |
| $\nearrow$                | `\nearrow`                | $\searrow$            | `\searrow`            |
| $\swarrow$                | `\swarrow`                | $\nwarrow$            | `\nwarrow`            |
| $\overrightarrow{AB}$     | `$\overrightarrow{AB}`    | $\overleftarrow{AB}$  | `\overleftarrow{AB}`  |
| $\overleftrightarrow{AB}$ | `\overleftrightarrow{AB}` |                       |                       |

(For those of you who hate typing long strings of letters, `\iff` $\iff$, `\implies` $\implies$ and `\impliedby` $\impliedby$ can be used in place of `\Longleftrightarrow`, `\Longrightarrow` and `\Longleftarrow` respectively.)

(对于不喜欢键入长串字母的人，`\iff` $\iff$，`\implies` $\implies$ 和 `\impliedby` $\impliedby$ 可以分别替代`\Longleftrightarrow`，`\Longrightarrow` 和 `\Longleftarrow`)

**AMS 箭头**

| Symbol               | Command              | Symbol                 | Command                |
| -------------------- | -------------------- | ---------------------- | ---------------------- |
| $\dashleftarrow$     | `\dashleftarrow`     | $\dashrightarrow$      | `\dashrightarrow`      |
| $\leftleftarrows$    | `\leftleftarrows`    | $\rightrightarrows$    | `\rightrightarrows`    |
| $\leftrightarrows$   | `\leftrightarrows`   | $\rightleftarrows$     | `\rightleftarrows`     |
| $\Lleftarrow$        | `\Lleftarrow`        | $\Rrightarrow$         | `\Rrightarrow`         |
| $\twoheadleftarrow$  | `\twoheadleftarrow`  | $\twoheadrightarrow$   | `\twoheadrightarrow`   |
| $\leftarrowtail$     | `\leftarrowtail`     | $\rightarrowtail$      | `\rightarrowtail`      |
| $\leftrightharpoons$ | `\leftrightharpoons` | $\rightleftharpoons$   | `$\rightleftharpoons`  |
| $\Lsh$               | `\Lsh`               | $\Rsh$                 | `\Rsh`                 |
| $\looparrowleft$     | `\looparrowleft`     | $\looparrowright$      | `\looparrowright`      |
| $\curvearrowleft$    | `\curvearrowleft`    | $\curvearrowright$     | `\curvearrowright`     |
| $\circlearrowleft$   | `\circlearrowleft`   | $\circlearrowright$    | `\circlearrowright`    |
| $\upuparrows$        | `\upuparrows`        | $\downdownarrows$      | `\downdownarrows`      |
| $\upharpoonleft$     | `\upharpoonleft`     | $\upharpoonright$      | `\upharpoonright`      |
| $\downharpoonleft$   | `\downharpoonleft`   | $\downharpoonright$    | `\downharpoonright`    |
| $\rightsquigarrow$   | `\rightsquigarrow`   | $\leftrightsquigarrow$ | `\leftrightsquigarrow` |
| $\multimap$          | `\multimap`          |                        |                        |

## 点 (Dots)

| Symbol   | Command  | Symbol   | Command  |
| -------- | -------- | -------- | -------- |
| $\cdot$  | `\cdot`  | $\vdots$ | `\vdots` |
| $\dots$  | `\dots`  | $\ddots$ | `\ddots` |
| $\cdots$ | `\cdots` |          |          |

## 上标 (Accents)

| Symbol          | Command         | Symbol      | Command     | Symbol         | Command        |
| --------------- | --------------- | ----------- | ----------- | -------------- | -------------- |
| $\hat{x}$       | `$\hat{x}`      | $\check{x}$ | `\check{x}` | $\dot{x}$      | `\dot{x}`      |
| $\breve{x}$     | `\breve{x}`     | $\acute{x}$ | `\acute{x}` | $\ddot{x}$     | `\ddot{x}`     |
| $\grave{x}$     | `\grave{x}`     | $\tilde{x}$ | `\tilde{x}` | $\mathring{x}$ | `\mathring{x}` |
| $\bar{x}$       | `\bar{x}`       | $\vec{x}$   | `\vec{x}`   | $\overline{x}$ | `\overline{x}` |
| $\underline{x}$ | `\underline{x}` | $\dddot{x}$ | `\dddot{x}` | $\ddddot{x}$   | `\ddddot{x}`   |

When applying accents to `i` and `j`, you can use `\imath` and `\jmath` to keep the dots from interfering with the accents:

当对 `i` 和 `j` 应用上标时，可以使用 `\imath` 和 `\jmath` 来防止点干扰上标:

| Symbol         | Command        | Symbol         | Command        |
| -------------- | -------------- | -------------- | -------------- |
| $\vec{\jmath}$ | `\vec{\jmath}` | $\vec{\imath}$ | `\vec{\imath}` |

`\tilde` and `\hat` have wide versions that allow you to accent an expression:

`\tilde` 和 `\hat` 有很宽的版本，可以让你强调一个表达:

| Symbol          | Command         | Symbol            | Command           |
| --------------- | --------------- | ----------------- | ----------------- |
| $\widehat{7+x}$ | `\widehat{7+x}` | $\widetilde{abc}$ | `\widetilde{abc}` |

## 其他符号 (Other Symbols)

| Symbol               | Command              | Symbol           | Command          | Symbol            | Command           |
| -------------------- | -------------------- | ---------------- | ---------------- | ----------------- | ----------------- |
| $\infty$             | `\infty`             | $\triangle$      | `\triangle`      | $\angle$          | `\angle`          |
| $\aleph$             | `\aleph`             | $\hbar$          | `\hbar`          | $\imath$          | `\imath`          |
| $\jmath$             | `\jmath`             | $\ell$           | `\ell`           | $\wp$             | `\wp`             |
| $\Re$                | `\Re`                | $\Im$            | `\Im`            | $\mho$            | `\mho`            |
| $\prime$             | `\prime`             | $\emptyset$      | `\emptyset`      | $\nabla$          | `\nabla`          |
| $\surd$              | `\surd`              | $\partial$       | `\partial`       | $\top$            | `\top`            |
| $\bot$               | `\bot`               | $\vdash$         | `\vdash`         | $\dashv$          | `\dashv`          |
| $\forall$            | `\forall`            | $\exists$        | `\exists`        | $\neg$            | `\neg` or `\lnot` |
| $\flat$              | `\flat`              | $\natural$       | `\natural`       | $\sharp$          | `\sharp`          |
| $\backslash$         | `\backslash`         | $\Box$           | `\Box`           | $\Diamond$        | `\Diamond`        |
| $\clubsuit$          | `\clubsuit`          | $\diamondsuit$   | `\diamondsuit`   | $\heartsuit$      | `\heartsuit`      |
| $\spadesuit$         | `\spadesuit`         | $\Join$          | `\Join`          | $\blacksquare$    | `\blacksquare`    |
| $\S$                 | `\S`                 | $\circledR$      | `\circledR`      | $\implies$        | `\implies`        |
| $\P$                 | `\P`                 | $\therefore$     | `\therefore`     | $\because$        | `\because`        |
| $\checkmark$         | `\checkmark`         | $\mathbb{R}$     | `\mathbb{R}`     | $\eth$            | `\eth`            |
| $\backprime$         | `\backprime`         | $\square$        | `\square`        | $\cup$            | `\cup`            |
| $\bigstar$           | `\bigstar`           | $\in$            | `\in`            | $\sphericalangle$ | `\sphericalangle` |
| $\Vdash$             | `\Vdash`             | $\vDash$         | `\vDash`         | $\varnothing$     | `\varnothing`     |
| $\complement$        | `$\complement`       | $\vartriangle$   | `\vartriangle`   | $\hslash$         | `\hslash`         |
| $\Bbbk$              | `\Bbbk`              | $\circledS$      | `$\circledS`     | $\blacktriangle$  | `\blacktriangle`  |
| $\blacktriangledown$ | `\blacktriangledown` | $\Game$          | `\Game`          | $\lozenge$        | `\lozenge`        |
| $\blacklozenge$      | `\blacklozenge`      | $\measuredangle$ | `\measuredangle` | $\Finv$           | `\Finv`           |
| $$                   | `\nexists`           |                  |                  |                   |                   |

Note: `\cancer` and `\overarc{ABC}` do not work in the classroom.

## 命令符 (Command Symbols)

Some symbols are used in commands, so they need to be treated in a special way.

有些符号用于命令中，因此需要以特殊的方式处理它们。

| Symbol       | Command      | Symbol | Command | Symbol | Command | Symbol       | Command      |
| ------------ | ------------ | ------ | ------- | ------ | ------- | ------------ | ------------ |
| $\backslash$ | `\backslash` | $\&$   | `\&`    | $\%$   | `\%`    | $\#$         | `\#`         |
| $\_$         | `\_`         | $\{$   | `\{`    | $\}$   | `\}`    | $\backslash$ | `\backslash` |

## 括号 (Bracketing Symbols)

In mathematics, sometimes we need to enclose expressions in brackets, braces or parentheses. Some of these work just as you'd imagine in LaTeX; type `(` and `)` for parentheses, `[` and `]` for brackets, and `|` and `|` for absolute value. However, other symbols have special commands:

**定界符**

| Symbol       | Command           | Symbol    | Command   | Symbol    | Command         |
| ------------ | ----------------- | --------- | --------- | --------- | --------------- |
| $[$          | `[` or `\lbrack`  | $($       | `(`       | $|$       | `|` or `\vert`  |
| $\{$         | `\{` or `\lbrace` | $\}$      | `\}`      | $\|$      | `\|` or `\Vert` |
| $\backslash$ | `\backslash`      | $\lfloor$ | `\lfloor` | $\rfloor$ | `\rfloor`       |
| $\lceil$     | `\lceil`          | $\rceil$  | `\rceil`  | $\langle$ | `\langle`       |
| $\rangle$    | `\rangle`         |           |           |           |                 |

**用户行间公式的大定界符**

| Symbol        | Command       | Symbol       | Command       | Symbol        | Command       |
| ------------- | ------------- | ------------ | ------------- | ------------- | ------------- |
| $\lgroup$     | `\lgroup`     | $\rgroup$    | `\rgroup`     | $\lmoustache$ | `\lmoustache` |
| $\arrowvert$  | `\arrowvert`  | $\Arrowvert$ | `$\Arrowvert` | $\bracevert$  | `\bracevert`  |
| $\rmoustache$ | `\rmoustache` |              |               |               |               |

**AMS 定界符**

| Symbol      | Command     | Symbol      | Command     |
| ----------- | ----------- | ----------- | ----------- |
| $\ulcorner$ | `\ulcorner` | $\urcorner$ | `\urcorner` |
| $\llcorner$ | `\llcorner` | $\lrcorner$ | `\lrcorner` |

You might notice that if you use any of these to typeset an expression that is vertically large, like `(\frac{a}{x})^2`, the parentheses don't come out the right size:

您可能会注意到，如果使用其中任何一个来排版垂直较大的表达式，比如 `(\frac{a}{x})^2`，小括号的尺寸是不对的:
$$
(\frac{a}{x})^2
$$
If we put `\left` and `\right` before the relevant parentheses, we get a prettier expression: `\left(\frac{a}{x} \right)^2`, gives:

如果我们把 `\left` 和 `\right` 放在相关的括号前，我们会得到一个更漂亮的表达式:
`\left(\frac{a}{x} \right)^2` 会得到:
$$
\left(\frac{a}{x} \right)^2
$$
**放大括号的大小**

| Symbol                                              | Command                                             |
| --------------------------------------------------- | --------------------------------------------------- |
| $\big( \Big( \bigg( \Bigg($                         | `\big( \Big( \bigg( \Bigg(`                         |
| $\big] \Big] \bigg] \Bigg]$                         | `\big] \Big] \bigg] \Bigg]`                         |
| $\big\{ \Big\{ \bigg\{ \Bigg\{$                     | `\big\{ \Big\{ \bigg\{ \Bigg\{`                     |
| $\big\langle \Big\langle \bigg\langle \Bigg\langle$ | `\big\langle \Big\langle \bigg\langle \Bigg\langle` |
| $\big\rangle \Big\rangle \bigg\rangle \Bigg\rangle$ | `\big\rangle \Big\rangle \bigg\rangle \Bigg\rangle` |
| $\big| \Big| \bigg| \Bigg|$                         | `\big| \Big| \bigg| \Bigg|`                         |
| $\big\| \Big\| \bigg\| \Bigg\|$                     | `\big\| \Big\| \bigg\| \Bigg\|`                     |
| $\big\lceil \Big\lceil \bigg\lceil \Bigg\lceil$     | `\big\lceil \Big\lceil \bigg\lceil \Bigg\lceil`     |
| $\big\rceil \Big\rceil \bigg\rceil \Bigg\rceil$     | `\big\rceil \Big\rceil \bigg\rceil \Bigg\rceil`     |
| $\big\lfloor \Big\lfloor \bigg\lfloor \Bigg\lfloor$ | `\big\lfloor \Big\lfloor \bigg\lfloor \Bigg\lfloor` |
| $\big\rfloor \Big\rfloor \bigg\rfloor \Bigg\rfloor$ | `\big\rfloor \Big\rfloor \bigg\rfloor \Bigg\rfloor` |

## 跨行或跨列的符号

| Symbol                                                       | Command                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| $f(x) = \begin{cases} x^2 & x \ge 0 \\ x & x < 0 \end{cases}$ | `f(x) = \begin{cases} x^2 & x \ge 0 \\ x & x < 0 \end{cases}` |
| $\left\lceil\frac{x}{y}\right\rceil$                         | `\left\lceil\frac{x}{y}\right\rceil`                         |
| $\left\lfloor\frac{x}{y}\right\rfloor$                       | `\left\lfloor\frac{x}{y}\right\rfloor`                       |
| $\underbrace{a_0+a_1+a_2+\cdots+a_n}_{x}$                    | `\underbrace{a_0+a_1+a_2+\cdots+a_n}_{x}`                    |
| $\overbrace{a_0+a_1+a_2+\cdots+a_n}^{x}$                     | `\overbrace{a_0+a_1+a_2+\cdots+a_n}^{x}`                     |
| $\arg \underset{1\leq k \leq n} {\max} \frac{\lambda_k}{\lambda_{k+1}}$ | `\arg \underset{1\leq k \leq n} {\max} \frac{\lambda_k}{\lambda_{k+1}}` |

`\left` and `\right` can also be used to resize the following symbols:

`\left` 和 `\right` 也可以用来调整下列符号的大小:

| Symbol     | Command    | Symbol       | Command      | Symbol         | Command        |
| ---------- | ---------- | ------------ | ------------ | -------------- | -------------- |
| $\uparrow$ | `\uparrow` | $\downarrow$ | `\downarrow` | $\updownarrow$ | `\updownarrow` |
| $\Uparrow$ | `\Uparrow` | $\Downarrow$ | `\Downarrow` | $\Updownarrow$ | `\Updownarrow` |

## 不同尺寸的符号 (Multi-Size Symbols)

Some symbols render differently in inline math mode and in display mode. Display mode occurs when you use `\[...\]` or `$$...$$`, or environments like `\begin{equation}...\end{equation}`, `\begin{align}...\end{align}`.

| Symbol      | Command     | Symbol      | Command     | Symbol       | Command      |
| ----------- | ----------- | ----------- | ----------- | ------------ | ------------ |
| $\sum$      | `\sum`      | $\int$      | `\int`      | $\oint$      | `\oint`      |
| $\prod$     | `\prod`     | $\coprod$   | `\coprod`   | $\bigcap$    | `\bigcap`    |
| $\bigcup$   | `\bigcup`   | $\bigsqcup$ | `\bigsqcup` | $\bigvee$    | `\bigvee`    |
| $\bigwedge$ | `\bigwedge` | $\bigodot$  | `\bigodot`  | $\bigotimes$ | `\bigotimes` |
| $\bigoplus$ | `\bigoplus` | $\biguplus$ | `\biguplus` | $\iint$      | `\iint`      |
| $\iiint$    | `\iiint`    | $\iiiint$   | `\iiiint`   | $\idotsint$  | `\idotsint`  |

## 分数 (Fractions)

Use `\cfrac` for continued fractions.

` \cfrac{2}{1+\cfrac{2}{1+\cfrac{2}{1+\cfrac{2}{1}}}}`
$$
	\cfrac{2}{1+\cfrac{2}{1+\cfrac{2}{1+\cfrac{2}{1}}}}
$$

## 矩阵

| Symbol                                              | Command                                                      |
| --------------------------------------------------- | ------------------------------------------------------------ |
| $\begin{matrix} 1&2&3\\a&b&c\end{matrix}$           | `\begin{matrix} 1 & 2 & 3 \\ a & b & c \end{matrix}`         |
| $\begin{pmatrix} 1&2&3\\a&b&c\end{pmatrix}$         | `\begin{pmatrix} 1 & 2 & 3 \\ a & b & c \end{pmatrix}`       |
| $\begin{bmatrix} 1&2&3\\a&b&c\end{bmatrix}$         | `\begin{bmatrix} 1 & 2 & 3 \\ a & b & c \end{bmatrix}`       |
| $\begin{Bmatrix} 1&2&3\\a&b&c\end{Bmatrix}$         | `\begin{Bmatrix} 1 & 2 & 3 \\ a & b & c \end{Bmatrix}`       |
| $\begin{vmatrix} 1&2&3\\a&b&c\end{vmatrix}$         | `\begin{vmatrix} 1 & 2 & 3 \\ a & b & c \end{vmatrix}`       |
| $\begin{Vmatrix} 1&2&3\\a&b&c\end{Vmatrix}$         | `\begin{Vmatrix} 1 & 2 & 3 \\ a & b & c \end{Vmatrix}`       |
| $\begin{smallmatrix} 1&2&3\\a&b&c\end{smallmatrix}$ | `\begin{smallmatrix} 1 & 2 & 3 \\ a & b & c \end{smallmatrix}` (inline display) |

## 组合 (Combinations)

| Symbol            | Command           |
| ----------------- | ----------------- |
| $\binom{a}{b^2}$  | `\binom{a}{b^2}`  |
| $\dbinom{a}{b^2}$ | `\dbinom{a}{b^2}` |
| $\tbinom{a}{b^2}$ | `\tbinom{a}{b^2}` |

## 高级运算符

**极限 (Limits)**

| Symbol                                | Command                               |
| ------------------------------------- | ------------------------------------- |
| $\lim\limits_{x\to\infty}\frac{1}{x}$ | `\lim\limits_{x\to\infty}\frac{1}{x}` |

In Display mode, we use `\lim_{x\to\infty}\frac{1}{x}`
$$
\lim_{x\to\infty}\frac{1}{x}
$$
**三角函数 (Trigonometric Functions)**

| Symbol    | Command   | Symbol    | Command   | Symbol    | Command   |
| --------- | --------- | --------- | --------- | --------- | --------- |
| $\cos$    | `\cos`    | $\sin$    | `\sin`    | $\tan$    | `\tan`    |
| $\sec$    | `\sec`    | $\csc$    | `\csc`    | $\cot$    | `\cot`    |
| $\arccos$ | `\arccos` | $\arcsin$ | `\arcsin` | $\arctan$ | `\arctan` |
| $\cosh$   | `\cosh`   | $\sinh$   | `\sinh`   | $\tanh$   | `\tanh`   |
| $\coth$   | `\coth`   |           |           |           |           |

**其他**

| Symbol                | Command               | Symbol               | Command              | Symbol                | Command               |
| --------------------- | --------------------- | -------------------- | -------------------- | --------------------- | --------------------- |
| $\exp$                | `\exp`                | $\min$               | `\min`               | $\max$                | `\max`                |
| $\dim$                | `\dim`                | $\lg$                | `\lg`                | $\ln$                 | `\ln`                 |
| $\log$                | `\log`                | $\arg$               | `\arg`               | $\ker$                | `\ker`                |
| $\limsup$             | `\limsup`             | $\liminf$            | `\liminf`            | $\Pr$                 | `\Pr`                 |
| $\hom$                | `\hom`                | $\operatorname{dom}$ | `\operatorname{dom}` | $\operatorname{ran}$  | `\operatorname{ran}`  |
| $\gcd$                | `\gcd`                | $\deg$               | `\deg`               | $\operatorname{proj}$ | `\operatorname{proj}` |
| $\operatorname{span}$ | `\operatorname{span}` | $\operatorname{tr}$  | `\operatorname{tr}`  | $\det$                | `\det`                |
| $\sup$                | `\sup`                | $\inf$               | `\inf`               |                       |                       |

**微积分 (Calculus)**

Below are examples of calculus expressions rendered in LaTeX. Most of these commands have been introduced before. Notice how definite integrals are rendered (and the difference between inline math and display mode for definite integrals). The `\,` in the integrals makes a small space before the `dx`.

| Symbol                                                       | Command                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| $\frac{\mathrm{d}}{\mathrm{d} x}\left(x^2\right) = 2x$       | `\frac{\mathrm{d}}{\mathrm{d} x}\left(x^2\right) = 2x`       |
| $\int 2x\,\mathrm{d}x = x^2+C$                               | `\int 2x\,\mathrm{d}x = x^2+C`                               |
| $ \int^5_1 2x\,dx = 24$                                      | ` \int^5_1 2x\,dx = 24`                                      |
| $ \frac{\partial^2U}{\partial x^2} + \frac{\partial^2U}{\partial y^2}$ | ` \frac{\partial^2U}{\partial x^2} + \frac{\partial^2U}{\partial y^2}` |
| $\frac{1}{4\pi}\oint_\Sigma\frac{1}{r}\frac{\partial U}{\partial n} ds$ | `\frac{1}{4\pi}\oint_\Sigma\frac{1}{r}\frac{\partial U}{\partial n} ds` |

$$
\begin{gather*}
	\iint_V \mu(u,v) \,du\,dv \\
	\iiint_V \mu(u,v,w) \,du\,dv\,dw \\
	\iiiint_V \mu(t,u,v,w) \,dt\,du\,dv\,dw \\
	\idotsint_V \mu(u_1,\dots,u_k) \,du_1 \dots du_k
\end{gather*}
$$

**同余 (Mods)**

| Symbol               | Command              |
| -------------------- | -------------------- |
| $9\equiv 3 \bmod{6}$ | `9\equiv 3 \bmod{6}` |
| $9\equiv 3 \pmod{6}$ | `9\equiv 3 \pmod{6}` |
| $9\equiv 3 \mod{6}$  | `9\equiv 3 \mod{6}`  |
| $9\equiv 3 \pod{6}$  | `9\equiv 3 \pod{6}`  |

## 数学间距控制

- `\quad`: space equal to the current font size (=18 mu)
- `\,`: $3/18$ of `/quad` (=3 mu)
- `\:`: $4/18$ of `/quad` (=4 mu)
- `\;`: $5/18$ of `/quad` (=5 mu)
- `\!`: $-3/18$ of `/quad` (=-3 mu)
- `\ ` (space after backslash!): equivalent of space in normal text
- `\qquad`: twice of `\quad` (=36 mu)

| Symbol       | Command      |
| ------------ | ------------ |
| $a=1 \\ b=2$ | `a=1 \\ b=2` |
| $a \qquad b$ | `a \qquad b` |
| $a \quad b$  | `a \quad b`  |
| $a\ b$       | `a\ b`       |
| $a\; b$      | `a\; b`      |
| $a\: b$      | `a\: b`      |
| $a\, b$      | `a\, b`      |
| $a\! b$      | `a\! b`      |
| $ab$         | `ab`         |

## 对齐

**展示长公式**

`\begin{multline*}` + `公示内容` + 中间用 `\\` 分行 + `\end{multline*}`

```latex
\begin{multline*}
p(x) = 3x^6 + 14x^5y + 590x^4y^2 + 19x^3y^3 \\
- 12x^2y^4 - 12xy^5 + 2y^6 = a^3b^3
\end{multline*}
```

$$
\begin{multline*}
p(x) = 3x^6 + 14x^5y + 590x^4y^2 + 19x^3y^3 \\
- 12x^2y^4 - 12xy^5 + 2y^6 = a^3b^3
\end{multline*}
$$

**拆分、对其方程**

`\begin{align*}` + 公示内容 + 换行符`\\` + 对齐符`&` + `\end{align*}` 

```latex
\begin{align*}
x&=y		&	w&=z				&	a&=b+c \\
2x&=-y		&	3w&=\frac{1}{2}z	&	a&=b \\
-4+5x&=2+y	&	w+2&=-1+w			&	ab&=cb
\end{align*}
```

$$
\begin{align*}
x&=y		&	w&=z				&	a&=b+c \\
2x&=-y		&	3w&=\frac{1}{2}z	&	a&=b \\
-4+5x&=2+y	&	w+2&=-1+w			&	ab&=cb
\end{align*}
$$

**居中显示方程 (不以等号对齐)**

使用 `{gather*}`

```latex
\begin{gather*}
2x - 5y = 8 \\
3x^2 + 9y = 3a + c
\end{gather*}
```

$$
\begin{gather*}
2x - 5y = 8 \\
3x^2 + 9y = 3a + c
\end{gather*}
$$

## 数学字体 (Mathematical fonts)

**Capital letters-only font typefaces**

There are some font typefaces which support only a limited number of characters; these fonts usually denote some special sets. For instance, to display the $R$ in blackboard bold typeface you can use `$\mathbb{R}$` to produce $\mathbb{R}$. The following example shows calligraphic, fraktur and blackboard bold typefaces:

```latex
\begin{align*}
RQSZ \\
\mathcal{RQSZ} \\
\mathfrak{RQSZ} \\
\mathbb{RQSZ} \\
\mathscr{RQSZ}
\end{align*}
```

$$
\begin{align*}
RQSZ \\
\mathcal{RQSZ} \\
\mathfrak{RQSZ} \\
\mathbb{RQSZ} \\
\mathscr{RQSZ}
\end{align*}
$$

**Other mathematical fonts**

It is possible to set a different font family for a complete mathematical expression:

```latex
\begin{align*}
3x^2 \in R \subset Q \\
\mathnormal{3x^2 \in R \subset Q} \\
\mathrm{3x^2 \in R \subset Q} \\
\mathit{3x^2 \in R \subset Q} \\
\mathbf{3x^2 \in R \subset Q} \\
\mathsf{3x^2 \in R \subset Q} \\
\mathtt{3x^2 \in R \subset Q}
\end{align*}
```

$$
\begin{align*}
3x^2 \in R \subset Q \\
\mathnormal{3x^2 \in R \subset Q} \\
\mathrm{3x^2 \in R \subset Q} \\
\mathit{3x^2 \in R \subset Q} \\
\mathbf{3x^2 \in R \subset Q} \\
\mathsf{3x^2 \in R \subset Q} \\
\mathtt{3x^2 \in R \subset Q}
\end{align*}
$$

## 字体字形设置

| Symbol          | Command         | Symbol              | Command             |
| --------------- | --------------- | ------------------- | ------------------- |
| $\boxed{text}$  | `\boxed{text}`  | $\boldsymbol{text}$ | `\boldsymbol{text}` |
| $\fbox{text}$   | `\fbox{text}`   | $A \large{A}$       | `A \large{A}`       |
| $\mathbf{text}$ | `\mathbf{text}` | $A \small{A}$       | `A \small{A}`       |
| $\bold{text}$   | `\bold{text}`   |                     |                     |

## 特殊数学公式

| Symbol                             | Command                            | Comment                                    |
| ---------------------------------- | ---------------------------------- | ------------------------------------------ |
| $\sideset{^1_2}{^3_4}\bigotimes$   | `$\sideset{^1_2}{^3_4}\bigotimes`  | 左右都有上下标                             |
| ${}^{12}_{\phantom{1}6}\textrm{C}$ | `{}^{12}_{\phantom{1}6}\textrm{C}` | 上下标在左边                               |
| $1+\frac{a}{\frac{b}{c}+1}$        | `1+\frac{a}{\frac{b}{c}+1}`        | 分数，字体会逐渐变小                       |
| $1+\cfrac{a}{\cfrac{b}{c}+1}$      | `1+\cfrac{a}{\cfrac{b}{c}+1}`      | 分数，字体不会变小                         |
| $1+\frac{a}{\dfrac{b}{c}+1}$       | `1+\frac{a}{\dfrac{b}{c}+1}`       | 分数，字号为独立公式的大小                 |
| $1+\frac{a}{\tfrac{b}{c}+1}$       | `1+\frac{a}{\tfrac{b}{c}+1}`       | 分数，字号为行间公式的大小                 |
| $\stackrel{a}{b}$                  | `\stackrel{a}{b}`                  | 下面字符大，上面字符小                     |
| ${a \atop b+c}$                    | `{a \atop b+c}`                    | 上下符号等大                               |
| ${a \choose b+c}$                  | `{a \choose b+c}`                  | 上下符号等大                               |
| $\sum\limits_{i=a}^{b} c_i$        | `\sum\limits_{i=a}^{b} c_i`        | 不压缩表示，独立公式默认                   |
| $\sum\nolimits_{i=a}^{b} c_i$      | `\sum\nolimits_{i=a}^{b} c_i`      | 压缩表示，行间公式默认                     |
| $\displaystyle\sum_{i=1}^{b} c_i$  | `\displaystyle\sum_{i=1}^{b} c_i`  | `\displaystyle` 强制转换为行间公式显示模式 |
| $\xleftarrow[x+y]{x}$              | `\xleftarrow[x+y]{x}`              | 可自行调整                                 |
| $\xrightarrow[x+y]{x}$             | `\xrightarrow[x+y]{x}`             | 可自行调整                                 |
| $\overset{x+y}{\rightarrow}$       | `\overset{x+y}{\rightarrow}`       | 长度固定，适用单字符                       |
| $\underset{x+y}{\rightarrow}$      | `\underset{x+y}{\rightarrow}`      | 长度固定，适用单字符                       |
| $\underrightarrow{x+y}$            | `\underrightarrow{x+y}`            | 长度不固定，适用多字符                     |
| $\underrightarrow{x+y}$            | `\underrightarrow{x+y}`            | 长度不固定，适用多字符                     |
| $\overleftarrow{x+y}$              | `\overleftarrow{x+y}`              | 长度不固定，适用多字符                     |
| $\bar{a}$                          | `\bar{a}`                          | 单个字母上面加横线                         |
| $\overline{a+b}$                   | `\overline{a+b}`                   | 多个字母上面加横线                         |
| $\overbrace{a\dots a}^{n}$         | `\overbrace{a\dots a}^{n}`         | 括号在上面                                 |
| $\underbrace{a\dots a}_{n}$        | `\underbrace{a\dots a}_{n}`        | 括号在下面                                 |
| $y=x^2 (\text{二次方程})$          | `y=x^2 (\text{二次方程})`          | 公式中插入文本                             |
| $y=x^2 (\mbox{二次方程})$          | `y=x^2 (\mbox{二次方程})`          | 公式中插入文本                             |
| $\gcd(35,14)=7$                    | `\gcd(35,14)=7`                    | Greatest common factor                     |
| $\deg(2x^2+3x+5)=2$                | `\deg(2x^2+3x+5)=2`                | Degree of polynomial                       |
| $\angle ABC$                       | `\angle ABC`                       | Angle                                      |
| $\measuredangle ABC$               | `\measuredangle ABC`               | Measure of angle                           |
| $\pi \mathrm{rad}=180^{\circ}$     | `\pi \mathrm{rad}=180^{\circ}`     | Radian                                     |

用 `$$` 显示公式，可以自动居中，括号必须成对出现，如果在一行中只有一半的括号，则要添加对应的"影子括号"，例如在一行中有 `\left(`，则要在后面添加 `\right.`，同理有 `\left.` 和 `\right)`。

```latex
\begin{aligned}
	a =& \left(1+2+3+ \cdots \right. \\
	& \cdots+ \left. \infty-2+\infty-1+\infty\right)
\end{aligned}
```

$$
\begin{aligned}
	a =& \left(1+2+3+ \cdots \right. \\
	& \cdots+ \left. \infty-2+\infty-1+\infty\right)
\end{aligned}
$$

**分隔符 `\middle` 的作用**

```latex
P=\left(A=2|\frac{A^2}{B}>4\right) \\
P=\left(A=2\middle|\frac{A^2}{B}>4\right)
```

$$
P=\left(A=2|\frac{A^2}{B}>4\right) \\
P=\left(A=2\middle|\frac{A^2}{B}>4\right)
$$

**`case` 环境**

在单行文本中，不是只能写一行公式，只是整个公式占用一行

```latex
L(Y,f(X))=
\begin{cases}
	1,\quad &Y\neq f(X) \\
	0,\quad &Y=f(X)
\end{cases}
```

$$
L(Y,f(X))=
\begin{cases}
	1,\quad &Y\neq f(X) \\
	0,\quad &Y=f(X)
\end{cases}
$$

这里用到了 `cases` 环境，把多个情况放在一个公式中，每个情况用 `\\` 换行

**`equation` 环境**

`equation` 环境，自动居中对齐，带有公式编号

```latex
\begin{equation}f(x)=3x^{2}+6(x-2)-1\end{equation}
```

$$
\begin{equation}f(x)=3x^{2}+6(x-2)-1\end{equation}
$$

在 `equation` 环境中添加 `aligned` 环境，可以添加多行公式，每一行用 `\\` 分隔结束

```latex
\begin{equation}
\begin{aligned}
	f(x) &= (x+a)(x+b) \\
	&= x^2 + (a+b)x + ab
\end{aligned}
\end{equation}
```

$$
\begin{equation}
\begin{aligned}
	f(x) &= (x+a)(x+b) \\
	&= x^2 + (a+b)x + ab
\end{aligned}
\end{equation}
$$

```latex
\begin{equation}
\begin{aligned}
	x=&\left( a+b+c+ \right. \\
	&\left. d+e+f+g \right) a
\end{aligned}
\end{equation}
```

$$
\begin{equation}
\begin{aligned}
	x=&\left( a+b+c+ \right. \\
	&\left. d+e+f+g \right) a
\end{aligned}
\end{equation}
$$

有时候需要方程组，把多个公式放在一起

```latex
\left.
\begin{aligned}
	x+y &> 5 \\
	y-y &> 11
\end{aligned}
\right\} \Rightarrow x^2 - y^2 > 55
```

$$
\left.
\begin{aligned}
	x+y &> 5 \\
	y-y &> 11
\end{aligned}
\right\} \Rightarrow x^2 - y^2 > 55
$$

还可以把括号放在左边，只需要换一下"影子括号"位置就可以了。

**`array` 环境**

在 `equation` 环境中添加 `array` 环境，就可以实现数组或者表格的形式，其中每个元素用 `&` 分隔，竖直分割线 在定义式中插入 `|`，(`||` 表示两条竖直分割线)，水平分割线 在下一行输入前插入 `\hline`

```latex
\begin{equation}
\begin{array}{c|l|c|r}
	n & \text{左对齐} & \text{居中对齐} & \text{右对齐} \\\hline
	1 & 0.24 & 1 & 125 \\\hline
	2 & -1 & 189 & -8 \\\hline
	3 & -20 & 2000 & 1+10i
\end{array}\end{equation}
```

$$
\begin{equation}
\begin{array}{c|l|c|r}
	n & \text{左对齐} & \text{居中对齐} & \text{右对齐} \\\hline
	1 & 0.24 & 1 & 125 \\\hline
	2 & -1 & 189 & -8 \\\hline
	3 & -20 & 2000 & 1+10i
\end{array}\end{equation}
$$

公式中如果有中文，就要用 `\text{}` 或者 `\mbox{}` 装载，否则不能正常输出中文。
单行文本也可以表示矩阵和公式数组

```latex
\left(\begin{array}{ccc|c}
	a11 & a12 & a13 & b1 \\
	a21 & a22 & a23 & b2 \\
	a31 & a32 & a33 & b3
\end{array}\right)
```

$$
\left(\begin{array}{ccc|c}
	a11 & a12 & a13 & b1 \\
	a21 & a22 & a23 & b2 \\
	a31 & a32 & a33 & b3
\end{array}\right)
$$

```latex
\left\{\begin{array}{c}
	a_1x+b_1y+c_1z=d_1 \\
	a_2x+b_2y+c_2z=d_2 \\
	a_3x+b_3y+c_3z=d_3
\end{array}\right.
```

$$
\left\{\begin{array}{c}
	a_1x+b_1y+c_1z=d_1 \\
	a_2x+b_2y+c_2z=d_2 \\
	a_3x+b_3y+c_3z=d_3
\end{array}\right.
$$

**数学公式的序号与引用**

```latex
\begin{equation} \label{eq:eps} \tag{1}
    \epsilon > 0
\end{equation}
```

$$
\begin{equation} \label{eq:eps} \tag{1}
    \epsilon > 0
\end{equation}
$$

From ($\ref{eq:eps}$), we can easily draw a conclusion that $\ldots$

## Reference

> https://artofproblemsolving.com/wiki/index.php/LaTeX:Symbols
>
> https://artofproblemsolving.com/wiki/index.php/LaTeX:Commands
>
> https://zhuanlan.zhihu.com/p/464237097
>
> https://zhuanlan.zhihu.com/p/443086245
>
> https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols
