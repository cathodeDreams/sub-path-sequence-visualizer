# sub-path-sequence-visualizer

A Three.js-based visualization tool that renders multiple planes following parametric paths in 3D space. Supports various path types including spiral, wave, helix, lemniscate, and torus knot patterns.

## Features
- Interactive 3D visualization with orbit controls
- Multiple path generation algorithms
- Adjustable path complexity and smoothness
- Configurable plane styles and sizes
- Animation speed control
- Video recording capability (WebM/MP4)
- Post-processing effects with bloom

## Usage
Open `index.html` in a modern web browser. Requires internet connection for CDN dependencies (Three.js and CCapture.js).

## Controls
- Path Style: Select different path generation algorithms
- Plane Style: Modify plane animation behavior
- Base Plane Size: Adjust plane dimensions
- Animation Speed: Control movement speed
- Path Complexity: Modify number of control points and path smoothness
- Record Animation: Save animation as video file
- Generate New Path: Create new path with current settings

## Optional
Contains a python script to convert the WebM video to an MP4 file. Just run the script for tkinter GUI.

## Dependencies
- Three.js (0.157.0)
- CCapture.js
- ffmpeg (optional for conversion to mp4)
- python (optional for conversion to mp4)