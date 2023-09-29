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
te = TransactionEncoder() TransactionEncoder是mlxtend中专门用于对交易记录进行编码的类型
encorder = te.fit(dataset) fit()方法参数是之前的双层列表对象，该方法可以从数据中统计唯一的商品列表，在执行这一句代码的时候已经
                           把每一列对应的上篇标签都存在encoder.columns_这个属性里
