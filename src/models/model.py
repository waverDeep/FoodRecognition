import src.models.model_baseline as model_baseline
import torch


def load_model(config, checkpoint_path=None):
    model_name = config['model_name']
    model = None
    if model_name == 'VGG16Combine':
        model = model_baseline.VGG16Combine(
            last_node=config['last_node'],
            num_classes=config['num_classes'],
        )
    elif model_name == 'ResNET50Combine':
        model = model_baseline.ResNET50Combine(
            last_node=config['last_node'],
            num_classes=config['num_classes'],
        )
    elif model_name == 'ResNET152Combine':
        model = model_baseline.ResNET152Combine(
            last_node=config['last_node'],
            num_classes=config['num_classes'],
        )
    elif model_name == 'WideResNET50_2Combine':
        model = model_baseline.WideResNET50_2Combine(
            last_node=config['last_node'],
            num_classes=config['num_classes'],
        )
    elif model_name == 'MobileNetV2Combine':
        model = model_baseline.MobileNetV2Combine(
            last_node=config['last_node'],
            num_classes=config['num_classes'],
        )
    elif model_name == 'DenseNet121Combine':
        model = model_baseline.DenseNet121Combine(
            last_node=config['last_node'],
            num_classes=config['num_classes'],
        )
    elif model_name == 'SqueezeNet10Combine':
        model = model_baseline.SqueezeNet10Combine(
            last_node=config['last_node'],
            num_classes=config['num_classes'],
        )

    if config['model_checkpoint'] is not None:
        device = torch.device('cpu')
        checkpoint = torch.load(checkpoint_path, map_location=device)
        model.load_state_dict(checkpoint['model_state_dict'])

    return model
