---
name: motion-director
description: Use when a user wants ChatGPT to create reference views for Motion Director, control Blender on an authorized computer, prepare a 3D asset, or automate Motion Director/Blender work without OpenAI API keys.
---

# Motion Director

Use ChatGPT's built-in image generation for the image-creation stage. Do not require or request an OpenAI API key for this workflow.

## Required local connection

Remote Desktop Commander is a required app dependency for local computer control. Use it to access the user's authorized computer, inspect files, run Motion Director, start Blender, run Blender Python, and collect rendered verification outputs.

If Remote Desktop Commander is unavailable or not connected, tell the user that the local Blender stage cannot run until they approve/connect that dependency. Do not claim local actions succeeded without tool evidence.

## Reference-image workflow

1. Keep the user's original image unchanged as the source reference.
2. Use ChatGPT image generation to create only the missing useful views, typically left/45-degree, right/45-degree, and back.
3. Treat hidden sides as inferred, not recovered facts.
4. Let the user correct or regenerate a bad inferred view before using it downstream.
5. Preserve approved views as separate image files rather than a collage.

## Blender workflow

Prefer deterministic Blender Python over mouse automation.

1. Use Remote Desktop Commander to find Blender. Check PATH and normal install locations before assuming a path.
2. Use Blender in background mode when a visible window is not needed: `blender --background --python <script>`.
3. Use `bpy` for imports, scene setup, mesh cleanup, materials, cameras, rigging, rendering, saving, and export.
4. Keep destructive or broad filesystem actions scoped to the Motion Director project and user-selected files.
5. Render verification angles and compare them with the approved reference views before claiming the asset is ready.

Typical Blender operations include importing GLB/FBX/OBJ, adding reference cameras, cleaning geometry, assigning textures/materials, creating or attaching a rig, rendering test views, exporting GLB/FBX, and saving the .blend project.

## Motion Director

Prefer Motion Director's existing local project, CLI, or MCP-backed workflow when it already provides the requested operation. Use Remote Desktop Commander as the bridge from ChatGPT to the user's computer; do not introduce a second cloud API merely to control local Motion Director or Blender.

## Completion rule

Report separately what ChatGPT generated, what was approved by the user, what was actually executed on the local computer, and what remains unverified.
