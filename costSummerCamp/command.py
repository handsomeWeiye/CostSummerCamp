from costSummerCamp import db,app
from costSummerCamp.model import CostDetails,Cost
import click

@app.cli.command()
def inintdb():
    print('==============================')
    db.create_all()
    CostName = [
        "毛笔",
        "墨汁",
        '毛边纸',
        "毛毡纸",
        "小碟子",
        "2b铅笔",
        '速写板',
        "打印纸",
        '橡皮',
        '透明胶带',
        '美工刀',
        '水彩纸',
        '水彩笔',
        '水桶',
        '水彩颜料',
        '水胶带',
        '调色盘',
        '画框',
        '油费',
        '过路费',
    ]
    price = [29.90,
             22.00,
             39.00,
             5.50,
             1.50,
             9.90,
             18.90,
             25.00,
             32.40,
             3.00,
             2.00,
             16.00,
             35.00,
             12.50,
             23.80,
             15.60,
             4.36,
             33.30,
             25.00,
             0.70,
             18.00,
             ]
    number = [25,
              2,
              2,
              25,
              25,
              3,
              25,
              1,
              1,
              5,
              5,
              2,
              5,
              25,
              5,
              5,
              5,
              5,
              15,
              550,
              10,
              ]
    unit = [
        '支',
        '瓶',
        '张',
        '张',
        '个',
        '盒',
        '个',
        '包',
        '盒',
        '个',
        '把',
        '包',
        '套',
        '个',
        '个',
        '盒',
        '五卷',
        '个',
        '个',
        '公里',
        "次",

    ]
    specification = [
        '中号小白云',
        '一得阁',
        '两刀',
        '50x50cm',
        '水彩小蝶',
        '12支每盒',
        '8k画夹速写板',
        'a4',
        '一盒30个',
        '12 mm',
        '小号',
        '180g a4',
        '7支装',
        '折叠小凳子'
        '折叠水桶',
        '24色',
        '1.8CM',
        '18格',
        '中号',
        '1公里',
        '次',
    ]
    classmodel = [
        '书法',
        '书法',
        '书法',
        '书法',
        '书法',
        '右脑模式',
        '右脑模式',
        '右脑模式',
        '右脑模式',
        '右脑模式',
        '右脑模式',
        '水彩写生上色',
        '水彩写生上色',
        '水彩写生上色',
        '水彩写生上色',
        '水彩写生上色',
        '水彩写生上色',
        '水彩写生上色',
        '水彩写生上色',
        '交通补贴',
        '交通补贴',

    ]
    isConsumables = [
        False,
        True,
        True,
        False,
        False,
        True,
        False,
        True,
        True,
        True,
        False,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        True,
        True,
        True,

    ]

    cost_id = [1,2,3,4,5,6,7,8,9,10,11,12,13
               ,14,15,16,17,18,19,20,21,22]

    for i in range(len(CostName)):
        cost = Cost(
            name=CostName[i],
            price=price[i],
            unit =unit[i],
            specification =specification[i],
            classify= classmodel[i],
            isConsumables = isConsumables[i],
            isRealPrice=False
        )
        print(cost)
        db.session.add(cost)

    print('11111111111111111111111111111111111111111')

    for i in range(len(CostName)):
        costdetails = CostDetails(
            costName=CostName[i],
            number=number[i],
            cost_id=cost_id[i],

        )
        db.session.add(costdetails)
    print('22222222222222222222222222222222222222222222222')
    db.session.commit()

    click.echo('Initialized database')

