from flask import redirect,url_for,render_template,flash
from costSummerCamp import db,app
from costSummerCamp.form import CostAdd,CostDetailsAdd
from costSummerCamp.model import Cost,CostDetails
from pyecharts.charts import Bar,Pie
from pyecharts import options as opts

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/budgetpage',methods=['GET','POST'])
def budgetpage():

    costadd = CostAdd()
    costdetailsadd = CostDetailsAdd()


    def getTotalBudget():
        costClassOfBudget = Cost.query.filter(Cost.isRealPrice == False).all()
        totalBudget = 0
        for item in costClassOfBudget:
            price = item.price
            budgetDetails = item.costdetails
            budgetDetailsNumCount = 0
            for i in budgetDetails:
                budgetDetailsNumCount = budgetDetailsNumCount + i.number
            amountOfItem = budgetDetailsNumCount * price
            totalBudget = totalBudget + amountOfItem

        # print('{:.2f}'.format(totalBudget))
        return '{:.2f}'.format(totalBudget)

    def getTotalReal():
        costClassOfReal = Cost.query.filter(Cost.isRealPrice == True).all()
        totalReal = 0
        for item in costClassOfReal:
            price = item.price
            RealDetails = item.costdetails
            RealDetailsNumCount = 0
            for i in RealDetails:
                RealDetailsNumCount = RealDetailsNumCount + i.number
            amountOfItem = RealDetailsNumCount * price
            totalReal = totalReal + amountOfItem

        print('{:.2f}'.format(totalReal))
        return '{:.2f}'.format(totalReal)

    def getCostPieInBudget():
        costClassOfBudget = Cost.query.filter(Cost.isRealPrice == False).all()
        listBudgetName = []
        listBudgetAmount = []
        for item in costClassOfBudget:
            listBudgetName.append(item.name)
            price = item.price
            budgetDetails = item.costdetails
            budgetDetailsNumCount = 0
            for i in budgetDetails:
                budgetDetailsNumCount = budgetDetailsNumCount + i.number
            amountOfItem =round(budgetDetailsNumCount * price, 2)
            listBudgetAmount.append(amountOfItem)
        # print(listBudgetName)
        #         # print(listBudgetAmount)
        zips = [list(z) for z in zip(listBudgetName, listBudgetAmount)]
        # print(zips)

        budgetCostPie = (
            Pie()
                .add("", zips)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用名预算饼图"),legend_opts=opts.LegendOpts(pos_top=20,type_='scroll'))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        )

        budgetCostPiedata = budgetCostPie.dump_options()
        # print(budgetCostPiedata)
        return budgetCostPiedata

    def getCostBarInBudget():
        costClassOfBudget = Cost.query.filter(Cost.isRealPrice == False).all()
        listBudgetName = []
        listBudgetAmount = []
        for item in costClassOfBudget:
            listBudgetName.append(item.name)
            price = item.price
            budgetDetails = item.costdetails
            budgetDetailsNumCount = 0
            for i in budgetDetails:
                budgetDetailsNumCount = budgetDetailsNumCount + i.number
            amountOfItem = round(budgetDetailsNumCount * price,2)
            listBudgetAmount.append(amountOfItem)
        # print(listBudgetName)
        # print(listBudgetAmount)
        zips = [list(z) for z in zip(listBudgetName, listBudgetAmount)]
        # print(zips)

        budgetCostBar = (
            Bar()
                .add_xaxis(listBudgetName)
                .add_yaxis("该预算费用总计", listBudgetAmount)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用名预算柱状图"))
        )

        budgetCostBardata = budgetCostBar.dump_options()
        # print(budgetCostBardata)
        return budgetCostBardata

    def getClassPieInBudget():

        def _getOneInBudgetAmount(classify):
            OneOfBudget = Cost.query.filter(Cost.isRealPrice == False).filter(
                Cost.classify == '{}'.format(classify)).all()
            OneOfBudgetAmount = 0
            for item in OneOfBudget:
                price = item.price
                budgetDetails = item.costdetails
                budgetDetailsNumCount = 0
                for i in budgetDetails:
                    budgetDetailsNumCount = budgetDetailsNumCount + i.number
                amountOfItem = budgetDetailsNumCount * price
                OneOfBudgetAmount = round(OneOfBudgetAmount + amountOfItem,2)

            return OneOfBudgetAmount

        classifylist = ['书法', '右脑模式', '水彩写生上色', '交通补贴']
        BudgetAmountlist = []
        for i in classifylist:
            BudgetAmountlist.append(_getOneInBudgetAmount(i))

        zips = [list(z) for z in zip(classifylist, BudgetAmountlist)]
        # print(zips)

        budgetClassPie = (
            Pie()
                .add("", zips)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用类别预算饼图"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        )

        budgetClassPiedata = budgetClassPie.dump_options()
        # print(budgetClassPiedata)
        return budgetClassPiedata

    def getClassBarInBudget():

        def _getOneInBudgetAmount(classify):
            OneOfBudget = Cost.query.filter(Cost.isRealPrice == False).filter(
                Cost.classify == '{}'.format(classify)).all()
            OneOfBudgetAmount = 0
            for item in OneOfBudget:
                price = item.price
                budgetDetails = item.costdetails
                budgetDetailsNumCount = 0
                for i in budgetDetails:
                    budgetDetailsNumCount = budgetDetailsNumCount + i.number
                amountOfItem = round(budgetDetailsNumCount * price,2)
                OneOfBudgetAmount = OneOfBudgetAmount + amountOfItem

            return OneOfBudgetAmount

        classifylist = ['书法', '右脑模式', '水彩写生上色', '交通补贴']
        BudgetAmountlist = []
        for i in classifylist:
            BudgetAmountlist.append(_getOneInBudgetAmount(i))

        zips = [list(z) for z in zip(classifylist, BudgetAmountlist)]
        # print(zips)

        budgetClassBar = (
            Bar()
                .add_xaxis(classifylist)
                .add_yaxis("该类目预算费用总计", BudgetAmountlist)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用类目预算柱状图"))
        )

        budgetCostBardata = budgetClassBar.dump_options()
        # print(budgetCostBardata)
        return budgetCostBardata

    def getConsumablesPieInBudget():

        def _getOneInBudgetAmount(bool):
            OneOfBudget = Cost.query.filter(Cost.isRealPrice == False).filter(Cost.isConsumables == bool).all()
            OneOfBudgetAmount = 0
            for item in OneOfBudget:
                price = item.price
                budgetDetails = item.costdetails
                budgetDetailsNumCount = 0
                for i in budgetDetails:
                    budgetDetailsNumCount = budgetDetailsNumCount + i.number
                amountOfItem = round(budgetDetailsNumCount * price,2)
                OneOfBudgetAmount = OneOfBudgetAmount + amountOfItem

            return OneOfBudgetAmount

        classifylist = [True, False]
        BudgetAmountlist = []
        for i in classifylist:
            BudgetAmountlist.append(_getOneInBudgetAmount(i))

        zips = [list(z) for z in zip(['消耗品', '非消耗品'], BudgetAmountlist)]
        # print(zips)

        budgetClassPie = (
            Pie()
                .add("", zips)
                .set_global_opts(title_opts=opts.TitleOpts(title="消耗分类费用预算饼图"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        )

        budgetClassPiedata = budgetClassPie.dump_options()
        # print(budgetClassPiedata)
        return budgetClassPiedata

    def getConsumablesBarInBudget():
        def _getOneInBudgetAmount(bool):
            OneOfBudget = Cost.query.filter(Cost.isRealPrice == False).filter(Cost.isConsumables == bool).all()
            OneOfBudgetAmount = 0
            for item in OneOfBudget:
                price = item.price
                budgetDetails = item.costdetails
                budgetDetailsNumCount = 0
                for i in budgetDetails:
                    budgetDetailsNumCount = budgetDetailsNumCount + i.number
                amountOfItem = round(budgetDetailsNumCount * price,2)
                OneOfBudgetAmount = OneOfBudgetAmount + amountOfItem

            return OneOfBudgetAmount

        classifylist = [True, False]
        classifylistname = ['消耗品', '非消耗品']
        BudgetAmountlist = []
        for i in classifylist:
            BudgetAmountlist.append(_getOneInBudgetAmount(i))

        zips = [list(z) for z in zip(['消耗品', '非消耗品'], BudgetAmountlist)]
        # print(zips)

        budgetClassBar = (
            Bar()
                .add_xaxis(classifylistname)
                .add_yaxis("该类目预算费用总计", BudgetAmountlist)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用类目预算柱状图"))
        )

        budgetCostBardata = budgetClassBar.dump_options()
        # print(budgetCostBardata)
        return budgetCostBardata

    # def getBudget():
    #     TotalBudget =  getTotalBudget()
    #     CostPieInBudget = getCostPieInBudget()
    #     CostBarInBudget = getCostBarInBudget()
    #     ClassPieInBudget =getClassPieInBudget()
    #     ClassBarInBudget = getClassBarInBudget()
    #     ConsumablesPieInBudget = getConsumablesPieInBudget()
    #     ConsumablesBarInBudget = getConsumablesBarInBudget()
    #
    #     return TotalBudget,CostPieInBudget,CostBarInBudget,ClassPieInBudget,ClassBarInBudget,ConsumablesPieInBudget,ConsumablesBarInBudget

    if costdetailsadd.validate_on_submit():
        cost_id = costdetailsadd.costName.data
        costName = Cost.query.filter(Cost.id == cost_id).first().name
        number = costdetailsadd.number.data
        adddata = CostDetails(costName = costName,number=number,cost_id=cost_id)
        db.session.add(adddata)
        db.session.commit()
        flash('您的费用明细信息已更新')
        return redirect(url_for('budgetpage'))

    if costadd.validate_on_submit():
        name = costadd.name.data
        price = costadd.price.data
        unit = costadd.unit.data
        specification = costadd.specification.data
        classifyNum = costadd.classify.data
        lista = ['aa','书法', '右脑模式', '水彩写生上色',  '交通补贴']
        classify = lista[classifyNum]
        isConsumables = costadd.isConsumables.data
        isRealPrice = costadd.isRealPrice.data
        adddata = Cost(name = name,price=price,unit=unit,specification=specification,classify=classify,isConsumables=isConsumables,isRealPrice=isRealPrice)
        db.session.add(adddata)
        db.session.commit()
        flash('您的费用类型信息已更新')
        return redirect(url_for('index'))




    return render_template('budgetpage.html', TotalBudget=getTotalBudget(), CostPieInBudget=getCostPieInBudget(),CostBarInBudget = getCostBarInBudget(),
                           ClassPieInBudget =getClassPieInBudget(),ClassBarInBudget = getClassBarInBudget(),ConsumablesPieInBudget = getConsumablesPieInBudget(),
                           ConsumablesBarInBudget = getConsumablesBarInBudget(),costdetailsadd=costdetailsadd,costadd=costadd)


@app.route('/realpage',methods=['GET','POST'])
def realpage():

    costadd = CostAdd()
    costdetailsadd = CostDetailsAdd()


    # def getTotalBudget():
    #     costClassOfBudget = Cost.query.filter(Cost.isRealPrice == False).all()
    #     totalBudget = 0
    #     for item in costClassOfBudget:
    #         price = item.price
    #         budgetDetails = item.costdetails
    #         budgetDetailsNumCount = 0
    #         for i in budgetDetails:
    #             budgetDetailsNumCount = budgetDetailsNumCount + i.number
    #         amountOfItem = budgetDetailsNumCount * price
    #         totalBudget = totalBudget + amountOfItem
    #
    #     # print('{:.2f}'.format(totalBudget))
    #     return '{:.2f}'.format(totalBudget)

    def getTotalReal():
        costClassOfReal = Cost.query.filter(Cost.isRealPrice == True).all()
        totalReal = 0
        for item in costClassOfReal:
            price = item.price
            RealDetails = item.costdetails
            RealDetailsNumCount = 0
            for i in RealDetails:
                RealDetailsNumCount = RealDetailsNumCount + i.number
            amountOfItem =round(RealDetailsNumCount * price,2)
            totalReal = totalReal + amountOfItem

        # print('{:.2f}'.format(totalReal))
        return '{:.2f}'.format(totalReal)

    def getCostPieInBudget():
        costClassOfBudget = Cost.query.filter(Cost.isRealPrice == True).all()
        listBudgetName = []
        listBudgetAmount = []
        for item in costClassOfBudget:
            listBudgetName.append(item.name)
            price = item.price
            budgetDetails = item.costdetails
            budgetDetailsNumCount = 0
            for i in budgetDetails:
                budgetDetailsNumCount = budgetDetailsNumCount + i.number
            amountOfItem = round(budgetDetailsNumCount * price,2)
            listBudgetAmount.append(amountOfItem)
        # print(listBudgetName)
        #         # print(listBudgetAmount)
        zips = [list(z) for z in zip(listBudgetName, listBudgetAmount)]
        # print(zips)

        budgetCostPie = (
            Pie()
                .add("", zips)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用名预算饼图"),legend_opts=opts.LegendOpts(pos_top=20,type_='scroll'))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        )

        budgetCostPiedata = budgetCostPie.dump_options()
        # print(budgetCostPiedata)
        return budgetCostPiedata

    def getCostBarInBudget():
        costClassOfBudget = Cost.query.filter(Cost.isRealPrice == True).all()
        listBudgetName = []
        listBudgetAmount = []
        for item in costClassOfBudget:
            listBudgetName.append(item.name)
            price = item.price
            budgetDetails = item.costdetails
            budgetDetailsNumCount = 0
            for i in budgetDetails:
                budgetDetailsNumCount = budgetDetailsNumCount + i.number
            amountOfItem = round(budgetDetailsNumCount * price,2)
            listBudgetAmount.append(amountOfItem)
        # print(listBudgetName)
        # print(listBudgetAmount)
        zips = [list(z) for z in zip(listBudgetName, listBudgetAmount)]
        # print(zips)

        budgetCostBar = (
            Bar()
                .add_xaxis(listBudgetName)
                .add_yaxis("该预算费用总计", listBudgetAmount)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用名预算柱状图"))
        )

        budgetCostBardata = budgetCostBar.dump_options()
        # print(budgetCostBardata)
        return budgetCostBardata

    def getClassPieInBudget():

        def _getOneInBudgetAmount(classify):
            OneOfBudget = Cost.query.filter(Cost.isRealPrice == True).filter(
                Cost.classify == '{}'.format(classify)).all()
            OneOfBudgetAmount = 0
            for item in OneOfBudget:
                price = item.price
                budgetDetails = item.costdetails
                budgetDetailsNumCount = 0
                for i in budgetDetails:
                    budgetDetailsNumCount = budgetDetailsNumCount + i.number
                amountOfItem = round(budgetDetailsNumCount * price,2)
                OneOfBudgetAmount = OneOfBudgetAmount + amountOfItem

            return OneOfBudgetAmount

        classifylist = ['书法', '右脑模式', '水彩写生上色', '交通补贴']
        BudgetAmountlist = []
        for i in classifylist:
            BudgetAmountlist.append(_getOneInBudgetAmount(i))

        zips = [list(z) for z in zip(classifylist, BudgetAmountlist)]
        # print(zips)

        budgetClassPie = (
            Pie()
                .add("", zips)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用类别预算饼图"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        )

        budgetClassPiedata = budgetClassPie.dump_options()
        # print(budgetClassPiedata)
        return budgetClassPiedata

    def getClassBarInBudget():

        def _getOneInBudgetAmount(classify):
            OneOfBudget = Cost.query.filter(Cost.isRealPrice == True).filter(
                Cost.classify == '{}'.format(classify)).all()
            OneOfBudgetAmount = 0
            for item in OneOfBudget:
                price = item.price
                budgetDetails = item.costdetails
                budgetDetailsNumCount = 0
                for i in budgetDetails:
                    budgetDetailsNumCount = budgetDetailsNumCount + i.number
                amountOfItem = round(budgetDetailsNumCount * price,2)
                OneOfBudgetAmount = OneOfBudgetAmount + amountOfItem

            return OneOfBudgetAmount

        classifylist = ['书法', '右脑模式', '水彩写生上色', '交通补贴']
        BudgetAmountlist = []
        for i in classifylist:
            BudgetAmountlist.append(_getOneInBudgetAmount(i))

        zips = [list(z) for z in zip(classifylist, BudgetAmountlist)]
        # print(zips)

        budgetClassBar = (
            Bar()
                .add_xaxis(classifylist)
                .add_yaxis("该类目预算费用总计", BudgetAmountlist)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用类目预算柱状图"))
        )

        budgetCostBardata = budgetClassBar.dump_options()
        # print(budgetCostBardata)
        return budgetCostBardata

    def getConsumablesPieInBudget():

        def _getOneInBudgetAmount(bool):
            OneOfBudget = Cost.query.filter(Cost.isRealPrice == True).filter(Cost.isConsumables == bool).all()
            OneOfBudgetAmount = 0
            for item in OneOfBudget:
                price = item.price
                budgetDetails = item.costdetails
                budgetDetailsNumCount = 0
                for i in budgetDetails:
                    budgetDetailsNumCount = budgetDetailsNumCount + i.number
                amountOfItem = round(budgetDetailsNumCount * price,2)
                OneOfBudgetAmount = OneOfBudgetAmount + amountOfItem

            return OneOfBudgetAmount

        classifylist = [True, False]
        BudgetAmountlist = []
        for i in classifylist:
            BudgetAmountlist.append(_getOneInBudgetAmount(i))

        zips = [list(z) for z in zip(['消耗品', '非消耗品'], BudgetAmountlist)]
        # print(zips)

        budgetClassPie = (
            Pie()
                .add("", zips)
                .set_global_opts(title_opts=opts.TitleOpts(title="消耗分类费用预算饼图"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
        )

        budgetClassPiedata = budgetClassPie.dump_options()
        # print(budgetClassPiedata)
        return budgetClassPiedata

    def getConsumablesBarInBudget():
        def _getOneInBudgetAmount(bool):
            OneOfBudget = Cost.query.filter(Cost.isRealPrice == True).filter(Cost.isConsumables == bool).all()
            OneOfBudgetAmount = 0
            for item in OneOfBudget:
                price = item.price
                budgetDetails = item.costdetails
                budgetDetailsNumCount = 0
                for i in budgetDetails:
                    budgetDetailsNumCount = budgetDetailsNumCount + i.number
                amountOfItem = round(budgetDetailsNumCount * price,2)
                OneOfBudgetAmount = OneOfBudgetAmount + amountOfItem

            return OneOfBudgetAmount

        classifylist = [True, False]
        classifylistname = ['消耗品', '非消耗品']
        BudgetAmountlist = []
        for i in classifylist:
            BudgetAmountlist.append(_getOneInBudgetAmount(i))

        zips = [list(z) for z in zip(['消耗品', '非消耗品'], BudgetAmountlist)]
        # print(zips)

        budgetClassBar = (
            Bar()
                .add_xaxis(classifylistname)
                .add_yaxis("该类目预算费用总计", BudgetAmountlist)
                .set_global_opts(title_opts=opts.TitleOpts(title="费用类目预算柱状图"))
        )

        budgetCostBardata = budgetClassBar.dump_options()
        # print(budgetCostBardata)
        return budgetCostBardata

    # def getBudget():
    #     TotalBudget =  getTotalBudget()
    #     CostPieInBudget = getCostPieInBudget()
    #     CostBarInBudget = getCostBarInBudget()
    #     ClassPieInBudget =getClassPieInBudget()
    #     ClassBarInBudget = getClassBarInBudget()
    #     ConsumablesPieInBudget = getConsumablesPieInBudget()
    #     ConsumablesBarInBudget = getConsumablesBarInBudget()
    #
    #     return TotalBudget,CostPieInBudget,CostBarInBudget,ClassPieInBudget,ClassBarInBudget,ConsumablesPieInBudget,ConsumablesBarInBudget

    if costdetailsadd.validate_on_submit():
        cost_id = costdetailsadd.costName.data
        costName = Cost.query.filter(Cost.id == cost_id).first().name
        number = costdetailsadd.number.data
        adddata = CostDetails(costName = costName,number=number,cost_id=cost_id)
        db.session.add(adddata)
        db.session.commit()
        flash('您的费用明细信息已更新')
        return redirect(url_for('index'))

    if costadd.validate_on_submit():
        name = costadd.name.data
        price = costadd.price.data
        unit = costadd.unit.data
        specification = costadd.specification.data
        classifyNum = costadd.classify.data
        lista = ['aa','书法', '右脑模式', '水彩写生上色',  '交通补贴']
        classify = lista[classifyNum]
        isConsumables = costadd.isConsumables.data
        isRealPrice = costadd.isRealPrice.data
        adddata = Cost(name = name,price=price,unit=unit,specification=specification,classify=classify,isConsumables=isConsumables,isRealPrice=isRealPrice)
        db.session.add(adddata)
        db.session.commit()
        flash('您的费用类型信息已更新')
        return redirect(url_for('realpage'))




    return render_template('budgetpage.html', TotalBudget=getTotalReal(), CostPieInBudget=getCostPieInBudget(),CostBarInBudget = getCostBarInBudget(),
                           ClassPieInBudget =getClassPieInBudget(),ClassBarInBudget = getClassBarInBudget(),ConsumablesPieInBudget = getConsumablesPieInBudget(),
                           ConsumablesBarInBudget = getConsumablesBarInBudget(),costdetailsadd=costdetailsadd,costadd=costadd)




