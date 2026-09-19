# Third-party notices / 第三方来源与授权

[English README](README.md) · [中文 README](README.zh-CN.md)

## Scope of MIT / MIT 的适用范围

The repository's MIT license covers its original theme CSS, documentation, specimen text, preview page, scripts, and preview images. It does **not** replace the licenses of bundled fonts. Each font retains its original copyright notices and license. Preview images are rendered from this project's own specimen and theme files.

仓库的 MIT 授权适用于原创主题 CSS、文档、样张文字、预览页面、脚本和预览图；**不覆盖第三方字体，也不改变字体的原始许可**。预览图使用本项目自己的样张和主题文件渲染。

## Bundled fonts / 随包字体

| Family | Included styles | Source | License |
| --- | --- | --- | --- |
| Open Sans | Regular, Bold, Italic, Bold Italic | [Typora's official default-theme font assets](https://github.com/typora/typora-default-themes/tree/master/themes/github), original Open Sans design | [Apache 2.0](themes/cutelemon6/licenses/Open-Sans-Apache-2.0.txt) |
| Source Han Sans CN / 思源黑体 | Regular, Medium, Bold, version 2.005 | [Adobe Source Han Sans](https://github.com/adobe-fonts/source-han-sans) | [SIL OFL 1.1](themes/cutelemon6/licenses/Source-Han-Sans-OFL.txt) |
| Source Han Serif CN / 思源宋体 | Medium, SemiBold, version 2.003 | [Adobe Source Han Serif](https://github.com/adobe-fonts/source-han-serif) | [SIL OFL 1.1](themes/cutelemon6/licenses/Source-Han-Serif-OFL.txt) |
| Source Serif 4 | Regular, Semibold, Italic; standard Text optical design | [Adobe Source Serif releases](https://github.com/adobe-fonts/source-serif/tree/release/WOFF2/TTF) | [SIL OFL 1.1](themes/cutelemon6/licenses/Source-Serif-4-OFL.txt) |

The Open Sans files identify their copyright as “Digitized data copyright © 2010-2011, Google Corporation” and reference Apache 2.0 in their metadata. The complete license is included. The other families retain their Adobe copyright metadata and OFL notices.

Open Sans 文件的元数据包含 Google Corporation 的 2010–2011 年版权声明及 Apache 2.0 许可地址，仓库同时附带完整许可文本。其余字体保留 Adobe 版权元数据及相应 OFL 声明。

## Binary provenance / 字体文件身份

All font binaries in this repository are unmodified copies of upstream files. The Chinese fonts retain their original OTF format; Open Sans retains upstream WOFF; Source Serif 4 retains Adobe's original WOFF2 files. This project does not subset, instantiate, rename internally, or re-encode these distributed binaries. Descriptive filenames and CSS family aliases identify their use in the themes without changing the font data.

本仓库中的字体二进制文件均直接复制自上游：中文字体保留原始 OTF，Open Sans 保留原始 WOFF，Source Serif 4 使用 Adobe 提供的原始 WOFF2。本项目没有对这些发布文件裁字、生成静态实例、改写内部名称或重新编码。文件名和 CSS 字体别名只用于组织主题资源，不改变字体数据。

[`font-manifest.json`](font-manifest.json) records the download location, embedded family/version/copyright information, mapped character count, and SHA-256 of each file. `python3 scripts/check.py` verifies the local files against this manifest. The upstream repositories may reorganize downloads; the hashes identify the versions shipped here.

[`font-manifest.json`](font-manifest.json)记录每个文件的下载来源、内部字体名称、版本、版权、字符映射数量和 SHA-256。运行 `python3 scripts/check.py` 可以核对本地文件是否与清单一致。上游下载路径可能调整，校验值用于确定本仓库实际提供的版本。

## Reuse and redistribution / 使用与再分发

Keep the font license files, copyright notices, and this attribution when redistributing the theme package. Font modifications, subsetting, and format changes require a new review of the applicable license, including any Reserved Font Name restrictions. Fonts remain under their own licenses even when bundled with MIT-licensed code.

再次分发主题包时，请保留字体许可、版权声明和来源说明。若继续修改字体、裁字或转换格式，需要重新检查对应许可及保留字体名限制。字体与 MIT 代码一同提供时，仍然遵循其自身授权。

The OFL's [WOFF guidance](https://openfontlicense.org/ofl-faq/) distinguishes unchanged compression from modified font software. Shipping upstream binaries unchanged keeps that distinction explicit in this repository. Apache 2.0's [redistribution conditions](https://www.apache.org/licenses/LICENSE-2.0#redistribution) apply to the bundled Open Sans version.

## Names and acknowledgments / 名称与致谢

Typora, Adobe, Google, and the font family names identify the relevant products and sources. Their owners do not sponsor or endorse this project. This repository does not include the Typora application, another theme's CSS, third-party theme screenshots, or externally supplied document content.

Typora、Adobe、Google 及字体名称用于说明相关产品与来源，不表示获得这些权利人的赞助或背书。仓库不包含 Typora 应用程序、其他主题的 CSS、第三方主题截图或外部提供的文稿内容。
