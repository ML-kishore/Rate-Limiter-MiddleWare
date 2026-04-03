# Django Custom Rate Limiter Middleware 🛡️

A lightweight, production-ready **Sliding Window Rate Limiter** built from scratch using Django Middleware. No external libraries required.

## 🚀 Overview
This middleware acts as a "Global Bouncer" for your Django application. It tracks incoming requests by **IP Address** and enforces a limit within a specific time window.

### Key Features:
* **Sliding Window Logic:** Uses Python's `time` module to track request history.
* **Non-Blocking:** Only blocks requests that exceed the limit, letting valid traffic pass through.
* **DRF Compatible:** Includes `.render()` handling for Django Rest Framework responses.
* **Efficiency:** Stops unauthorized requests *before* they hit your Views or Database.

##  How the Logic Works (Sliding Window)
Instead of a "Fixed" timer that resets at 00:00, this uses a **Sliding Window**:
1. Every request is recorded with a timestamp.
2. The middleware automatically "garbage collects" timestamps older than **60 seconds**.
3. If the count of active timestamps > **5**, the user is blocked with a `429 Too Many Requests` status.

##  Installation

1. **Add the file:** Place `middleware.py` in your app folder.
2. **Update Settings:** Add the middleware to your `MIDDLEWARE` list in `settings.py`.

```python
MIDDLEWARE = [
    # Put it near the top to block traffic early!
    'your_app.middleware.rate_limiter_middleware', 
    'django.middleware.security.SecurityMiddleware',
    # ...
]
