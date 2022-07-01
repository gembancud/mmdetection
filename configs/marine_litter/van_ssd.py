# The new config inherits a base config to highlight the necessary modification
_base_ = '../ssd/ssd512_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
        bbox_head=dict(num_classes=18)
    )

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('Glass-bottle',
'Glass-other',
'Metal-drinking cans',
'Plastic-Other',
'Plastic-bag',
'Plastic-drinks',
'Plastic-food container',
'Plastic-food packet',
'Plastic-hard',
'Plastic-nonfood Packet',
'Plastic-nonfood container',
'Plastic-other bottles containers and drums',
'Plastic-rope string',
'Plastic-tableware',
'Rubber-Other',
'Rubber-footwear',
'SanitaryMedicalWaste-Other',
'Trash-Generic')
data = dict(
    train=dict(
        img_prefix='marine_litter/hydroflask/train',
        classes=classes,
        ann_file='marine_litter/hydroflask/train/_annotations.coco.json'),
    val=dict(
        img_prefix='marine_litter/hydroflask/valid',
        classes=classes,
        ann_file='marine_litter/hydroflask/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='marine_litter/hydroflask/test',
        classes=classes,
        ann_file='marine_litter/hydroflask/test/_annotations.coco.json')
    )

log_config= dict(
    hooks=[
    dict(type='TextLoggerHook'),
    dict(type='MMDetWandbHook',
         init_kwargs={'project': 'marine_litter'},
         interval=1,
         log_checkpoint=False,
         log_checkpoint_metadata=True,
         num_eval_images=100)]
)

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/ssd512_coco_20210803_022849-0a47a1ca.pth'
