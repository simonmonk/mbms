input.onButtonPressed(Button.A, () => {
    music.beginMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
})
input.onButtonPressed(Button.B, () => {
    music.beginMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
})