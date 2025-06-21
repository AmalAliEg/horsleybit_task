
# ---------- (اختياري) app2/routers.py (Database Router) ----------
class TradingRouter:
    """يوجّه موديلات app2 إلى قاعدة البيانات 'default'."""
    app_label = "app2"

    def db_for_read(self, model, **hints):
        return "default" if model._meta.app_label == self.app_label else None

    def db_for_write(self, model, **hints):
        return "default" if model._meta.app_label == self.app_label else None