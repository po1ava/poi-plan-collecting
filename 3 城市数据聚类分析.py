from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    column_name = ['餐饮服务', '购物服务', '生活服务', '风景名胜', '商务住宅', '公司企业', ]  # 用于聚类分析的类名
    n_clusters = 5  # 聚类分析类别数量

    df = pd.read_excel(f'2 城市poi详细数据.xlsx')
    data = df[column_name].values

    # 数据归一化
    scaler = MinMaxScaler()
    scaler.fit(data)
    data_norm = scaler.transform(data)

    data_pred = KMeans(n_clusters=5).fit_predict(data_norm)  # 删除n_clusters参数以自动选择合适的类别数量
    print(data_pred)

    # 数据降维显示
    pca = PCA(n_components=2)
    data_2 = pca.fit_transform(data_norm)
    plt.scatter(data_2[:, 0], data_2[:, 1], c=data_pred)
    plt.show()

    df['class'] = data_pred
    df.to_excel("3 城市poi聚类结果.xlsx", index=False)
