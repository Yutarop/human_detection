古澤君用

## Setup
```bash
$ cd ~/{ROS2_WORKSPACE}/src
$ git clone https://github.com/Yutarop/human_detection.git
$ cd ~/{ROS2_WORKSPACE} && $ colcon build
$ source ~/.bashrc
```

## Run
実機でデータを取る時やBagファイルを再生するときに、Launchしてください。
```bash
$ ros2 launch human_detection human_detec.launch.xml
```
点群を前処理するためのノードを立ち上げるコマンドです。
```bash
$ ros2 run human_detection pre_processing
```

## DBSCAN後の結果を表示
display_pcdのディレクトリに、DBSCANした後のグラフを表示させるpythonファイルがあります。<p>
x, y座標のみの情報でクラスタリングさせたい場合
```bash
$ cd ~/{ROS2_WORKSPACE}/src/human_detection/display_pcd
$ python3 display_cluster_2d.py
```
x, y, z座標の情報でクラスタリングさせたい場合
```bash
$ cd ~/{ROS2_WORKSPACE}/src/human_detection/display_pcd
$ python3 display_cluster_2d.py
```
