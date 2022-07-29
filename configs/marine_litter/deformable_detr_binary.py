# The new config inherits a base config to highlight the necessary modification
_base_ = '../deformable_detr/deformable_detr_twostage_refine_r50_16x2_50e_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
        bbox_head=dict(num_classes=1)
    )

# Modify dataset related settings
dataset_type = 'COCODataset'
# classes = ('trash',)
classes = (
           'Trash-Generic',)
data = dict(
    samples_per_gpu=1,
    train=dict(
        img_prefix='marine_litter/aceluya/train',
        classes=classes,
        ann_file='marine_litter/aceluya/train/_annotations.coco.json'),
    val=dict(
        img_prefix='marine_litter/aceluya/valid',
        classes=classes,
        ann_file='marine_litter/aceluya/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='marine_litter/aceluya/test',
        classes=classes,
        ann_file='marine_litter/aceluya/test/_annotations.coco.json')
    )


log_config= dict(
    hooks=[
    dict(type='TextLoggerHook'),
    dict(type='MMDetWandbHook', 
         init_kwargs={'project': 'marine_litter'},
         interval=10,
         log_checkpoint=False,
         log_checkpoint_metadata=True,)]
)

runner = dict(type='EpochBasedRunner', max_epochs=150)
workflow = [('train', 1), ('val', 1)]



# We can use the pre-trained Mask RCNN model to obtain higher performance
# load_from = 'work_dirs/deformable_detr_2/latest.pth'
load_from = 'checkpoints/deformable_detr_twostage_refine_r50_16x2_50e_coco_20210419_220613-9d28ab72.pth'
