from ultralytics import YOLO

print("Loading YOLO model...")

model = YOLO("yolov8n.pt")

print("Starting detection...")

try:
    for result in model.predict(
        source="data/Store 1/CAM 3 - entry.mp4",
        stream=True,
        imgsz=160,
        verbose=False,
        device="cpu"
    ):
        pass

    print("Detection Complete")

except Exception as e:
    print("Detection finished with warning:")
    print(e)
