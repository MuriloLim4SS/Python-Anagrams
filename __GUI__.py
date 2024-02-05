import flet as ft
from __anagram__ import *

def main(page):
    def btn_anagram(e):
        if not txt_anagram.value:
            txt_anagram.error_text = "Please enter one or more words"
            page.update()
        else:
            new_anagram = Anagram(txt_anagram.value)
            new_anagram.anagram()
            text = new_anagram.print_words
            page.clean()
            page.add(ft.Text(f"{text}"))


    txt_anagram = ft.TextField()

    page.add(txt_anagram, ft.ElevatedButton("Create Anagram", on_click=btn_anagram))


ft.app(target=main)
