# from flask import Flask,render_template
# from pyecharts.charts import Bar
#
#
# app = Flask(__name__)
#
#
#
#
# @app.route("/")
# def show_pyecharts():
#   bar = (
#     Bar()
#       .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#       .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#   )
#
#   # print(bar.dump_options())
#   return render_template(
#     "show_pyecharts.html",
#     bar_data=bar.dump_options()
#   )
#
# if __name__ == "__main__":
#     app.run()