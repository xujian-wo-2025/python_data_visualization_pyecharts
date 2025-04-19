# 导包，导入Line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建 Line 对象
line = Line()

# 添加 x 轴数据
line.add_xaxis(['中国', '美国', '英国'])

# 正确调用 add_yaxis 方法，分别传入系列名称和 y 轴数据
line.add_yaxis(series_name="GDP", y_axis=[30, 20, 10])

# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 渲染图表，生成一个 HTML 文件
line.render("gdp_line_chart.html")
