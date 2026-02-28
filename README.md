# 🏎️ Rayfield Caliburn — Particle Deconstructor

A futuristic, high-performance 3D car visualization powered by **Three.js** and controlled entirely by **Hand Gestures** via **MediaPipe**. Experience the Rayfield Caliburn as it deconstructs and reassembles in a stunning particle matrix.

---

## 🌐 Live Demo
Experience the interactive visualization directly in your browser:
**[View Live Demo →](https://3d-car-controll-by-hand.vercel.app/)**

---

## 🌌 Project Vision
The **Rayfield Caliburn — Particle Deconstructor** is an experimental 3D interface that reimagines vehicle visualization. Rather than a static model, the car is a dynamic entity composed of thousands of intelligent particles. This project explores the boundary between physical structure and digital flux, allowing users to "atomize" a high-performance vehicle using natural hand movements.

---

## 🎮 Hand Gesture Master Guide
Control the interface using your webcam. The system maps hand landmarks to 3D scene actions in real-time.

| Gesture           | Action           | Technical Logic                                                                                    |
| :---------------- | :--------------- | :------------------------------------------------------------------------------------------------- |
| **✊ Full Fist** | **Assemble** | Triggered when all fingertips (points 8, 12, 16, 20) are below their respective knuckles.          |
| **🖐 Open Hand** | **Deconstruct** | Default state when no specific gesture is detected. Triggers particle dispersion.                  |
| **☝ Pointing** | **Orbit Camera** | Detected when Index (8) is up and others are down. Maps finger x/y to camera orbit angles.       |
| **🙌 Two Hands** | **Zoom In/Out** | Calculates Euclidean distance between hand centers, mapping delta to Camera FOV.                   |
| **👋 Fast Swipe** | **Explosion** | Monitors wrist (landmark 0) velocity. Exceeding 0.015 units/ms triggers a vertex shader burst.   |

---

## 🏗️ Technical Architecture

### 💎 Graphics Engine (Three.js + GLSL)
The system renders over **100,000 active particles** using a single `THREE.Points` object.
* **Particle Sampling**: Uses `MeshSurfaceSampler` to distribute particles across the original GLB mesh geometry via barycentric coordinate sampling.
* **Custom Shaders**:
    * **Vertex Shader**: Handles the "Morph" logic by interpolating between `startPosition` and `targetPosition`. Includes a "Breathing" sine-wave animation for the assembled state.
    * **Fragment Shader**: Renders soft, circular particles with additive blending and a bright radioactive core.

### 🧠 Intelligence Layer (MediaPipe)
* **Model Tracking**: Uses MediaPipe Hands with adaptive complexity.
* **Performance Scaling**:
    * **Desktop**: Full model complexity (1) for precise tracking.
    * **Mobile**: Lite model complexity (0) and throttled frame processing to maintain 60FPS.

---

## ⚙️ Performance Engineering
The application features an **Adaptive Matrix** system that scales based on hardware capabilities:

| Platform            | Particle Count | ML Complexity | Rendering Optimization              |
| :------------------ | :------------- | :------------ | :---------------------------------- |
| **PC / High-End** | 100,000+       | Full (1)      | Antialiasing On, High DPR           |
| **Mobile / Tablet** | 25,000         | Lite (0)      | Antialiasing Off, Clamped DPR (1.0) |

---

## 🛠️ Developer Setup

1.  **Dependency Management**:
    The project includes a script to fetch necessary assets (Three.js, MediaPipe) locally.
    ```bash
    python3 download_vendors.py
    ```

2.  **Local Server**:
    Due to CORS rules for ES Modules, run a local server:
    ```bash
    # Using Python
    python3 -m http.server 8000

    # Using Node.js
    npx serve .
    ```

3.  **Access**:
    Open `http://localhost:8000/3Dcar.html` in a modern, WebGL2-compatible browser.

---

## 🔮 Future Work Roadmap
* **🌐 Multiplayer Sync**: Shared sessions for collaborative deconstruction via WebSockets.
* **💥 Physical Collisions**: Particle-to-particle collision physics for realistic dispersion.
* **🕶️ Extended Reality**: WebXR support for immersive AR/VR experiences.
* **🏗️ Custom Car Modeler**: Interface to "particle-ize" user-uploaded `.glb` models.

---

_Engineered for visual excellence and interactive immersion._ 🥂
