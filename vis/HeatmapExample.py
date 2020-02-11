import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

countries = ["Australia", "Canada", "China", "France", "Germany", "Hong Kong", "India", "Ireland", "Italy", "Japan",
             "Mexico", "New Zealand", "Others", "South Korea", "Spain", "UK", "USA"]
corr = np.array([[1, 0.90200462, 0.803780284, 0.869436664, 0.913044132, 0.864814815, 0.639665286, 0.792063492,
                  0.723184223, 0.831154684, 0.786375661, 0.743386243, 0.801375661, 0.770502646, 0.81456044, 0.896497442,
                  0.910047373],
                 [0.90200462, 1, 0.847047195, 0.909930169, 0.921926127, 0.866849244, 0.655524937, 0.831298905,
                  0.765364917, 0.801873331, 0.83962106, 0.729949139, 0.84123109, 0.808489828, 0.851616107, 0.870110624,
                  0.886855309],
                 [0.803780284, 0.847047195, 1, 0.874170721, 0.819627193, 0.85380117, 0.684083397, 0.83874269,
                  0.801435407, 0.810887513, 0.852234754, 0.761452242, 0.871598441, 0.863011696, 0.863472785,
                  0.819120229, 0.797853484],
                 [0.869436664, 0.909930169, 0.874170721, 1, 0.908258, 0.894708995, 0.669904194, 0.894747899, 0.82380528,
                  0.856442577, 0.841503268, 0.760270775, 0.886106443, 0.851423903, 0.900587158, 0.91499474,
                  0.850768824],
                 [0.913044132, 0.921926127, 0.819627193, 0.908258, 1, 0.849873737, 0.637887022, 0.844507576,
                  0.773042929, 0.81825609, 0.79716811, 0.766308923, 0.833341751, 0.806628788, 0.855477855, 0.9084309,
                  0.903357509],
                 [0.864814815, 0.866849244, 0.85380117, 0.894708995, 0.849873737, 1, 0.637037037, 0.844444444,
                  0.785353535, 0.851742919, 0.815740741, 0.75462963, 0.829259259, 0.797222222, 0.862250712, 0.892072238,
                  0.850611542],
                 [0.639665286, 0.655524937, 0.684083397, 0.669904194, 0.637887022, 0.637037037, 1, 0.642149758,
                  0.698945982, 0.696433646, 0.71652864, 0.52757649, 0.721513688, 0.706884058, 0.652127462, 0.604896129,
                  0.585212148],
                 [0.792063492, 0.831298905, 0.83874269, 0.894747899, 0.844507576, 0.844444444, 0.642149758, 1,
                  0.825505051, 0.788071895, 0.826190476, 0.723148148, 0.880185185, 0.894444444, 0.929059829,
                  0.850428528, 0.764814815],
                 [0.723184223, 0.765364917, 0.801435407, 0.82380528, 0.773042929, 0.785353535, 0.698945982, 0.825505051,
                  1, 0.768419489, 0.795093795, 0.674031987, 0.884814815, 0.857828283, 0.818861694, 0.781986532,
                  0.689741602],
                 [0.831154684, 0.801873331, 0.810887513, 0.856442577, 0.81825609, 0.851742919, 0.696433646, 0.788071895,
                  0.768419489, 1, 0.757236228, 0.753540305, 0.835925926, 0.792647059, 0.802224736, 0.843915987,
                  0.781237777],
                 [0.786375661, 0.83962106, 0.852234754, 0.841503268, 0.79716811, 0.815740741, 0.71652864, 0.826190476,
                  0.795093795, 0.757236228, 1, 0.700727513, 0.856666667, 0.842460317, 0.84539072, 0.803724474,
                  0.751732497],
                 [0.743386243, 0.729949139, 0.761452242, 0.760270775, 0.766308923, 0.75462963, 0.52757649, 0.723148148,
                  0.674031987, 0.753540305, 0.700727513, 1, 0.71, 0.70462963, 0.723468661, 0.794191919, 0.782420327],
                 [0.801375661, 0.84123109, 0.871598441, 0.886106443, 0.833341751, 0.829259259, 0.721513688, 0.880185185,
                  0.884814815, 0.835925926, 0.856666667, 0.71, 1, 0.93462963, 0.903262108, 0.836535047, 0.760904393],
                 [0.770502646, 0.808489828, 0.863011696, 0.851423903, 0.806628788, 0.797222222, 0.706884058,
                  0.894444444, 0.857828283, 0.792647059, 0.842460317, 0.70462963, 0.93462963, 1, 0.889957265,
                  0.809113866, 0.734965547],
                 [0.81456044, 0.851616107, 0.863472785, 0.900587158, 0.855477855, 0.862250712, 0.652127462, 0.929059829,
                  0.818861694, 0.802224736, 0.84539072, 0.723468661, 0.903262108, 0.889957265, 1, 0.87427892,
                  0.789509706],
                 [0.896497442, 0.870110624, 0.819120229, 0.91499474, 0.9084309, 0.892072238, 0.604896129, 0.850428528,
                  0.781986532, 0.843915987, 0.803724474, 0.794191919, 0.836535047, 0.809113866, 0.87427892, 1,
                  0.882384522],
                 [0.910047373, 0.886855309, 0.797853484, 0.850768824, 0.903357509, 0.850611542, 0.585212148,
                  0.764814815, 0.689741602, 0.781237777, 0.751732497, 0.782420327, 0.760904393, 0.734965547,
                  0.789509706, 0.882384522, 1]])

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    ax = sns.heatmap(corr, vmin=0.5, vmax=1, square=True, annot=False, cmap="YlGnBu", xticklabels=countries,
                     yticklabels=countries)

# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=23)

labels = ax.get_xticklabels() + ax.get_yticklabels()
for label in labels:
    label.set_fontname('Times New Roman')
    label.set_fontsize(10)
    plt.setp(label, rotation=45, horizontalalignment='right')

#
# font1 = {'family': 'Times New Roman',
#          'weight': 'normal',
#          'size': 12,
#          }

# plt.title('Attribute similarity of IMDB-country', font1)
# plt.xlabel('')
plt.tight_layout()
plt.savefig(fname="IMDB-CountryCorr.pdf", format='pdf')

plt.show()