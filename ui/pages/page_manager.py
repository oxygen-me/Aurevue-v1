from ui.pages.registry import get_page_class
from PySide6.QtCore import Qt
from eventbus import bus

class PageManager:
    def __init__(self, layer):
        self.layer = layer
        self.current = None
        bus.configRequested.connect(self.render_page)

    def fabric_page(self, page_cls, **kwargs):
        page = page_cls(self.layer, **kwargs)
        page.setGeometry(self.layer.rect())
        return page

    def render_page(self, page_id):
        page_cls = get_page_class(page_id)
        if not page_cls:
            print(f"[PageManager] No page for id {page_id}")
            return

        if self.current:
            self.current.setParent(None)
            self.current.deleteLater()

        page = self.fabric_page(page_cls)

        self.current = page
        page.show()
        page.apply_theme()

        self.layer.show()
        self.layer.raise_()