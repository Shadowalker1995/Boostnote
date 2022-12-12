# SVM 中的常见问题解答

## Derivation of SVM formula's original form

<img src="https://cdn.jsdelivr.net/gh/Shadowalker1995/images/2021/cap_SVM-1_00:11:03_01.jpg" alt="cap_SVM-1_00:11:03_01" style="zoom:=50%;" />

对于超平面方程 $g(\boldsymbol{x}) = \boldsymbol{w}^T \boldsymbol{x} + b$.

- $\boldsymbol{w}$ 就是该超平面的法向量. 在超平面 $g(\boldsymbol{x})$ 上任取两点, $\boldsymbol{x}_1$ 和 $\boldsymbol{x}_2$, 则有:
    $$
    \begin{equation}
    \boldsymbol{w}^T \boldsymbol{x}_1 + b = 0 \\
    \boldsymbol{w}^T \boldsymbol{x}_2 + b = 0 \\
    \boldsymbol{w}^T (\boldsymbol{x}_1 - \boldsymbol{x}_2) = 0
    \end{equation}
    $$

- 原点到超平面的"距离"为 $\frac{-b}{\|\boldsymbol{w}\|}$. 过原点作超平面的垂线,垂足为点 $\boldsymbol{x}_1$, 则可令 $\boldsymbol{x}_1 = \lambda \frac{\boldsymbol{w}}{\|\boldsymbol{w}\|}$ , 带入 $g(\boldsymbol{x})$ 中, 有:
    $$
    \lambda \boldsymbol{w}^T \frac{\boldsymbol{w}}{\|\boldsymbol{w}\|} + b = 0
    $$
    化简, 得:
    $$
    \text{offset} \ \lambda = \frac{-b}{\|\boldsymbol{w}\|}
    $$

- 超平面外一点 $\boldsymbol{x}$ 到超平面的距离 $r = \frac{|\boldsymbol{w}^T \boldsymbol{x} + b|}{\|\boldsymbol{w}\|}$. 过原点作一与 $g(\boldsymbol{x})$ 平行的超平面. 则距离 $r$ 可以看作点 $\boldsymbol{x}$ 到这个过原点的超平面的距离减去这两个超平面之间的距离:
    $$
    \begin{equation} \begin{aligned}
    r &= \Bigg\| \frac{\boldsymbol{w}^T}{\|\boldsymbol{w}\|} \cdot \boldsymbol{x} \cdot \frac{\boldsymbol{w}}{\|\boldsymbol{w}\|} - \frac{-b}{\|\boldsymbol{w}\|} \cdot \frac{\boldsymbol{w}}{\|\boldsymbol{w}\|} \Bigg\| \\
    &= \Big\| \frac{\boldsymbol{w}^T\boldsymbol{x}}{\|\boldsymbol{w}\|^2} + \frac{b}{\|\boldsymbol{w}\|^2} \Big\| \| \boldsymbol{w} \| \\
    &= \frac{|\boldsymbol{w}^T\boldsymbol{x} + b|}{\| \boldsymbol{w} \|}
    \end{aligned} \end{equation}
    $$
