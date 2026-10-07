# ChatGPT / Codex plugin setup

Motion Director includes a local Agent Plugin package at the repository root.

## Install behavior

The plugin declares **Remote Desktop Commander** as a required dependency. When the host supports app dependencies, installing Motion Director prompts the user to approve/connect Remote Desktop Commander. That approval cannot be silently bypassed.

After approval:

1. ChatGPT uses its built-in image generation to make missing reference views. No OpenAI API key is required for that image step.
2. Remote Desktop Commander provides authorized access to the user's computer.
3. Blender is controlled primarily through deterministic Python/`bpy` scripts.
4. Motion Director files, renders, imports, exports and Blender projects stay on the user's machine unless the user explicitly chooses otherwise.

The dependency declaration lives in `.app.json`; the workflow instructions live in `skills/motion-director/SKILL.md`.
