# 🏎️ Rayfield Caliburn — Particle Deconstructor

A futuristic, high-performance 3D car visualization powered by **Three.js** and controlled entirely by **Hand Gestures** via **MediaPipe**. Experience the Rayfield Caliburn as it deconstructs and reassembles in a stunning particle matrix.

---

## 🌌 Project Vision

The **Rayfield Caliburn — Particle Deconstructor** is an interactive experimental 3D interface. It reimagines vehicle visualization not as a static model, but as a dynamic entity composed of thousands of intelligent particles. The core concept explores the boundary between physical structure and digital flux, allowing users to "atomize" a high-performance vehicle into its constituent components using natural hand movements.

---

## 🎮 Hand Gesture Master Guide

Control the interface using your webcam. The system uses a coordinate-based gesture recognition engine to map hand landmarks to 3D scene actions.

| Gesture           | Action           | Technical Logic                                                                                    |
| :---------------- | :--------------- | :------------------------------------------------------------------------------------------------- |
| **✊ Full Fist**  | **Assemble**     | Triggered when all fingertips (points 8, 12, 16, 20) are below their respective knuckles.          |
| **🖐 Open Hand**  | **Deconstruct**  | Default state when no specific gesture is detected. Triggers particle dispersion.                  |
| **☝ Pointing**    | **Orbit Camera** | Detected when Index (8) is up and others are down. Maps finger `x/y` to camera orbit angles.       |
| **🙌 Two Hands**  | **Zoom In/Out**  | Calculates Euclidean distance between hand centers. Mapping distance Delta to Camera FOV/Distance. |
| **👋 Fast Swipe** | **Explosion**    | Monitors wrist (landmark 0) velocity. Exceeding `0.015` units/ms triggers a vertex shader burst.   |

---

## 🏗️ Technical Architecture

### 💎 Graphics Engine (Three.js + GLSL)

The system renders over **100,000 active particles** using a single `THREE.Points` object.

- **Particle Sampling**: Uses `MeshSurfaceSampler` to distribute particles across the original GLB mesh geometry via barycentric coordinate sampling.
- **Custom Shaders**:
  - **Vertex Shader**: Handles the "Morph" logic by interpolating between `startPosition` (explosion shell) and `targetPosition` (car mesh). Includes a "Breathing" sine-wave animation for the assembled state.
  - **Fragment Shader**: Renders soft, circular particles with an additive blending glow effect and a bright radioactive core.

### 🧠 Intelligence Layer (MediaPipe)

- **Model Tracking**: Uses `MediaPipe Hands` with adaptive complexity.
- **Performance Scaling**:
  - **Desktop**: Full model complexity (1) for precise tracking.
  - **Mobile**: Lite model complexity (0) and throttled frame processing to maintain 60FPS.

---

## ⚙️ Performance Engineering

The application features an **Adaptive Matrix** system that scales based on hardware capabilities:

| Platform            | Particle Count | ML Complexity | Rendering Optimization              |
| :------------------ | :------------- | :------------ | :---------------------------------- |
| **PC / High-End**   | 100,000+       | Full (1)      | Antialiasing On, High DPR           |
| **Mobile / Tablet** | 25,000         | Lite (0)      | Antialiasing Off, Clamped DPR (1.0) |

---

## ⬡ Component Map (Technical Specs)

The vehicle is divided into functional modules, each with unique particle densities and physics properties.

| Component       | Color     | Technical Specification              | Material Basis    |
| :-------------- | :-------- | :----------------------------------- | :---------------- |
| **Body Shell**  | `#00d4ff` | Aerodynamic Carbon-Ceramic Monocoque | Composite Fiber   |
| **Power Unit**  | `#ff3366` | 1,200 BHP Twin-Turbo Hybrid V12      | Titanium-Alloy    |
| **Front Aero**  | `#00ff88` | Active Splitter (350kg Downforce)    | Carbon Polymer    |
| **Interior**    | `#aa66ff` | Holographic HUD Interface            | Alcantara Trim    |
| **Brakes**      | `#ff2244` | 420mm Carbon-Ceramic Discs           | Ceramic Sinter    |
| **Engine Hood** | `#ffaa00` | Vented NACA Duct Geometry            | 3.2kg Ultra-light |

---

## 🛠️ Developer Setup

1.  **Dependency Management**:
    The project includes a `download_vendors.py` script to fetch all necessary assets (Three.js, MediaPipe) locally for offline use.

    ```bash
    python3 download_vendors.py
    ```

2.  **Local Server**:
    Due to Cross-Origin Resource Sharing (CORS) rules for ES Modules, run:

    ```bash
    # Option 1: Python
    python3 -m http.server 8000

    # Option 2: Node.js
    npx serve .
    ```

3.  **Access**:
    Open `http://localhost:8000/3Dcar.html` in a modern, WebGL2-compatible browser.

---

## 🔮 Future Work Roadmap

We are continuously evolving the Rayfield Caliburn experience. Planned updates include:

- **🌐 Multiplayer Synchronization**: Real-time shared 3D sessions using WebSockets for collaborative deconstruction.
- **💥 Physical Collisions**: Integration of particle-to-particle collision physics for more realistic dispersion.
- **🕶️ Extended Reality (XR)**: WebXR support for immersive AR/VR experiences directly in the browser.
- **🏗️ Custom Car Modeler**: An interface for users to upload and "particle-ize" their own `.glb` or `.gltf` models.
- **✨ Advanced Environment Mapping**: Ray-traced dynamic reflections on assembled meshes using real-time environment probes.

---

_Engineered for visual excellence and interactive immersion._ 🥂
