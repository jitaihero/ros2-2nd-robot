# ROS2 2nd Robot

《ROS 2 机器人开发：从入门到实践（第 2 版）》学习代码仓库。

## 章节目录

| 章节 | 内容 | 目录 |
| --- | --- | --- |
| 第 7 章 | BFS 广度优先遍历、URDF 建模、Gazebo 仿真 | [`chapt7/`](./chapt7) |

## 使用方式

将对应章节的 ROS2 功能包复制到工作空间的 `src/` 下再编译：

```bash
mkdir -p ~/ros2_ws/src
cp -r chapt7/py_sprint ~/ros2_ws/src/
cd ~/ros2_ws
colcon build --packages-select py_sprint
source install/setup.bash
```
