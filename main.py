import soundfile as sf
import sounddevice as sd
import os


def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text


# Given Path for saving record and playing sound file. YOU SHOULD THIS SIGN { / } INSTEAD OF { \ }  #
path = ""
duration = 0
channels = 1
freq = 44100
sd.default.samplerate = freq
sd.default.channels = channels


if not(os.path.exists(path)):
    print("path does not exist")

while os.path.exists(path):

    select = input("record = r \nplay = p \nexit = e\nselect: ")

    if select == "r":

        duration = int_or_str((input("record time (max 10 sec): ")))

        while True:

            if type(duration) != int:

                print("please give a integer value")
                duration = int_or_str(input("record time (max 10 sec): "))

            if type(duration) == int:

                while duration <= 0 or duration >= 11:

                    print("please give a integer value between 1-10: ")
                    duration = int_or_str(input("record time (max 10 sec): "))

                    if type(duration) != int:
                        break

            if type(duration) == int:
                break

        print("record starting...")
        recorded_sound = sd.rec(int(duration * freq))
        sd.wait()
        print("record completed")
        file_name = input("File name: ")

        while f"{file_name}.wav" in os.listdir(path):

            over_write_selection = input("There is a file which has this name. Do you want to overwrite Y/N:")

            if over_write_selection == "N":

                file_name = input("Please give a different name: ")

            elif over_write_selection == "Y":

                sf.write(f"{path}{file_name}.wav", recorded_sound, freq)
                break
            else:
                print("wrong key")

        if not(f"{file_name}.wav" in os.listdir(path)):

            sf.write(f"{path}{file_name}.wav", recorded_sound, freq)

    elif select == "p":

        print("sound files")
        i = 0

        for x in os.listdir(path):
            if x.endswith(".wav"):
                print(f"[{i}] {x}")
                i += 1

        if i != 0:

            file_index_forplay = int_or_str(input("Give index of file: "))
            i = 0

            for x in os.listdir(path):
                if x.endswith(".wav"):

                    if i == file_index_forplay:
                        file_name_forplay = x
                    i += 1

            try:
                sd.play(sf.read(f"{path}{file_name_forplay}")[0])
                sd.wait()
                file_name_forplay = None
            except NameError:
                print("Index did not find!")
            except:
                print("Something goes wrong!")
        else:
            print("Sound file is not found!!")

    elif select == "e":
        break

    else:
        print("wrong key")
