"""Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

import pygame
import threading

pygame.init()
pygame.mixer.music.load("exercicios/fat.mp3")
pygame.mixer.music.play(start=60)
threading.Timer(10, lambda: pygame.mixer.music.stop()).start()
input()
pygame.event.wait()

