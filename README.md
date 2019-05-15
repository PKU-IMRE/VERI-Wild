# VERI-Wild
A Large-Scale Dataset for Vehicle Re-Identification in the Wild

## Description of VERI-Wild Dataset
A large-scale vehicle ReID dataset in the wild (VERI-Wild) is captured from a large CCTV surveillance system consisting of 174 cameras across one month (30× 24h) under unconstrained scenarios. The cameras are distributed in a large urban district of more than 200km2. The YOLO-v2 [2] is used to detect the bounding box of vehicles. The raw vehicle image set contains 12 million vehicle images, and 11 volunteers are invited to clean the dataset for 1 month. After data cleaning and annotation, 416,314 vehicle images of 40,671 identities are collected. The statistics of VERI-Wild is illustrated in Figure 2. For privacy issues, the license plates are masked in the dataset. The distinctive features of VERI-Wild are summarized into the following aspects:

'Unconstrained capture conditions in the wild'  
The VERI-Wild dataset is collected from a real CCTV camera system consisting of 174 surveillance cameras, in which the unconstrained image capture conditions pose a variety of challenges.

'Complex capture conditions'  
The 174 surveillance cameras are distributed in an urban district over 200km2, presenting various backgrounds, resolutions, viewpoints, and occlusion in the wild. In extreme cases, one vehicle appears in more than 40 different cameras, which would be challenging for ReID algorithms.

'Large time span involving severe illumination and weather changes'  
The VERI-Wild is collected from a duration of 125, 280 (174x24x30) video hours. Figure 2. (b) gives the vehicle distributions in 4 time slots of 24h, i.e., morning, noon, afternoon, evening across 30 days. VERI-Wild also contains poor weather conditions, such as rainy, foggy, etc, which are not provided in previous datasets.

'Rich Context Information'  
We provide rich context information such as camera IDs, timestamp, tracks relation across cameras, which are potential to facilitate the research on behavior analysis in camera networks, like vehicle behavior modeling, cross-camera tracking and graph-based retrieval.


