## iframe-resizer 使用说明

* 主页面
    - 引入 `iframeResizer.min.js`, 对需要调整的iframe调用 `iFrameResize()`方法
* iFrame页面
    - 引入 `iframeResizer.contentWindow.min.js`
    - 在contentWindow的js引入之前，设置全区变量`iFrameResizer`, 用于修改默认行为（比如：高度修正）