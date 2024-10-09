import os

def read_yolo_instance_segmentation_file(file_path):
    """Read and parse a YOLO instance segmentation text file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    annotations = []
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        points = [(float(parts[i]) * 256, float(parts[i + 1]) * 256) for i in range(1, len(parts), 2)]
        annotations.append((class_id, points))

    return annotations

def polygon_area(points):
    """Calculate the area of a polygon using the Shoelace formula."""
    n = len(points)
    if n < 3:
        return 0  # Not a polygon

    area = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2
        area -= x2 * y1
    area = abs(area) / 2.0
    return area

# Path to the directory containing YOLO instance segmentation text files
txt_dir = '/content/runs/segment/predict3/labels'

total_area = 0.0
image_size = 640  # Image width and height in pixels

# Loop through each file in the directory
for filename in os.listdir(txt_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(txt_dir, filename)

        # Read and parse the file
        annotations = read_yolo_instance_segmentation_file(file_path)

        # Calculate the area for each annotation
        for class_id, points in annotations:
            area = polygon_area(points)
            total_area += area
            print(f"Class ID: {class_id}, Area: {area:.2f} pixels")

print(f"Total Area Covered: {total_area:.2f} pixels")