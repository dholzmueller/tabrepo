from autogluon.common.space import Real, Int, Categorical
from autogluon.tabular.models import KNNModel

from ...utils.config_utils import ConfigGenerator


name = 'KNeighbors'
manual_configs = [
    {'weights': 'uniform'},
    {'weights': 'distance'},
]
search_space = {
    'n_neighbors': Categorical(3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 20, 30, 40, 50),
    'weights': Categorical('uniform', 'distance'),
    'p': Categorical(2, 1),
}

gen_knn = ConfigGenerator(model_cls=KNNModel, manual_configs=[{}], search_space=search_space)


def generate_configs_knn(num_random_configs=50):
    config_generator = ConfigGenerator(name=name, manual_configs=manual_configs, search_space=search_space)
    return config_generator.generate_all_configs(num_random_configs=num_random_configs)
