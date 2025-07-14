# VERSION 1

# # main.py
#
# from ultralytics import YOLO
# import cv2
#
# # Load YOLOv8 model
# model = YOLO("yolov8n.pt")  # Use 'yolov8n.pt' for speed, or 'yolov8m.pt' for more accuracy
#
# # Open a sample video (or use 0 for webcam)
# cap = cv2.VideoCapture("data/sample_video_2.mp4")  # Replace with 0 to use webcam
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # Run YOLOv8 inference
#     results = model(frame)[0]
#
#     # Draw results on frame
#     annotated_frame = results.plot()
#
#     # Display result
#     cv2.imshow("YOLOv8 Detection", annotated_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# ----------------------------------------------------------------------------------------------------------

# VERSION 2

# main.py

# from ultralytics import YOLO
# from deep_sort_realtime.deepsort_tracker import DeepSort
# import cv2
#
# # Load YOLOv8 model
# model = YOLO("yolov8n.pt")  # Replace with yolov8m.pt or yolov8l.pt for better accuracy
#
# # Initialize DeepSORT tracker
# tracker = DeepSort(max_age=30)
#
# # Open video
# cap = cv2.VideoCapture("data/sample_video_2.mp4")  # Use 0 for webcam
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # Run YOLO detection
#     results = model(frame, verbose=False)[0]
#
#     detections = []
#     for result in results.boxes:
#         cls = int(result.cls[0])
#         conf = float(result.conf[0])
#         label = model.names[cls]
#
#         # Filter to only vehicles (you can modify this)
#         if label in ["car", "bus", "truck", "motorbike"]:
#             x1, y1, x2, y2 = map(int, result.xyxy[0])
#             detections.append(([x1, y1, x2 - x1, y2 - y1], conf, label))
#
#     # Update tracker
#     tracks = tracker.update_tracks(detections, frame=frame)
#
#     # Draw tracked objects
#     for track in tracks:
#         if not track.is_confirmed():
#             continue
#         track_id = track.track_id
#         l, t, w, h = track.to_ltrb()
#         cv2.rectangle(frame, (int(l), int(t)), (int(l + w), int(t + h)), (0, 255, 0), 2)
#         cv2.putText(frame, f'ID: {track_id}', (int(l), int(t) - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
#
#     # Display
#     cv2.imshow("Vehicle Tracking", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# ----------------------------------------------------------------------------------------------------------

# VERSION 3
# main.py

# from ultralytics import YOLO
# from deep_sort_realtime.deepsort_tracker import DeepSort
# import cv2
# import csv
# import os
#
# # Load model
# model = YOLO("yolov8n.pt")
#
# # DeepSORT tracker
# tracker = DeepSort(max_age=30)
#
# # Video
# cap = cv2.VideoCapture("data/sample_video_2.mp4")
#
# # Unique vehicle ID store
# unique_ids = set()
#
# # Prepare CSV
# csv_file = "output/traffic_log.csv"
# os.makedirs("output", exist_ok=True)
# with open(csv_file, mode="w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Frame", "ActiveVehicles", "TotalUniqueVehicles", "CongestionLevel"])
#
# frame_count = 0
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     frame_count += 1
#     results = model(frame, verbose=False)[0]
#
#     detections = []
#     for result in results.boxes:
#         cls = int(result.cls[0])
#         conf = float(result.conf[0])
#         label = model.names[cls]
#         if label in ["car", "bus", "truck", "motorbike"]:
#             x1, y1, x2, y2 = map(int, result.xyxy[0])
#             detections.append(([x1, y1, x2 - x1, y2 - y1], conf, label))
#
#     tracks = tracker.update_tracks(detections, frame=frame)
#
#     active_ids = 0
#     for track in tracks:
#         if not track.is_confirmed():
#             continue
#         track_id = track.track_id
#         active_ids += 1
#         unique_ids.add(track_id)
#
#         l, t, w, h = track.to_ltrb()
#         cv2.rectangle(frame, (int(l), int(t)), (int(l + w), int(t + h)), (0, 255, 0), 2)
#         cv2.putText(frame, f'ID: {track_id}', (int(l), int(t) - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
#
#     # Congestion logic
#     if active_ids > 15:
#         congestion = "High"
#     elif active_ids > 5:
#         congestion = "Medium"
#     else:
#         congestion = "Low"
#
#     # Log to CSV
#     with open(csv_file, mode="a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([frame_count, active_ids, len(unique_ids), congestion])
#
#     # Display
#     cv2.putText(frame, f"Congestion: {congestion}", (10, 30),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     cv2.imshow("Vehicle Count & Congestion", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

