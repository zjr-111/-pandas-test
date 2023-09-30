                                                      关联分析
np.genfromtxt()方法是从指定csv文件中加载数据，并将其储存在NumPy数组中
格式：  第一个参数是要加载的csv文件url，delimiter是指定csv文件中的分隔符，skip_header是指定数组元素的类型，
        encoding指定文件编码方式
raw_data = np.genfromtxt(
  'url'
  delimiter=',',
  skip_header=True,
  dtype=None,
  encoding='utf8'
)
te = TransactionEncoder() 
    TransactionEncoder是mlxtend中专门用于对交易记录进行编码的类型
encorder = te.fit(dataset) 
    fit()方法参数是之前的双层列表对象，该方法可以从数据中统计唯一的商品列表，在执行这一句代码的时候已经把每一列对应的上篇标签都存在encoder.columns_这个属性里
one_hot_encoded_array = encorder.transform(dataset) 
    transform()方法再次把dataset作为参数传进去，这时候返回的值就是一个经过独热编码过的，numpy 的 ndarray 类型对象。每一行依然是代表一个顾客的购物清单，其中每一个元素代表这位顾客有没有购买对应商品
dataset_te = pd.DataFrame(one_hot_encoded_array, columns=encorder.columns_)
    创建一个 pandas 的 DataFrame 对象 df，将数据组合和商品标签组合在一起。
frequent = apriori(dataset_te, min_support = 0.2, use_colnames = True)
    apriori()函数可以寻找最小支持度的商品组合，参数1，一个DataFrame对象，里面存放的是经过独热编码的顾客购物清单；min_support最小支持度，use_colnames如果是 True，那么结果会使用列标签的名称，否则使用序号。
rules = association_rules(frequent, metric = 'confidence', min_threshold = 0.6)
    association_rules()函数挖掘到符合条件的关联规则集合，参数1具有support和itemsets这两列的DataFrame对象；metric作为条件的数据指标英语名称，支持三个指标：'support'（支持度），'confidence'（置信度）和 'lift'（提升度），默认为 'confidence'；min_threshold数据指标的最小值，默认是0.8
rules.sort_values("lift", ascending=False)
    sort_values()方法按照lift这一列的值进行降序排列
