# VERI-Wild
VERI-Wild: A Large Dataset and a New Method for Vehicle Re-Identification in the Wild

![](https://github.com/PKU-IMRE/VERI-Wild/blob/master/cars.JPG)

## Description of VERI-Wild Dataset
A large-scale vehicle ReID dataset in the wild (VERI-Wild) is captured from a large CCTV surveillance system consisting of 174 cameras across one month (30*24h) under unconstrained scenarios. The cameras are distributed in a large urban district of more than 200km2. The YOLO-v2 [2] is used to detect the bounding box of vehicles. The raw vehicle image set contains 12 million vehicle images, and 11 volunteers are invited to clean the dataset for 1 month. After data cleaning and annotation, 416,314 vehicle images of 40,671 identities are collected. The statistics of VERI-Wild is illustrated in Figure. For privacy issues, the license plates are masked in the dataset. The distinctive features of VERI-Wild are summarized into the following aspects:

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
Important!!!!!!!!!


Note that, for VERI-Wild test set, given a query image, you need to remove the images with the same camera id and same vehicle id as query image in the gallery set. They are not considered when computing the mAP and CMC.


## Citation
``` 
@inproceedings{lou2019large,
 title={VERI-Wild: A Large Dataset and a New Method for Vehicle Re-Identification in the Wild},
 author={Lou, Yihang and Bai, Yan and Liu, Jun and Wang, Shiqi and Duan, Ling-Yu},
 booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
 pages = {3235--3243},
 year={2019}
}
```
``` 
@inproceedings{lou2019large,
 title={Disentangled Feature Learning Network and a Comprehensive Benchmark for Vehicle Re-Identification},
 author={Bai, Yan and Liu, Jun and Lou, Yihang and Wang, Ce and Duan, Ling-Yu},
 booktitle={In IEEE Transactions on Pattern Analysis and Machine Intelligence},
 year={2021}
}
```

## Contactor
Yan Bai, Email: yanbai@pku.edu.cn

To encourage related research, we will provide the dataset according to your request. Please email your full name and affiliation to the contact person (yanbai at pku dot edu dot cn). We ask for your information only to make sure the dataset is used for non-commercial purposes. We will not give it to any third party or publish it publicly anywhere. Due to the privacy issue we will not provide the license plates in the future. If you download our dataset, it means you have agreed to our terms of access in the email.


## State-of-the-art Results on the VeRi-Wild Dataset

<table>
  <tr>
    <td>Methods</td><td colspan="3">Small</td><td colspan="3">Medium</td><td colspan="3">Large</td>
	<tr>
	<tr>
		<td> </td> <td> mAP </td> <td> Top1 </td> <td> Top5 </td><td> mAP </td> <td> Top1 </td> <td> Top5 </td><td> mAP </td> <td> Top1 </td> <td> Top5 </td>
	<tr>
	<tr>
		<td> GoogleNet[1]</td> <td> 24.27 </td> <td> 57.16 </td> <td> 75.13 </td><td> 24.15 </td> <td> 53.16 </td> <td> 71.1 </td><td> 21.53 </td> <td> 44.61 </td> <td> 63.55 </td>
	<tr>
	<tr>
		<td> FDA-Net(VGGM)[2]</td> <td> 35.11 </td> <td> 64.03 </td> <td> 82.80 </td><td> 29.80 </td> <td> 57.82 </td> <td> 78.34 </td><td> 22.78 </td> <td> 49.43 </td> <td> 70.48 </td>
	<tr>
	<tr>
		<td> MLSL[3]</td> <td> 46.32 </td> <td> - </td> <td> - </td><td> 42.37 </td> <td> - </td> <td> - </td><td> 36.61 </td> <td> - </td> <td> - </td>
	<tr>
	<tr>
		<td> Triplet(Resnet50)</td> <td> 58.43 </td> <td> 65.76 </td> <td> 86.98 </td><td> 49.72 </td> <td> 57.76 </td> <td> 80.86 </td><td> 38.57 </td> <td> 47.65 </td> <td> 71.66 </td>
	<tr>
	<tr>
		<td> FDA-Net(Resnet50)[2]</td> <td> 61.57 </td> <td> 73.62 </td> <td> 91.23 </td><td> 52.69 </td> <td> 64.29 </td> <td> 85.39 </td><td> 45.78 </td> <td> 58.76 </td> <td> 80.97 </td>
	<tr>
	<tr>
		<td> AAVER(Resnet50)[4]</td> <td> 62.23 </td> <td> 75.80 </td> <td> 92.70 </td><td> 53.66 </td> <td> 68.24 </td> <td> 88.88 </td><td> 41.68 </td> <td> 58.69 </td> <td> 81.59 </td>
	<tr>
	<tr>
		<td> DFLNet(Resnet50)[5]</td> <td> 68.21 </td> <td> 80.68 </td> <td> 93.24 </td><td> 60.07 </td> <td> 70.67 </td> <td> 89.25 </td><td> 49.02 </td> <td> 61.60 </td> <td> 82.73 </td>
	<tr>
	<tr>
		<td> BS(mobilenet)[6]</td> <td> 70.54 </td> <td> 84.17 </td> <td> 95.30 </td><td> 62.83 </td> <td> 78.22 </td> <td> 93.06 </td><td> 51.63 </td> <td> 69.99 </td> <td> 88.45 </td>
	<tr>
	<tr>
		<td> UMTS(Resnet50)[7]</td> <td> 72.7 </td> <td> 84.5 </td> <td> - </td><td> 66.1 </td> <td> 79.3 </td> <td> - </td><td> 54.2 </td> <td> 72.8 </td> <td> - </td>
	<tr>
	<tr>
		<td> Strong baesline(Resnet50)[8]</td> <td> 76.61 </td> <td> 90.83 </td> <td> 97.29 </td><td> 70.11 </td> <td> 87.45 </td> <td> 95.24 </td><td> 61.3 </td> <td> 82.58 </td> <td> 92.73 </td>
	<tr>
	<tr>
		<td> HPGN(Resnet50+PGN)[9]</td> <td> 80.42 </td> <td> 91.37 </td> <td> - </td><td> 75.17 </td> <td> 88.21 </td> <td> - </td><td> 65.04 </td> <td> 82.68 </td> <td> - </td>
	<tr>
	<tr>
		<td> GLAMOR(Resnet50+PGN)[10]</td> <td> 77.15 </td> <td> 92.13 </td> <td> 97.43 </td><td> - </td> <td> - </td> <td> - </td><td> - </td> <td> - </td> <td> - </td>
	<tr>
	<tr>
		<td> PVEN(Resnet50)[12]</td> <td> 79.8 </td> <td> 94.01 </td> <td> 98.06 </td><td> 73.9 </td> <td> 92.03 </td> <td> 97.15 </td><td> 66.2 </td> <td> 88.62 </td> <td> 95.31 </td>
	<tr>	
	<tr>
		<td> SAVER(Resnet50)[11]</td> <td> 80.9 </td> <td> 93.78 </td> <td> 97.93 </td><td> 75.3 </td> <td> 92.7 </td> <td> 97.48 </td><td> 67.7 </td> <td> 89.5 </td> <td> 95.8 </td>
	<tr>
	<tr>
	        <td> DFNet(Resnet50)[14]</td> <td> 83.09 </td> <td> 94.79 </td> <td> 98.05 </td><td> 77.27 </td> <td> 93.22 </td> <td> 97.46 </td><td> 69.85 </td> <td> 89.38 </td> <td> 96.03 </td>
	<tr>
</table>


## State-of-the-art Results on the VeRi-Wild 2.0 Dataset
<table>
  <tr>
      <td>Methods</td><td colspan="3">Test Set All</td><td colspan="3">Test Set A</td><td colspan="3">Test Set B</td>
  <tr>
  <tr>
      <td> </td> <td> mAP </td> <td> Top1 </td> <td> Top5 </td><td> mAP </td> <td> Top1 </td> <td> Top5 </td><td> mAP </td> <td> Top1 </td> <td> Top5 </td>
  <tr>
  <tr>
       <td> Strong Baseline (Resnet50) [8] </td> <td> 34.71 </td> <td> 54.37 </td> <td> 63.99 </td> <td> 32.75 </td> <td> 40.12 </td> <td> 52.18 </td> <td> 42.25 </td> <td> 82.72 </td> <td> 90.67</td>
  <tr>
  <tr>
       <td> GSTE (Resnet50) (w/ bag-of-tricks)[13] </td> <td> 32.57 </td> <td> 59.25 </td> <td> 64.48 </td> <td> 33.01 </td> <td> 47.54 </td> <td> 50.81 </td> <td> 41.82 </td> <td> 86.08 </td> <td> 91.43</td>
  <tr>
  <tr>
       <td> FDA-Net (Resnet50)(w/ bag-of-tricks) [2] </td> <td> 34.21 </td> <td> 57.32 </td> <td> 64.90 </td> <td> 34.63 </td> <td> 45.53 </td> <td> 52.77 </td> <td> 3.93 </td> <td> 84.78 </td> <td> 92.47</td>
  <tr>
  <tr>
       <td> EVER (Resnet50) [41] </td> <td> 36.8 </td> <td> 59.1 </td> <td> 67.6 </td> <td> 36.8 </td> <td> 48.7 </td> <td> 57.3 </td> <td> 45.4 </td> <td> 86.1 </td> <td> 94.3</td>
   <tr>
  <tr>
      <td> PVEN(Resnet50)[12]</td> <td> 37.15 </td> <td> 61.19 </td> <td> 68.63 </td> <td> 38.77 </td> <td> 51.28 </td> <td> 59.32 </td> <td> 45.48 </td> <td> 88.05 </td> <td> 94.35 </td>
  <tr>  
  <tr>
      <td> SAVER(Resnet50)[11]</td> <td> 38.0 </td> <td> 62.1 </td> <td> 69.50 </td><td> 39.2 </td> <td> 52.3 </td> <td> 60.2 </td><td> 45.1 </td> <td> 88.1 </td> <td> 94.1 </td>
  <tr>
  <tr>
      <td> DFNet(Resnet50)[14]</td> <td> 39.84 </td> <td> 62.21 </td> <td> 68.90 </td><td> 40.39 </td> <td> 51.68 </td> <td> 60.51 </td><td> 46.13 </td> <td> 88.56 </td> <td> 94.17 </td>
  <tr>
</table>


[1] Yang, L., Luo, P., Change Loy, C., Tang, X.: A large-scale car dataset for fine-grained categorization and verification. In: IEEE Conference on Computer Visionand Pattern Recognition. (2015)

[2] Lou, Y., Bai, Y., Liu, J., Wang, S., Duan, L.: Veri-wild: A large dataset and a newmethod for vehicle re-identification in the wild. In: IEEE Conference on ComputerVision and Pattern Recognition. (2019)

[3] Alfasly, S., Hu, Y., Li, H., Liang, T., Jin, X., Liu, B., Zhao, Q.: Multi-label-basedsimilarity learning for vehicle re-identification. IEEE Access7(2019)

[4] Pirazh, K., Kumar, A., Peri, N., et al: A dual path modelwith adaptive attentionfor vehicle re-identification. In: IEEE International Conference on Computer Vision(2019)

[5] Yan Bai, Yihang Lou, Yongxing Dai, et al: Disentangled Feature Learning Network for Vehicle Re-Identification. In: IJCAI 2020

[6] Kuma Ratnesh and  Weill Edwin and et al: Vehicle re-identification: an efficient baseline using triplet embedding. IN IJCNN 2019

[7] Xin Jin, Cuiling Lan, Wenjun Zeng, Zhibo Chen: Uncertainty-Aware Multi-Shot Knowledge Distillation for Image-Based Object Re-Identification. In: AAAI 2020

[8] Luo Hao and Gu Youzhi and et al:Bag of Tricks and a Strong Baseline for Deep Person Re-Identification. In CVPR workshop 2019.

[9] Shen Fei, Zhu Jianqing and et al: Exploring Spatial Significance via Hybrid Pyramidal Graph Network for Vehicle Re-identification. In arXiv preprint arXiv:2005.14684

[10] Abhijit Suprem and Calton Pu: Looking GLAMORous: Vehicle Re-Id in Heterogeneous Cameras Networks with Global and Local Attention. In arXiv preprint arXiv:2002.02256

[11] Khorramshahi Pirazh, Peri Neehar, Chen Jun-cheng, Chellappa Rama: The Devil is in the Details: Self-Supervised Attention for Vehicle Re-Identification. In ECCV 2020

[12] Meng, Dechao, et al. "Parsing-based view-aware embedding network for vehicle re-identification." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.

[13] Yan Bai, Yihang Lou, Feng Gao, Shiqi Wang, Yuwei Wu, and Lingyu Duan. Group sensitive triplet embedding for vehicle re-identification. IEEE Transactions on Multimedia, 2018.

[14] Yan Bai, Jun Liu, Yihang Lou, Ce Wang, and Lingyu Duan. Disentangled Feature Learning Network and a Comprehensive Benchmark for Vehicle Re-Identification. Tpami 2021. 
