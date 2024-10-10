Set objShell = CreateObject("WScript.Shell")

lyrics = Array( _
    "Never gonna give you up", _
    "Never gonna let you down", _
    "Never gonna run around and desert you", _
    "Never gonna make you cry", _
    "Never gonna say goodbye", _
    "Never gonna tell a lie and hurt you" _
)

Do
    For i = 0 To UBound(lyrics)
        objShell.Popup lyrics(i), 0, "Got rickrolled LMAO!!"
    Next
Loop
