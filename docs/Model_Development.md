# Model Development

## Overview

The development phase focused on understanding different deep learning architectures before integrating a Vision-Language Model into the application.

Several convolutional neural network (CNN) architectures were explored to gain practical experience with feature extraction and transfer learning.

---

## Models Explored

### Custom CNN

A baseline CNN was implemented to understand the fundamentals of convolutional neural networks, including convolution, pooling, and fully connected layers.

### ResNet

ResNet was evaluated for its residual learning approach, allowing deeper networks to train more effectively.

### EfficientNet

EfficientNet was explored for its balance between accuracy and computational efficiency through compound scaling.

### MobileNet

MobileNet was investigated as a lightweight architecture suitable for deployment in resource-constrained environments.

---

## Final Model

The final application integrates the **BLIP (Bootstrapping Language-Image Pre-training)** Vision-Language Model.

Unlike traditional image classifiers, BLIP generates natural language descriptions for uploaded images.

Workflow:

```
Input Image
      │
      ▼
Vision Encoder
      │
      ▼
Language Decoder
      │
      ▼
Generated Caption
```

---

## Key Learning Outcomes

- Understanding CNN architectures
- Applying transfer learning
- Working with Vision-Language Models
- Integrating pretrained models into applications
