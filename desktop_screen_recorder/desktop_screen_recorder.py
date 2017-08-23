#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Desktop screen recorder."""
import os
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk  # noqa

__all__ = ['builder']


class Handler:
    """Handler."""

    def recordbutton(self, button):
        """Record button"""
        global entry
        filepathandname = os.environ["HOME"] + "/" + entry.get_text() + '.avi'
        os.environ["filename"] = filepathandname
        os.system(
            """avconv -f x11grab -r 25 -s `xdpyinfo | grep 'dimensions:'|
            awk '{print $2}'` -i :0.0 -vcodec libx264 -threads 4 $filename -y &
            """
        )

    def stopbutton(self, button):
        """
        Run the 'killall avconv' command when the stop button is clicked.

        :param button: Stop button
        """
        os.system("killall avconv")

    def playbutton(self, button):
        """
        Run the 'avplay' command in the shell to play the recorded

        file when the play button is clicked.
        """
        os.system("avplay $filename &")


def builder():
    """We just imported the 'ui.glade' file."""
    global entry
    builder = Gtk.Builder()
    builder.add_from_file("ui.glade")
    builder.connect_signals(Handler())
    window = builder.get_object("window1")
    entry = builder.get_object("entry1")
    entry.set_text('Enter filename')

    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
