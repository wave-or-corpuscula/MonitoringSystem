menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Магазины', 'url_name': 'observed'},
    {'title': 'Товары', 'url_name': 'goods'},
]

from parsing.views.about import AboutView
from parsing.views.good_prices import GoodPricesView
from parsing.views.index import IndexView
from parsing.views.prices import PricesView, get_goods_data
from parsing.views.observed import ObservedListView
from parsing.views.goods import GoodsListView
from parsing.views.observed_goods import ObservedGoodsView
from parsing.views.set_origin import SetOriginView, add_origin_to_good
