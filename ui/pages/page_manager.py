from ui.pages.registry import get_page_class

class PageManager:
    """This controls the creation and deletion of pages."""

    def __init__(self, board):
        self.board = board
        self.pages = []
        print("[PageManager] init pages complete.")

    # --------------------------
    # Public API
    # --------------------------
    def fabric_page(self, page_cls, **kwargs):
        page = page_cls(self.board, **kwargs)
        page.show()
        self.pages.append(page)
        return page

    def render_page(self, page_id):
        page_cls = get_page_class(page_id)
        if not page_cls:
            print(f"[PageManager] No page for id {page_id}")
            return

        return self.fabric_page(page_cls)

