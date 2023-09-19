我近期开始学习pandas，为我的数据分析生涯做准备，目前准备先从表格的基础操作做起，并不断完善。
2023/9/15
pd.read_excel('文件地址') 阅读文档,还有read_csv、read_html等等。
df['标签'] 选择列
df['标签'].apply(lambda x: x[-2:])
apply() 这个方法的第一个参数时函数将用于列表里的每一个元素。 ‘lambda x: x[-2:]’ 是匿名函数，lamba是关键字 x是函数参数 ‘:’是函数的冒号，冒号后面的语句是表达式。
df.to_excel('文件',index=False) 保存后缀为excel文件，如果要保存别的后缀的文件就需要改变to_excel的函数。
2023/9/16
判断列是否存在：if '标签' not in df.columns：..... df.columns用来获取DataFrame对象的列标签的属性
lambda函数不支持赋值语句'='，但可以返回值，test.py文件中32行，最后用if判断语句返回x的值
想进行列的操作时需要先确保对应列是否存在
'pd.to_numeric’函数用于将一个Series或DataFrame的数据类型转换为数值类型，'coerce’表示将无法转换的数据设置为NaN。
df.tail(n)文件的最后n行
2023/9/17
df.loc['标签']选择行
df['年龄'] = pd.to_numeric(df['年龄'], errors='coerce') 'pd.to_numeric’函数用于将一个Series或DataFrame的数据类型转换为数值类型，'coerce’表示将无法转换的数据设置为NaN。
df.iloc[] 和 df.loc[]的作用差不多，iloc是第几行并且可以分片 [：3]就代表前三行，loc是根据标签找所在行
2023/9/18
df.index用来获取DataFrame对象的行标签的属性
df['姓名'].fillna('') 该代码里fillna('')的作用时将姓名列表里的空格填入''
2023/9/19
给数据加标签 pd.cut()函数
例如：df['薪资水平'] = pd.cut(df['薪资'],bins=[3000,4000,5000,7000],labels=['小薪','小康','赋予'])
放标签的列=pd.cut(需要加标签的依据，判断条件，标签列表)
