# The new config inherits a base config to highlight the necessary modification
_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1))
    )

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('trash',)
data = dict(
    train=dict(
        img_prefix='marine_litter/uw_nov_binary/train',
        classes=classes,
        ann_file='marine_litter/uw_nov_binary_train.json'),
    val=dict(
        img_prefix='marine_litter/uw_nov_binary/val',
        classes=classes,
        ann_file='marine_litter/uw_nov_binary_val.json'),
    # test=dict(
    #     img_prefix='balloon/val/',
    #     classes=classes,
    #     ann_file='balloon/val/annotation_coco.json')
    )

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
