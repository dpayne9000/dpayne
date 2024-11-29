import curses
import requests
from typing import Any, Dict


class HttpRequester:
    def __init__(self):
        self.method = "GET"
        self.url = ""
        self.headers = {}
        self.body = ""
        self.response = None

    def start_ui(self) -> None:
        curses.wrapper(self.main)

    def main(self, stdscr: Any) -> None:
        curses.curs_set(1)
        stdscr.clear()
        stdscr.refresh()

        current_field = 0
        fields = ["Method", "URL", "Headers", "Body", "Send Request"]
        while True:
            stdscr.clear()
            self.display_interface(stdscr, fields, current_field)

            key = stdscr.getch()

            if key == curses.KEY_UP:
                current_field = max(0, current_field - 1)
            elif key == curses.KEY_DOWN:
                current_field = min(len(fields) - 1, current_field + 1)
            elif key in (curses.KEY_ENTER, 10, 13):  # Enter key
                if current_field == 0:
                    self.method = self.edit_field(stdscr, "Method", self.method)
                elif current_field == 1:
                    self.url = self.edit_field(stdscr, "URL", self.url)
                elif current_field == 2:
                    self.headers = self.edit_headers(stdscr, self.headers)
                elif current_field == 3:
                    self.body = self.edit_field(stdscr, "Body", self.body)
                elif current_field == 4:
                    self.send_request(stdscr)
            elif key == ord("q"):
                break

            stdscr.refresh()

    def display_interface(self, stdscr: Any, fields: list, current_field: int) -> None:
        h, w = stdscr.getmaxyx()
        for idx, field in enumerate(fields):
            x = 2
            y = idx * 2 + 1
            if idx == current_field:
                stdscr.addstr(y, x, f"> {field}: ", curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"  {field}: ")

            if field == "Method":
                stdscr.addstr(y, x + 10, self.method)
            elif field == "URL":
                stdscr.addstr(y, x + 10, self.url)
            elif field == "Headers":
                stdscr.addstr(y, x + 10, str(self.headers))
            elif field == "Body":
                stdscr.addstr(y, x + 10, self.body)

    def edit_field(self, stdscr: Any, field_name: str, current_value: str) -> str:
        curses.curs_set(1)
        edit_win = curses.newwin(3, curses.COLS - 4, 1, 2)
        edit_win.addstr(
            0, 0, f"Editing {field_name} (Press Enter to confirm, Esc to cancel):"
        )
        edit_win.addstr(1, 0, current_value)
        stdscr.refresh()

        curses.echo()
        new_value = edit_win.getstr(1, 0).decode("utf-8")
        curses.noecho()
        return new_value

    def edit_headers(
        self, stdscr: Any, current_headers: Dict[str, str]
    ) -> Dict[str, str]:
        curses.curs_set(1)
        edit_win = curses.newwin(10, curses.COLS - 4, 1, 2)
        edit_win.addstr(
            0, 0, "Editing Headers (Press Enter to confirm, Esc to cancel):"
        )
        y_offset = 1
        for k, v in current_headers.items():
            edit_win.addstr(y_offset, 0, f"{k}: {v}")
            y_offset += 1

        new_headers = {}
        stdscr.refresh()
        curses.echo()
        while True:
            edit_win.addstr(
                y_offset,
                0,
                "Add header (format key:value, or just press Enter to finish):",
            )
            header_input = edit_win.getstr(y_offset + 1, 0).decode("utf-8")
            if not header_input:
                break
            if ":" in header_input:
                key, value = map(str.strip, header_input.split(":", 1))
                new_headers[key] = value
                y_offset += 2
        curses.noecho()
        return new_headers

    def send_request(self, stdscr: Any) -> None:
        try:
            response = requests.request(
                method=self.method, url=self.url, headers=self.headers, data=self.body
            )
            self.response = response
            self.display_response(stdscr)
        except requests.RequestException as e:
            self.response = None
            stdscr.clear()
            stdscr.addstr(0, 0, f"Failed to make request: {str(e)}")
            stdscr.refresh()
            stdscr.getch()

    def display_response(self, stdscr: Any) -> None:
        if self.response is None:
            return

        curses.curs_set(0)
        stdscr.clear()
        response_text = f"Status Code: {self.response.status_code}\n\nHeaders:\n{self.response.headers}\n\nBody:\n{self.response.text}"

        y_offset = 0
        for line in response_text.splitlines():
            if y_offset >= curses.LINES - 1:
                break
            stdscr.addstr(y_offset, 0, line[: curses.COLS - 1])
            y_offset += 1

        stdscr.refresh()
        stdscr.addstr(curses.LINES - 1, 0, "Press any key to return...")
        stdscr.getch()


if __name__ == "__main__":
    requester = HttpRequester()
    requester.start_ui()
