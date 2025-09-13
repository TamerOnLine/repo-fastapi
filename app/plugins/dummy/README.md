# 🧩 Dummy Plugin

This is a **demo plugin** used as a template to test the plugin system.  
It does not perform real inference tasks, but returns a success message and echoes back the received payload.

---

## 📌 Metadata
- **Name:** `dummy`
- **Provider:** `dummy`
- **Supported tasks:** `ping`

---

## 🚀 Run the Task

### Endpoint
```
POST /plugins/dummy/ping
```

### Request Body (JSON)
```json
{
  "hello": "world"
}
```

### Example (cURL)
```bash
curl -X POST http://127.0.0.1:8000/plugins/dummy/ping \
     -H "Content-Type: application/json" \
     -d '{"hello": "world"}'
```

### Expected Response
```json
{
  "plugin": "dummy",
  "result": {
    "task": "ping",
    "message": "✅ Dummy service is working",
    "payload_received": {
      "hello": "world",
      "task": "ping"
    }
  }
}
```

---

## 📖 Notes
- The Dummy Plugin is **for testing purposes only**.  
- It can serve as a **starting point** for building new plugins: just replace the logic in `infer()` and update the `manifest.json`.
