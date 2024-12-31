

---

# Leaf Disease Detection and Segmentation Model

This project aims to develop an effective model for detecting and segmenting diseases in leaves using both supervised and semi-supervised learning approaches. The model leverages state-of-the-art architectures and techniques to accurately identify leaf diseases and assess the severity of infections.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Model Training](#model-training)
4. [Evaluation](#evaluation)
5. [Post-Processing](#post-processing)
6. [Installation](#installation)
7. [Usage](#usage)
8. [License](#license)

## Project Overview
This project involves training a deep learning model to detect and classify various leaf diseases. The approach uses a combination of manually annotated and semi-supervised data to increase dataset size and model accuracy. The model also includes post-processing to assess the severity of infections by calculating the affected area.

## Dataset
The dataset used for training and evaluation includes images of plant leaves with different diseases. The dataset is divided into:
- **Training Set**: Manually annotated images (472 images initially, expanded using semi-supervised methods).
- **Validation Set**: 280 manually annotated images for evaluation.

### Data Augmentation
To improve the robustness of the model, the dataset undergoes augmentation, including transformations like hue and saturation adjustments, ensuring a diverse range of data for training.

## Model Training
1. **Initial Model Training**:
   - A deep learning model was initially trained on a manually annotated dataset. Transfer learning was employed to fine-tune a pre-trained model for better performance.
   
2. **Semi-Supervised Learning**:
   - Semi-supervised learning techniques were used to automatically annotate additional data, reducing the need for manual labeling.
   - Incorrect or questionable annotations were manually reviewed and corrected in two iterations to improve accuracy.

3. **Cross-Validation**:
   - Cross-validation was conducted using the semi-supervised annotations, demonstrating the model's ability to generalize well even with mostly automated data.

## Evaluation
Several state-of-the-art models were evaluated to determine the best-performing architecture for this task. YOLOv8 was selected due to its superior performance in both detection accuracy and processing speed.

### Performance Metrics
- **Mask mAP**: 0.766
- **Box mAP**: 0.791
- **Validation Set**: Fixed at 280 manually annotated images.

## Post-Processing
Post-processing techniques were applied to calculate the percentage of the affected area on each leaf. This analysis helps determine the severity of infections:
- Leaves with severe infections are marked for discarding.
- Leaves with mild to moderate infections are treated with appropriate measures such as fertilizers.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ANaik611/plant_disease_detection_and_segmentation.git
   cd plant_disease_detection_and_segmentation

   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the model and make predictions on new images:

1. Prepare your image dataset and place it in a folder.
2. Run the following command to start the prediction process:
   ```bash
   !yolo task=segment mode=predict model=/path/to/best.pt conf=0.30 source=/path/to/images project=/path/to/output
   ```
   - Replace `/path/to/best.pt` with the path to your trained model.
   - Set the `conf` parameter to adjust the confidence threshold for predictions.
   - The predictions will be saved in the specified output folder.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README provides a clear overview of the project, how to use it, and the necessary steps for installation and execution. Adjust the paths and specific details according to your project's setup.
