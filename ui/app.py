import sys
import threading
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QLineEdit, QPushButton
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QTimer

from agents.llm_agent import ask_llm
from memory.conversation_memory import add_message
from voice.tts import speak


class VoiceBubble(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setFixedSize(70, 70)

        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint
        )

        self.setStyleSheet("""
        QWidget{
            background:#2563eb;
            border-radius:35px;
        }
        """)

        self.anim = QPropertyAnimation(self, b"geometry")

        self.timer = QTimer()
        self.timer.timeout.connect(self.pulse)

    def start_animation(self):

        self.timer.start(400)

    def stop_animation(self):

        self.timer.stop()

    def pulse(self):

        g = self.geometry()

        self.anim.stop()

        self.anim.setDuration(200)

        self.anim.setStartValue(g)

        self.anim.setEndValue(QRect(
            g.x()-3,
            g.y()-3,
            g.width()+6,
            g.height()+6
        ))

        self.anim.start()


class CardinalisUI(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Cardinalis")

        self.resize(420, 500)

        self.setStyleSheet("""
        QWidget{
            background:#0f172a;
            color:white;
        }
        QLineEdit{
            background:#1e293b;
            padding:8px;
            border-radius:8px;
        }
        QPushButton{
            background:#2563eb;
            border-radius:8px;
            padding:6px;
        }
        """)

        layout = QVBoxLayout()

        self.chat = QTextBrowser()

        self.input = QLineEdit()

        self.input.setPlaceholderText("Escribe...")

        self.input.returnPressed.connect(self.send_message)

        self.minimize_button = QPushButton("—")

        self.minimize_button.clicked.connect(self.minimize_to_widget)

        layout.addWidget(self.minimize_button)

        layout.addWidget(self.chat)

        layout.addWidget(self.input)

        self.setLayout(layout)

        self.bubble = VoiceBubble()

        self.move_to_corner()

    def move_to_corner(self):

        screen = QApplication.primaryScreen().geometry()

        x = screen.width() - 440
        y = screen.height() - 520

        self.move(x, y)

    def minimize_to_widget(self):

        self.hide()

        screen = QApplication.primaryScreen().geometry()

        x = screen.width() - 90
        y = screen.height() - 120

        self.bubble.move(x, y)

        self.bubble.show()

    def restore_window(self):

        self.bubble.hide()

        self.show()

    def send_message(self):

        text = self.input.text().strip()

        if text == "":
            return

        self.input.clear()

        self.chat.append(f"<b>Tú:</b> {text}")

        threading.Thread(target=self.process_message, args=(text,)).start()

    def process_message(self, text):

        self.bubble.start_animation()

        add_message("user", text)

        response = ask_llm(text)

        add_message("assistant", response)

        self.chat.append(f"<b>Cardinalis:</b> {response}")

        speak(response)

        self.bubble.stop_animation()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = CardinalisUI()

    window.show()

    sys.exit(app.exec())