import src.data.dataset_k_food as k_food
import src.data.dataset_ingredient as ingredient
import src.data.dataset_ingd as dataset_ingd
from torch.utils.data import Dataset, DataLoader

def get_dataloader(config, mode='train'):
    dataset = None
    dataset_type = config['dataset_type']
    if dataset_type == 'KFoodSampleDataset':
        dataset = k_food.KFoodSampleDataset(
            directory_path=config['{}_dataset'.format(mode)],
        )
    elif dataset_type == 'KFoodDataset':
        dataset = k_food.KFoodDataset(
            directory_path=config['{}_dataset'.format(mode)],
            mode=mode,
            crop_size=config['crop_size'],
        )
    elif dataset_type == 'IngredientDataset':
        dataset = ingredient.IngredientDataset(
            directory_path=config['{}_dataset'.format(mode)],
            mode=mode,
            crop_size=config['crop_size'],
        )
    elif dataset_type == 'INGDDataset':
        dataset = dataset_ingd.INGDDataset(
            directory_path=config['{}_dataset'.format(mode)],
            mode=mode,
            crop_size=config['crop_size'],
        )

    dataloader = DataLoader(
        dataset=dataset,
        batch_size=config['batch_size'],
        shuffle=config['dataset_shuffle'],
        num_workers=config['num_workers'],
    )
    return dataloader, dataset