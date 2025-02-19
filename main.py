from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


def set_volume(value):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() != "System Sounds":
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMasterVolume(value, None)


if __name__ == "__main__":
    set_volume(0.05)

'''
// to run script
pip install pycaw comtypes

// to build .exe
pip install pyinstaller
pyinstaller --onefile main.py
'''