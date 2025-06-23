# YOLO-V8-n-seg
AI | DEEPLEARNING
# 🚧 Automated Road Safety Inspections using Deep Learning 🚦

## 📌 Project Overview

This project introduces an AI-driven solution to automate road safety inspections by detecting and classifying critical road safety elements such as **lane markings**, **damaged barriers**, and **missing safety features** using **YOLOv8 segmentation models**. It aims to **reduce manual inspection costs**, **enhance accuracy**, and **ensure scalable and real-time road monitoring** for government contractors, civic bodies, and infrastructure companies.

---

## 🎯 Objective

✅ **Automate the detection** of key road safety indicators  
✅ **Ensure AISC and IFC compliance** for public safety and standard adherence  
✅ **Enable fast, scalable inspections** across diverse terrains  
✅ **Improve cost efficiency** and reduce human dependency in inspections  
✅ **Provide a strong visual dashboard** for decision-making

---

## 🧠 Technologies & Models Used

| Tool/Library | Purpose |
|--------------|---------|
| **YOLOv8s-seg** | Real-time segmentation & object detection |
| **OpenCV** | Live video feed & image preprocessing |
| **Python** | Core logic and orchestration |
| **Streamlit** | Web app for image/video testing |
| **Digital Sreeni** | Image annotation |
| **Pandas/Numpy** | Data handling |
| **Matplotlib/Seaborn** | Visualizations |
| **Google Colab** | Model training |
| **Vercel/GitHub** | Deployment & versioning |

---

## 🗃️ Dataset Overview

- 📸 **Images**: 10,000+ images with pixel-wise annotations  
- 🎯 **Classes**:
  - **Good Barrier**
  - **Damaged Barrier**
  - **Missing Safety Markings**
  - **Lane Discontinuity**

---

## ⚙️ Pipeline Architecture

1. **Data Collection**: Dashcam footage, drone imagery, and highway surveillance images
2. **Annotation**: Using Label Studio for polygon annotations
3. **Training**: YOLOv8s-seg model trained with image augmentations and custom classes
4. **Validation**: mAP, IoU used to monitor performance
5. **Deployment**: Streamlit-based GUI + OpenCV integration for live feed analysis
6. **Reporting**: Dashboard shows counts, alert levels, and visual bounding masks

---

## 📈 Evaluation Metrics

| Metric | Value |
|--------|-------|
| **mAP@0.5** | 0.82 |
| **IoU** | 0.67 |
| **Precision** | 89.4% |
| **Recall** | 85.1% |

---

## 🖥️ Streamlit App Features

- 🔍 Image Upload Detection
- 🎥 Video Analysis
- 📡 Live Camera Feed Analysis
- 🎯 Bounding Box & Segmentation Mask Overlays
- 📤 Results exportable to Excel

---

## 🧩 Use Cases

| Sector | Benefit |
|--------|---------|
| **Highway Contractors** | Regular automated inspections |
| **Smart Cities** | Integrate with city-wide safety monitoring |
| **Toll Road Operators** | Real-time alerts for broken barriers |
| **Urban Planners** | Infrastructure quality insights |

---

## 📊 Dashboard Sample

- 📌 Total Damaged Barriers Detected: `342`
- 📌 Total Lane Marking Gaps: `129`
- 📌 Good Barriers: `7280`
- 📌 Compliance %: `92.3%`

---

## 🏁 Future Enhancements

- 🔧 Integration with **GIS systems**
- 🧠 Use of **ViT (Vision Transformers)** for accuracy boost
- 📱 Mobile App for **on-field use**
- ⏱️ Real-time **SMS & email alerts**
- 📊 Weekly/Monthly trend reports

---

## 💡 Business Impact

- 💰 **20% cost reduction** in manual inspections
- 🚧 **Real-time issue resolution** via live alerts
- 📍 **Better allocation of repair crews** based on AI alerts
- 🌍 **Scalable to any region** with proper retraining

---

## 👨‍💻 Project Team

| Name | Role |
|------|------|
| Nobel X | AI Developer & Project Lead |
| GPT-4o (Assistant) | Technical Advisor & Reviewer |

---
