from flask import Flask, render_template, send_file
from API_preproc import candlestick_graph, tableRender
from plotly.offline import plot


app = Flask(__name__)


@app.route('/',methods=("POST","GET"))
def dashboard():
    apple = graphGeneratorApple()
    amazon = graphGeneratorAmazon()
    microsoft = graphGeneratorMicrosoft()
    nvidia = graphGeneratorNvidia()
    lyft = graphGeneratorLyft()
    warner = graphGeneratorWarner()
    tesla = graphGeneratorTesla()
    paramount = graphGeneratorParamount()
    meta = graphGeneratorMeta()
    intel = graphGeneratorIntel()
    return render_template('dashboard.html', chart1=apple, chart2=amazon, chart3=microsoft, chart4=nvidia
                           , chart5=lyft, chart6=warner, chart7=tesla, chart8=paramount, chart9=meta
                           , chart10=intel,table1=[tableRender('AAPL').to_html(classes='data',header=True,index=False,justify='center',escape=False)]
                           ,table2=[tableRender('AMZN').to_html(classes='data',header=True,index=False,justify='center')]
                           ,table3=[tableRender('MSFT').to_html(classes='data',header=True,index=False,justify='center')]
                           ,table4=[tableRender('NVDA').to_html(classes='data',header=True,index=False,justify='center')]
                           ,table5=[tableRender('LYFT').to_html(classes='data',header=True,index=False,justify='center')]
                           ,table6=[tableRender('WBD').to_html(classes='data',header=True,index=False,justify='center')]
                           ,table7=[tableRender('TSLA').to_html(classes='data',header=True,index=False,justify='center')]
                           ,table8=[tableRender('PARA').to_html(classes='data',header=True,index=False,justify='center')]
                           ,table9=[tableRender('META').to_html(classes='data',header=True,index=False,justify='center')]
                           ,table10=[tableRender('INTC').to_html(classes='data',header=True,index=False,justify='center')])

# ------------------------------RENDERING GRAPHS-----------------------------


def graphGeneratorApple():
    chart_html = plot(candlestick_graph('AAPL'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorAmazon():
    chart_html = plot(candlestick_graph('AMZN'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorMicrosoft():
    chart_html = plot(candlestick_graph('MSFT'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorNvidia():
    chart_html = plot(candlestick_graph('NVDA'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorLyft():
    chart_html = plot(candlestick_graph('LYFT'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorWarner():
    chart_html = plot(candlestick_graph('WBD'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorTesla():
    chart_html = plot(candlestick_graph('TSLA'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorParamount():
    chart_html = plot(candlestick_graph('PARA'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorMeta():
    chart_html = plot(candlestick_graph('META'), output_type='div', include_plotlyjs=False)
    return chart_html

def graphGeneratorIntel():
    chart_html = plot(candlestick_graph('INTC'), output_type='div', include_plotlyjs=False)
    return chart_html

@app.route('/get_image/<image_name>')
def get_image(image_name):
    image_path = f'./{image_name}.png'
    return send_file(image_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)