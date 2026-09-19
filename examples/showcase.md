# 日常笔记与长文阅读

这份样张用于比较三套主题的真实编辑效果。正文均为 **16 px**，日常白底和黑底采用 Open Sans 与思源黑体，暗红主题采用 Source Serif 4 与思源宋体。

## 1. 文字与超链接

今天整理项目资料，记录问题、判断与下一步行动。好的排版应让注意力停留在内容上：中文清楚，英文自然，数字容易辨认。查看 [Typora 使用文档](https://support.typora.io/)，或者回到 [本文的代码示例](#3-代码与行内命令)。

Typography for everyday writing. A clear paragraph helps you read, think, and revise. Markdown, API, GitHub, version 2.5.1 — 0123456789 / Il1 O0 rn m.

这里包含**需要强调的结论**、*英文斜体 emphasis*、~~已废弃的内容~~和 `inline_code()`。标点检查：「引号」、（括号）、省略号……、破折号——。

> 引用保留淡底和左侧边线。我们希望保持适中的信息密度，也能轻松回看之前写下的结论。
>
> 第二段引用用于检查段落之间的距离。

### 下一步行动

- 整理资料，记录问题和判断。
- 保留依据，让下一次回看更轻松。
  - 嵌套列表保持清楚的缩进。
  - 子项之间不额外拉开大段空白。

1. 打开这份样张。
2. 在主题菜单中依次选择 Cutelemon6 Day、Cutelemon6 Night、Cutelemon6 Editorial。
3. 比较普通正文、中文粗体和英文数字的效果。

- [x] 统一正文大小
- [x] 明确浅色与深色链接颜色
- [ ] 按实际使用体验微调

## 2. 表格与信息密度

| 主题 | 正文字体 | 链接颜色 | 用途 |
| --- | --- | --- | --- |
| Cutelemon6 Day | Open Sans＋思源黑体 | 墨青 | 日常白底编辑 |
| Cutelemon6 Night | Open Sans＋思源黑体 | 石墨蓝的浅色版本 | 夜间编辑 |
| Cutelemon6 Editorial | Source Serif 4＋思源宋体 | 墨青 | 暗红标题长文 |

较长的表格单元格也应自然换行，不把编辑区域撑得过宽。配置键名例如 `max_output_tokens` 应与中文解释保持清楚的视觉区分。

## 3. 代码与行内命令

行内命令 `python3 example.py --mode review` 使用等宽字体。多行代码使用独立的背景、较小字号和克制的语法高亮。

```python
from pathlib import Path

def summarize(notes: list[str]) -> dict[str, int]:
    # 中文注释应保持清楚，不受正文宋体影响。
    return {
        "documents": len(notes),
        "characters": sum(len(note) for note in notes),
    }

print(summarize(["清楚的正文", "稳定的层次"]))
```

```bash
python3 example.py --mode review --output notes.json
```

### 公式与脚注



行内公式 $E = mc^2$ 与正文保持适中的距离。块公式用于检查数学渲染是否沿用 Typora 的原生排版：

$$
\operatorname{softmax}(x_i)=\frac{e^{x_i}}{\sum_j e^{x_j}}
$$

正文中的补充说明可以放到脚注。[^note]

#### 四级标题

四级标题保持与正文接近的尺寸，用字重和间距建立次级结构。

---

[^note]: 字体文件随主题提供。PDF 打印使用白底，黑底主题的打印样式也会切回白底。
