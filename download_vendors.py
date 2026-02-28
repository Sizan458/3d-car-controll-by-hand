import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download_file(url, target_path):
    print(f"Downloading {url} to {target_path}...")
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(target_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Success: {target_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VENDOR_DIR = os.path.join(BASE_DIR, 'vendor')

files_to_download = {
    # Three.js
    "https://unpkg.com/three@0.154.0/build/three.module.js": "vendor/three/three.module.js",
    "https://unpkg.com/three@0.154.0/examples/jsm/loaders/GLTFLoader.js": "vendor/three/addons/loaders/GLTFLoader.js",
    "https://unpkg.com/three@0.154.0/examples/jsm/math/MeshSurfaceSampler.js": "vendor/three/addons/math/MeshSurfaceSampler.js",
    
    # MediaPipe Camera Utils
    "https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js": "vendor/mediapipe/camera_utils.js",
    
    # MediaPipe Hands (Needs the main JS + all WASM/Models that locateFile looks for)
    "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js": "vendor/mediapipe/hands/hands.js",
    "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands_solution_packed_assets_loader.js": "vendor/mediapipe/hands/hands_solution_packed_assets_loader.js",
    "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands_solution_packed_assets.data": "vendor/mediapipe/hands/hands_solution_packed_assets.data",
    "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands_solution_simd_wasm_bin.js": "vendor/mediapipe/hands/hands_solution_simd_wasm_bin.js",
    "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands_solution_simd_wasm_bin.wasm": "vendor/mediapipe/hands/hands_solution_simd_wasm_bin.wasm",
    "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.binarypb": "vendor/mediapipe/hands/hands.binarypb",
    "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hand_landmark_full.tflite": "vendor/mediapipe/hands/hand_landmark_full.tflite",
    "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hand_landmark_lite.tflite": "vendor/mediapipe/hands/hand_landmark_lite.tflite",
    
    # Fonts (We'll just grab the WOFF2 files directly from Google Fonts API)
    # Orbitron Regular
    "https://fonts.gstatic.com/s/orbitron/v31/yq5jcI3oO5IrmO8Wp60g9iAqzS55yY_3iA.woff2": "vendor/fonts/orbitron-regular.woff2",
    # Rajdhani Regular
    "https://fonts.gstatic.com/s/rajdhani/v15/LDIx-APCE2e0CGNEa773-KcwO-i-Gg.woff2": "vendor/fonts/rajdhani-regular.woff2",
}

for url, path in files_to_download.items():
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        download_file(url, full_path)
    else:
        print(f"Skipping {path}, already exists.")

print("Done downloading vendors.")
