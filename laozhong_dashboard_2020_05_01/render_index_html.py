#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie,Page,Line
from pyecharts.globals import ThemeType
import get_data
import datetime
with open("index_temp.html","r") as f:
    f.readline().rstrip("\n      bg")
    index_content = f.read()
    f.close()
def line_center(width,height,title,date,view):
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width=width,height=height))
        .add_xaxis(date)
        .add_yaxis("哔哩哔哩", view)
        # .add_yaxis("YouTube", [3,2,55,4,5])
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
        )
    )
    return c
def line_left(width,height,title,date,data):
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width=width,height=height))
        .add_xaxis(date)
        .add_yaxis(title, data)
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(
        yaxis_opts=opts.AxisOpts(name="单位:/千人",
            axislabel_opts=opts.LabelOpts(formatter="{value} K"),
        ),
    )
    )
    return c
def line_right(width,height,title,date,data):
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width=width,height=height))
        .add_xaxis(date)
        .add_yaxis(title, data)
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=True),
        )
    )
    return c
def bottom_all(width,height,title,date,view,follower,likes,video_count):
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width=width,height=height))
        .add_xaxis(date)
        .add_yaxis(
            series_name="被关注数",
            stack="总量",
            y_axis=follower,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="点赞数",
            stack="总量",
            y_axis=likes,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="视频总数",
            stack="总量",
            y_axis=video_count,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="播放总数",
            stack="总量",
            y_axis=view,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )

    )
    return c
def get_date():
    date = list()
    for i in range(5):
        date.append((datetime.date.today() + datetime.timedelta(days = -i)).strftime("%m月%d日"))
    return date
def write_html_to_file(format_content):
    with open("index.html","w+") as f:
        f.write(format_content) 
        f.close
def main():
    get_data.spider().insert_testdata() #如果数据不存在，插入前五天的测试数据
    date = get_date()[::-1] # 获取五天的日期
    # get_data.spider().spider_get_data()
    data = get_data.spider().select_data()[::-1] # 爬取哔哩哔哩 用户数据
    view = [x[1] for x in data[1:]] # 从用户数据提取 播放数
    follower = [x[2] for x in data[1:]] # 从用户数据提取 关注数
    likes =[x[3] for x in data[1:]] # 从用户数据提取 点赞数
    video_count =[x[4] for x in data[1:]] # 从用户数据提取 视频播放数
    view_six_day = [x[1] for x in data]
    view_sub = [(view_six_day[x+1]-view_six_day[x])/1000 for x in range(len(view_six_day)-1)]
    follower_six_day = [x[2] for x in data]
    follower_sub = [follower_six_day[x+1]-follower_six_day[x] for x in range(len(follower_six_day)-1)]
    # 开始画图并生成html
    # "256px","325px"
    all = line_center("533px","325px","总曝光量",date,view).render_html_content(template_name="temp.html")
    line_left_bilibili = line_left("310px","325px","新增播放",date,view_sub).render_html_content(template_name="temp.html")
    line_right_bilibili = line_right("310px","325px","新增关注",date,follower_sub).render_html_content(template_name="temp.html")
    bottom = bottom_all("1226px","600px","新增数",date,view,follower,likes,video_count).render_html_content(template_name="temp.html")
    format_content = index_content.format(all=all,line_left_bilibili=line_left_bilibili,line_right_bilibili=line_right_bilibili,bottom_all=bottom)
    write_html_to_file(format_content)
    print("index.html生成成功")
if __name__ == '__main__':
    main()