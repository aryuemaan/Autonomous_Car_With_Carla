# Autonomous Car Project

This project aims to develop an autonomous car using the Carla simulation platform and Python simulations. The project is divided into multiple stages, starting with the implementation of basic Python structures before transitioning to the Carla simulator.

## Project Overview

The goal of this project is to create a fully autonomous car that can navigate and make decisions based on its surroundings. The project uses a combination of computer vision techniques, machine learning algorithms, and robotic control to achieve autonomous driving capabilities. we can create map using RoadRunner Software which is owened by Mathworks

## Implementation Steps

1. **Lane Detection**: The first stage of the project involves developing a lane detection system. This system uses computer vision techniques to identify and track the lanes on the road. By analyzing the lane markings, the car can determine its position within the lane and make appropriate steering adjustments.

2. **Object Detection**: In the second stage, an object detection system is implemented. This system utilizes deep learning algorithms to detect and classify various objects present in the environment, such as vehicles, pedestrians, and obstacles. Accurate object detection is crucial for ensuring the safety of the autonomous car and enabling it to respond appropriately to different scenarios.

3. **Pedestrian Detection**: Building upon the object detection system, a specialized module for pedestrian detection is developed. This module focuses on identifying and tracking pedestrians specifically, as they are one of the most important objects to be aware of when driving autonomously. It helps the car anticipate and respond to pedestrian movements, ensuring their safety and preventing accidents.

4. **Traffic Signal Detection**: The next step involves implementing a traffic signal detection system. This module is responsible for recognizing and interpreting traffic signals, including traffic lights and stop signs. By accurately detecting and understanding traffic signals, the autonomous car can make informed decisions regarding speed, acceleration, and stopping at intersections.

## Carla Simulation

Once the above modules are implemented and tested using normal Python simulations, the project transitions to the Carla simulator. Carla is an open-source simulator specifically designed for autonomous driving research. It provides a realistic 3D environment for testing and validating autonomous driving algorithms.

By integrating the developed modules into the Carla simulator, the autonomous car can operate in a virtual world, closely mimicking real-world driving conditions. This allows for more realistic and comprehensive testing, enabling the refinement and improvement of the autonomous driving system.

## Conclusion

The project has successfully achieved the following milestones:

- Implemented a lane detection system for accurately tracking the lanes on the road.
- Developed an object detection module capable of detecting and classifying various objects in the environment.
- Created a specialized pedestrian detection system for identifying and tracking pedestrians.
- Implemented a traffic signal detection module to recognize and interpret traffic signals.

The project has now transitioned to the Carla simulator, where the developed modules will be integrated and further tested. This will enable the autonomous car to navigate and make decisions in a realistic virtual environment, paving the way for future advancements in autonomous driving technology.
