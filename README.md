# VERI-Wild
A Large-Scale Dataset for Vehicle Re-Identification in the Wild

![](https://github.com/PKU-IMRE/VERI-Wild/blob/master/cars.JPG)
## Description of VERI-Wild Dataset
A large-scale vehicle ReID dataset in the wild (VERI-Wild) is captured from a large CCTV surveillance system consisting of 174 cameras across one month (30× 24h) under unconstrained scenarios. The cameras are distributed in a large urban district of more than 200km2. The YOLO-v2 [2] is used to detect the bounding box of vehicles. The raw vehicle image set contains 12 million vehicle images, and 11 volunteers are invited to clean the dataset for 1 month. After data cleaning and annotation, 416,314 vehicle images of 40,671 identities are collected. The statistics of VERI-Wild is illustrated in Figure. For privacy issues, the license plates are masked in the dataset. The distinctive features of VERI-Wild are summarized into the following aspects:

`Unconstrained capture conditions in the wild`  
The VERI-Wild dataset is collected from a real CCTV camera system consisting of 174 surveillance cameras, in which the unconstrained image capture conditions pose a variety of challenges.

`Complex capture conditions`  
The 174 surveillance cameras are distributed in an urban district over 200km2, presenting various backgrounds, resolutions, viewpoints, and occlusion in the wild. In extreme cases, one vehicle appears in more than 40 different cameras, which would be challenging for ReID algorithms.

`Large time span involving severe illumination and weather changes`  
The VERI-Wild is collected from a duration of 125, 280 (174x24x30) video hours. Figure (b) gives the vehicle distributions in 4 time slots of 24h, i.e., morning, noon, afternoon, evening across 30 days. VERI-Wild also contains poor weather conditions, such as rainy, foggy, etc, which are not provided in previous datasets.

`Rich Context Information`  
We provide rich context information such as camera IDs, timestamp, tracks relation across cameras, which are potential to facilitate the research on behavior analysis in camera networks, like vehicle behavior modeling, cross-camera tracking and graph-based retrieval.

![](https://github.com/PKU-IMRE/VERI-Wild/blob/master/statistics.png)

## Test

Note that, for CVPR 2019 test set, given a query image, we remove the images with the same camera id and same vehicle id as query image in the gallery set. They are not considered when computing the mAP and CMC.

We also provide the test dataset for VCIP grand challenge, which is a more challenging dataset. We named it the GC test set.

## Download Links

`Baidu Yun Pan`: https://pan.baidu.com/s/1FzvR5iRQgh8ZbSYZPbi9aQ  
`Password`: kob9 

`Google Driver`:https://drive.google.com/drive/folders/1q9kClC0gy0bz2i06sHlKUh2Pqk6RxKan?usp=sharing

## Citation
```  
@inproceedings{lou2019large,
  title={A Large-Scale Dataset for Vehicle Re-Identification in the Wild},
  author={Lou, Yihang and Bai, Yan and Liu, Jun and Wang, Shiqi and Duan, Ling-Yu},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2019}
}
```
