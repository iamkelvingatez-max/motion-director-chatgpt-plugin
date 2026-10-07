# Motion Director ChatGPT Plugin

A small Agent Plugin package that uses ChatGPT image generation for missing reference views and Remote Desktop Commander for authorized local Blender/Motion Director control.

## Install with Codex

```powershell
codex plugin marketplace add iamkelvingatez-max/motion-director-chatgpt-plugin
codex plugin add motion-director@motion-director-plugins
```

During installation, the plugin declares **Remote Desktop Commander** as required. The host must still ask the user to approve/connect that dependency; GitHub cannot silently bypass ChatGPT permissions.

## Workflow

1. Create missing side/back reference views with ChatGPT image generation. No OpenAI API key is required for that chat workflow.
2. Approve/fix inferred views.
3. Use Remote Desktop Commander to access the authorized computer.
4. Control Blender primarily through Python/`bpy` for deterministic imports, cleanup, materials, rigging, renders, saves, and exports.

The plugin source is in `motion-director/`.
